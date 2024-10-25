import express from 'express';
import bodyParser from 'body-parser';
import cors from 'cors';
import ollama from 'ollama';

const app = express();
const PORT = 3001;

app.use(cors());
app.use(bodyParser.json());

const modelfile = `
FROM llama3.2
SYSTEM "You are an AI Job/career consultant who gives concise, JSON-formatted responses with only key points for transitioning between roles. DO NOT FOR ANY REASON SAY ANYTHING EXCEPT THAT BRO. BE PRECISE AND SHIT."
`;

// Start Ollama model
await ollama.create({ model: 'example', modelfile: modelfile });

function createRoadmap(technologies) {
    if (!Array.isArray(technologies) || technologies.length === 0) {
        console.log('No technologies provided for roadmap');
        return null;
    }
    let roadmap = '';
    for (let i = 0; i < technologies.length; i++) {
        roadmap += `[${technologies[i]}]`;
        if (i < technologies.length - 1) {
            roadmap += '\n    |\n    v\n';
        }
    }
    console.log('Generated roadmap:', roadmap);
    return roadmap;
}

async function getOllamaResponse(message, retries = 3) {
    for (let i = 0; i < retries; i++) {
        try {
            let jsonResponse = '';
            const response = await ollama.chat({ model: 'llama3.2', messages: [message], stream: true });
            for await (const part of response) {
                jsonResponse += part.message.content;
            }

            const jsonMatch = jsonResponse.match(/({[^]*})/);
            if (jsonMatch && jsonMatch[1]) {
                const validJson = jsonMatch[1];
                const parsedResponse = JSON.parse(validJson);
                if (Object.keys(parsedResponse).length > 0) {
                    return parsedResponse;
                }
            }
        } catch (error) {
            console.error(`Attempt ${i + 1} failed:`, error);
        }
    }
    throw new Error('Failed to get a valid response from Ollama after multiple attempts');
}

app.post('/api/recommend', async (req, res) => {
    let { educationLevel, currentRole, desiredRole, userSkills } = req.body;

    currentRole = currentRole || "fresher";

    const message = {
        role: 'user',
        content: `Generate a short and structured JSON response with key skills and technologies for education level of ${educationLevel} and transitioning from ${currentRole} to ${desiredRole} based on the following skills: ${JSON.stringify(userSkills)}. Respond only in the following JSON format: {
            "current_role": "${currentRole}",
            "desired_role": "${desiredRole}",
            "key_skills": ["<skill_1>", "<skill_2>", "..."],
            "essential_projects": ["<project_1>", "<project_2>", "..."],
            "technologies_to_learn_in_order": [
                {
                    "name": "<technology_1>",
                    "description": "<brief description and tips for learning based on ${educationLevel} level>"
                },
                {
                    "name": "<technology_2>",
                    "description": "<brief description and tips for learning based on ${educationLevel} level>"
                },
                ...
            ] (up to however many technologies needed)
        }`
    };

    try {
        const parsedResponse = await getOllamaResponse(message);
        console.log('Parsed response:', JSON.stringify(parsedResponse, null, 2));
        res.json(parsedResponse);
    } catch (error) {
        console.error('Error in /api/recommend:', error);
        res.status(500).json({ error: "An error occurred while processing your request." });
    }
});

app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
