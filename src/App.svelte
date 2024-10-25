<script>
    let currentRole = '';
    let desiredRole = '';
    let userSkills = {
        programming: '',
        data_analysis: '',
        machine_learning: '',
        statistics: '',
        communication_skills: ''
    };
    let responseData = null;

    async function fetchRecommendations() {
        const response = await fetch('http://localhost:3001/api/recommend', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ currentRole, desiredRole, userSkills })
        });
        responseData = await response.json();
    }
</script>

<form on:submit|preventDefault={fetchRecommendations}>
    <input type="text" bind:value={currentRole} placeholder="Current Role" required />
    <input type="text" bind:value={desiredRole} placeholder="Desired Role" required />
    <input type="text" bind:value={userSkills.programming} placeholder="Programming Skills" />
    <input type="text" bind:value={userSkills.data_analysis} placeholder="Data Analysis Skills" />
    <input type="text" bind:value={userSkills.machine_learning} placeholder="Machine Learning Skills" />
    <input type="text" bind:value={userSkills.statistics} placeholder="Statistics Skills" />
    <input type="text" bind:value={userSkills.communication_skills} placeholder="Communication Skills" />
    <button type="submit">Get Recommendations</button>
</form>

{#if responseData}
    <pre>{JSON.stringify(responseData, null, 2)}</pre>
{/if}
