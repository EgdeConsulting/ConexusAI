<script>
  import { ExpandedButton } from "$lib";
  
  export let buttons = [];
  export let showNavbar = false;
</script>

{#if showNavbar}
  <div class="navbar-set">
    <!-- <NavbarButtons {NavbarButtonsArray} /> -->
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
  }
</style>
