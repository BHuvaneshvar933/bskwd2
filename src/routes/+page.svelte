<script lang="ts">
  import Counter from './Counter.svelte';
  import welcome from '$lib/images/svelte-welcome.webp';
  import welcomeFallback from '$lib/images/svelte-welcome.png';
  import Title from '../components/Title.svelte';
  import ProfileIcon from '../components/ProfileIcon.svelte';
  import SearchBar from '../components/SearchBar.svelte';
  import JobListing from '../components/JobListing.svelte';

 
  let companies = ["apple", "google", "rohan"];

  
  let role = companies.map(company => ({
    component: JobListing,
    props: {
      role: company,
      description: `Job opening at ${company}. ChatGPT wooo`
    }
  }));
</script>

<svelte:head>
  <title>Home</title>
  <meta name="description" content="Svelte demo app" />
</svelte:head>

<div class="top">
  <Title />
  <ProfileIcon />
</div>
<div>
  <SearchBar />
</div>
<div class="bdy">
  {#each role as { component: Component, props }}
    
    <svelte:component this={Component} {...props} />
  {/each}
</div>

<style>
  .top {
    display: flex;
    padding: 3rem;
    justify-content: space-between;
  }

  .bdy {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 2rem;
  }
</style>
