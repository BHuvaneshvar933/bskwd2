<script>
	import { onMount } from 'svelte';

	let educationLevel = '';
	let currentRole = '';
	let desiredRole = '';
	let userSkills = '';
	let response = null;
	let error = null;
	let loading = false;
	let loadingMessages = [
		'Searching for your perfect roadmap...',
		'Cooking up jobs...',
		'Analyzing career paths...',
		'Crunching skill data...',
		'Preparing your personalized plan...'
	];
	let currentLoadingMessage = '';

	$: isWorking = educationLevel === 'Working';

	const educationLevels = ['School', 'College', 'Postgrad', 'Working'];

	const handleSubmit = async (event) => {
		event.preventDefault();
		error = null;
		response = null;
		loading = true;
		rotateLoadingMessages();

		const payload = {
			educationLevel,
			currentRole: isWorking ? currentRole : 'fresher',
			desiredRole,
			userSkills
		};

		try {
			const res = await fetch('http://localhost:3001/api/recommend', {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json'
				},
				body: JSON.stringify(payload)
			});

			if (!res.ok) {
				throw new Error('Failed to fetch recommendations');
			}

			response = await res.json();
			console.log('Frontend received response:', JSON.stringify(response, null, 2));
		} catch (err) {
			error = err.message;
			console.error(err);
		} finally {
			loading = false;
		}
	};

	function rotateLoadingMessages() {
		let index = 0;
		const intervalId = setInterval(() => {
			currentLoadingMessage = loadingMessages[index];
			index = (index + 1) % loadingMessages.length;
			if (!loading) clearInterval(intervalId);
		}, 2000);
	}

	onMount(() => {
		document.body.style.fontFamily = 'Inter, sans-serif';
	});
</script>

<main>
	<h1>betterjobs</h1>

	<form on:submit={handleSubmit}>
		<h2>What is your current Education Level?</h2>
		<div class="education-grid">
			{#each educationLevels as level}
				<button
					type="button"
					class:selected={educationLevel === level}
					on:click={() => (educationLevel = level)}
				>
					{level}
				</button>
			{/each}
		</div>

		{#if isWorking}
			<label>
				Current Role:
				<input
					type="text"
					bind:value={currentRole}
					required
					placeholder="e.g. Software Developer"
				/>
			</label>
		{/if}

		<label>
			Desired Role:
			<input type="text" bind:value={desiredRole} required placeholder="e.g. Data Scientist" />
		</label>

		<label>
			Current Skills:
			<input
				type="text"
				bind:value={userSkills}
				required
				placeholder="e.g. Python, JavaScript, SQL"
			/>
		</label>

		<button type="submit" class="submit-btn">Get Recommendations</button>
	</form>

	{#if loading}
		<div class="loading-message">
			<p>{currentLoadingMessage}</p>
		</div>
	{/if}

	{#if response}
		<div class="results-container">
			<h2>Recommendations</h2>
			<h3>Current Role: {response.current_role}</h3>
			<h3>Desired Role: {response.desired_role}</h3>

			<div class="results-grid">
				<div class="section">
					<h4>Key Skills:</h4>
					<ul>
						{#each response.key_skills as skill}
							<li>{skill}</li>
						{/each}
					</ul>
				</div>

				<div class="section">
					<h4>Essential Projects:</h4>
					<ul>
						{#each response.essential_projects as project}
							<li>{project}</li>
						{/each}
					</ul>
				</div>
			</div>

			<div class="section">
				<h4>Technologies to Learn (Roadmap):</h4>
				<div class="roadmap">
					{#each response.technologies_to_learn_in_order as tech, index}
						<div class="roadmap-item">
							<strong>{tech}</strong>
						</div>
						{#if index < response.technologies_to_learn_in_order.length - 1}
							<div class="arrow">↓</div>
						{/if}
					{/each}
				</div>
			</div>
		</div>
	{/if}

	{#if error}
		<div class="error-message">
			<h2>Error</h2>
			<p>{error}</p>
		</div>
	{/if}
</main>

<style>
	:global(body) {
		background-color: #f5f5f5;
		margin: 0;
		padding: 0;
		font-family: 'Inter', sans-serif;
	}

	main {
		max-width: 800px;
		margin: 0 auto;
		padding: 2rem;
	}

	h1 {
		font-size: 3rem;
		font-weight: 900;
		margin-bottom: 2rem;
	}

	h2 {
		font-size: 1.5rem;
		font-weight: 600;
		margin-bottom: 1rem;
	}

	.education-grid {
		display: grid;
		grid-template-columns: repeat(2, 1fr);
		gap: 1rem;
		margin-bottom: 1.5rem;
	}

	button {
		background-color: #fff;
		border: 2px solid #e0e0e0;
		border-radius: 8px;
		padding: 1rem;
		font-size: 1rem;
		cursor: pointer;
		transition: all 0.2s ease-in-out;
	}

	button.selected {
		background-color: #007bff;
		color: #fff;
		border-color: #007bff;
	}

	label {
		display: block;
		margin-bottom: 1rem;
	}

	input {
		width: 100%;
		padding: 0.5rem;
		font-size: 1rem;
		border: 2px solid #e0e0e0;
		border-radius: 4px;
		margin-top: 0.25rem;
	}

	.submit-btn {
		background-color: #007bff;
		color: #fff;
		border: none;
		border-radius: 4px;
		padding: 0.75rem 1.5rem;
		font-size: 1rem;
		cursor: pointer;
		transition: background-color 0.2s ease-in-out;
	}

	.submit-btn:hover {
		background-color: #0056b3;
	}

	.loading-message {
		text-align: center;
		font-size: 1.2rem;
		color: #007bff;
		margin-top: 2rem;
	}

	.results-container {
		margin-top: 2rem;
		background-color: #fff;
		border-radius: 8px;
		padding: 2rem;
		box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
	}

	.results-grid {
		display: grid;
		grid-template-columns: 1fr 1fr;
		gap: 2rem;
	}

	.roadmap {
		display: flex;
		flex-direction: column;
		align-items: center;
	}

	.roadmap-item {
		background-color: #f0f0f0;
		border-radius: 8px;
		padding: 1rem;
		margin-bottom: 1rem;
		width: 100%;
		max-width: 400px;
	}

	.roadmap-item strong {
		display: block;
		margin-bottom: 0.5rem;
		font-size: 1.1rem;
	}

	.roadmap-item p {
		margin: 0;
		font-size: 0.9rem;
	}

	.arrow {
		font-size: 1.5rem;
		color: #007bff;
		margin: 0.5rem 0;
	}
</style>
