<script>
  import { ExpandedButton, Switch } from "$lib";
  import { writable } from "svelte/store";

  export const isDarkMode = writable(false);
  export let buttons = [];
  export let showNavbar = false;
</script>

{#if showNavbar}
  <div class="navbar-set">
    <p class="LogoConexusAI">ConexusAI</p>
    <div class="switch-container">
      <div>
        <Switch bind:checked={$isDarkMode} />
      </div>
      <div>
        <p class="dark-modus">Mørk modus</p>
      </div>
    </div>
    <ExpandedButton {buttons} />
  </div>
{/if}

<style>
  .navbar-set {
    position: relative;
    box-shadow: 2px 5px rgba(0, 0, 0, 0.1);
    background-color: #00244e;
    height: 100%;
    width: 100%;

    /* display: flex; */
    /* flex-direction: column; */
    /* align-items: center; */
  }
  .LogoConexusAI {
    margin: 0px;
    width: auto;
    height: 1.7rem;
    font-family: "Open Sans";
    font-style: normal;
    font-weight: bold;
    font-size: 1.5em;
    line-height: 27px;
    text-align: center;
    color: #ffa800;
    text-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
  }
  .switch-container {
    display: flex;
    align-items: center; /* Sentrerer elementene vertikalt */
    gap: 0.5rem; /* Gir litt plass mellom switch og tekst */
    justify-content: center;
    margin: 0.5rem;
  }
  .dark-modus {
    height: 0.87rem;
    width: 4.3rem;
    font-family: "Open Sans";
    font-size: 0.75rem;
    white-space: nowrap; 
    color: #ffa800;
    margin: 0px;
    
  } 
</style>
