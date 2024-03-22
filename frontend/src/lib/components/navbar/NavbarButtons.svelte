<!-- <script>
  // export let NavbarButtonsArray = [];
</script>

{#each NavbarButtonsArray as item}
  <button on:click={item.method}>
    <div class="image-wrapper">
      <svelte:component this={item.icon} />
    </div>
    <p>{item.text}</p>
    
  </button>
{/each}
<style>
  .image-wrapper {
   
    display: flex; 
    justify-content: center;
    align-items: center;
    filter: invert(100%);
  }
  button {
    display: flex;
    align-items: center;
    background: none;
    border: none;
    cursor: pointer;
    padding: 0.5em;
    width: 100%;
    height: fit-content;
  }
  p {
    color: #ffffff;
    text-align: left;
    vertical-align: text-middle;
    font-size: 1rem;
    font-family: Open Sans;
    line-height: auto;
    border-style: hidden;
    outline: none;

    margin-left: 0.625rem;
  }
</style> -->
