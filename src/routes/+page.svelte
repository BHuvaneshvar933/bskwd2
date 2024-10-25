<script>
	import { onMount } from 'svelte';

	let educationLevel = '';
	let currentRole = '';
	let desiredRole = '';
	let userSkills = '';
	let response = null; // Store the response from the backend
	let error = null; // Store error messages if any
	let loading = false;

	$: isWorking = educationLevel === 'Working';

	const educationLevels = ['School', 'College', 'Postgrad', 'Working'];

	const handleSubmit = async (event) => {
		event.preventDefault(); // Prevent the default form submission behavior
		error = null; // Reset error message
		response = null; // Reset response
		loading = true;

		// Construct the payload
		const payload = {
			educationLevel,
			currentRole: isWorking ? currentRole : null,
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

			// Ensure technologies_to_learn_in_order is an array of objects
			if (Array.isArray(response.technologies_to_learn_in_order)) {
				response.technologies_to_learn_in_order = response.technologies_to_learn_in_order.map(
					(tech) => {
						if (typeof tech === 'string') {
							return { name: tech, description: '' };
						}
						return tech;
					}
				);
			} else {
				response.technologies_to_learn_in_order = [];
			}
		} catch (err) {
			error = err.message; // Set the error message
			console.error(err); // Log the error to the console
		} finally {
			loading = false;
		}
	};

	function isNonEmptyArray(arr) {
		return Array.isArray(arr) && arr.length > 0;
	}
</script>

<h1>Job Role Recommendations</h1>
<form on:submit={handleSubmit}>
	<label>
		Current Level of Education:
		<select bind:value={educationLevel} required>
			<option value="" disabled selected>Select education level</option>
			{#each educationLevels as level}
				<option value={level}>{level}</option>
			{/each}
		</select>
	</label>
	<br />

	{#if isWorking}
		<label>
			Current Role:
			<input type="text" bind:value={currentRole} required />
		</label>
		<br />
	{/if}

	<label>
		Desired Role:
		<input type="text" bind:value={desiredRole} required />
	</label>
	<br />

	<label>
		User Skills:
		<input type="text" bind:value={userSkills} required />
	</label>
	<br />

	<button type="submit">Get Recommendations</button>
</form>

{#if loading}
	<div class="skeleton">
		<div class="skeleton-item"></div>
		<div class="skeleton-item"></div>
		<div class="skeleton-item"></div>
		<div class="skeleton-item"></div>
	</div>
{:else if response}
	<h2>Recommendations</h2>
	<h3>Current Role: {response.current_role}</h3>
	<h3>Desired Role: {response.desired_role}</h3>

	{#if isNonEmptyArray(response.key_skills)}
		<h4>Key Skills:</h4>
		<ul>
			{#each response.key_skills as skill}
				<li>{skill}</li>
			{/each}
		</ul>
	{/if}

	{#if isNonEmptyArray(response.essential_projects)}
		<h4>Essential Projects:</h4>
		<ul>
			{#each response.essential_projects as project}
				<li>{project}</li>
			{/each}
		</ul>
	{/if}

	{#if isNonEmptyArray(response.technologies_to_learn_in_order)}
		<h4>Technologies to Learn (in order):</h4>
		<ol>
			{#each response.technologies_to_learn_in_order as tech}
				<li>
					<strong>{tech.name}</strong>
					{#if tech.description}
						<p>{tech.description}</p>
					{:else}
						<p>No description available.</p>
					{/if}
				</li>
			{/each}
		</ol>
	{/if}
{/if}

{#if error}
	<h2>Error</h2>
	<p>{error}</p>
{/if}

<style>
	.skeleton {
		margin-top: 20px;
	}

	.skeleton-item {
		height: 20px;
		background-color: #f0f0f0;
		margin-bottom: 10px;
		border-radius: 4px;
		animation: pulse 1.5s infinite;
	}

	@keyframes pulse {
		0% {
			opacity: 0.6;
		}
		50% {
			opacity: 1;
		}
		100% {
			opacity: 0.6;
		}
	}

	.roadmap {
		display: flex;
		flex-direction: column;
		align-items: center;
		gap: 20px;
	}

	.tech-box {
		border: 2px solid #007bff;
		border-radius: 10px;
		padding: 15px;
		max-width: 300px;
		text-align: center;
		background-color: #f8f9fa;
	}

	.tech-box h5 {
		margin: 0 0 10px 0;
		color: #007bff;
	}

	.tech-box p {
		margin: 0;
		font-size: 0.9em;
	}

	.arrow {
		font-size: 24px;
		color: #007bff;
	}
</style>
