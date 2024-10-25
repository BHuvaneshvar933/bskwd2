<script>
  let isApplied = false;
  let isRejected = false; // New flag to control rendering
  export let role = "unknown";
  export let description = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.";

  function applyJob() {
    isApplied = true;
  }

  function rejectJob() {
    isRejected = true; // Set to true to hide component
  }
</script>

{#if !isRejected}
  <div class="job-card">
    <div class="job-details">
      <h3 class="job-title">{role}</h3>
      <p class="job-description">
        {description}
      </p>
    </div>
    <div class="job-actions">
      <button class="apply-button" on:click={applyJob} disabled={isApplied} style="background-color: green;">
        {isApplied ? 'Applied' : 'Apply'}
      </button>
      <button class="reject-button" on:click={rejectJob} style="background-color: red;">
        Reject
      </button>
    </div>
  </div>
{/if}

<style>
  .job-card {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: #999;
    padding: 20px;
    border-radius: 15px;
    width: 70%;
    margin-bottom: 20px;
    color: white;
  }

  .job-details {
    flex-grow: 1;
  }

  .job-title {
    font-size: 1.5rem;
    font-weight: bold;
    margin-bottom: 10px;
  }

  .job-description {
    font-size: 1rem;
    line-height: 1.5;
  }

  .job-actions {
    display: flex;
    flex-direction: column;
    gap: 10px;
  }

  .apply-button, .reject-button {
    width: 100px;
    height: 40px;
    color: white;
    border: none;
    cursor: pointer;
    border-radius: 5px;
    font-size: 1rem;
  }

  .apply-button[disabled] {
    background-color: gray;
    cursor: not-allowed;
  }
</style>
