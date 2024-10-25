<svelte:head>
  <title>Home</title>
  <meta name="description" content="Svelte demo app" />
</svelte:head>

<div class="top">
  <Title />
  <ProfileIcon />
</div>

<div class="container">
  <div class="header">
    <h1 class="logo">betterjobs</h1>
    <div class="profile-icon"></div>
  </div>

  <div class="cta">
    <button class="cta-button" on:click={handleCTA}>
      Start Your Journey Now!
    </button>
  </div>
</div>

<script>
  // You can add any functionality if needed later
  function handleCTA() {
    alert('Journey started!'); // Placeholder for CTA action
  }
</script>

<style>
  .top {
    display: flex;
    padding: 3rem;
    justify-content: space-between;
  }

  .container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-around;
    height: 100vh;
    background-color: white;
  }

  .header {
    display: flex;
    justify-content: space-between;
    width: 90%;
    padding: 20px;
  }

  .logo {
    font-size: 3rem;
    font-weight: bold;
    margin: 0;
  }

  .profile-icon {
    width: 50px;
    height: 50px;
    background-color: lightgray;
    border-radius: 50%;
  }

  .cta {
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: #4b3227;
    border-radius: 20px;
    padding: 1.5rem;
    width: 80%;
  }

  .cta-button {
    background-color: #c0c0c0;
    padding: 10px 30px;
    border: none;
    border-radius: 10px;
    font-size: 1rem;
    font-weight: bold;
    cursor: pointer;
  }

  .cta-button:hover {
    background-color: #a0a0a0;
  }
</style>
