<script>
  let searchQuery = '';

  function handleSearch() {
    alert(`Searching for: ${searchQuery}`);
    // Add your job search logic here
  }
</script>

<div class="search-bar">
  <input
    type="text"
    placeholder="python, data analyst, machine learning... etc."
    bind:value={searchQuery}
    class="search-input"
  />
  <button class="search-button" on:click={handleSearch}>
    suggest me jobs
  </button>
</div>

<style>
  .search-bar {
    display: flex;
    margin: 30` px 0;
    /* gap: 10px; */
    align-items: center;
    justify-content: center;
  }
  
  .search-input {
    padding: 35px;
    font-size: 1.5rem;
    width: 60%;
    border: 2px solid #ccc;
  }

  .search-input:focus {
    border-color: #0073e6; /* Optional: Change color on focus */
    outline: none;
  }

  .search-button {
    padding: 30px 20px;
    font-size: 1.5rem;
    font-weight: 700;
    background-color: #0C9DC5; /* Button color */
    color: white;
    border: 2px solid #0C9DC5;
    cursor: pointer;
  }

  .search-button:hover {
    background-color: #005bb5; /* Darker shade on hover */
  }
</style>
