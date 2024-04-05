<script>
  export let buttons = [];
  import { MissingIcon } from "$lib";
  let expandedButton = null;

  function toggleButton(button) {
    if (button.subButtons && button.subButtons.length > 0) {
      expandedButton = expandedButton === button.id ? null : button.id;
    } else if (button.method) {
      button.method();
    }
  }
</script>

{#each buttons as button}
  <div>
    <button on:click={() => toggleButton(button)} class="button">
      <div class="image-wrapper">
       
        {#if button.icon }
        <svelte:component this={button.icon} color={button === expandedButton ? "black" : "white"} height=1.5em width=1.5em />
        
        {:else}

        <svelte:component this={MissingIcon} />
        
        {/if}
        
      </div>
      <p>{button.text}</p> 
    </button>
    {#if expandedButton === button.id && button.subButtons}
    <div class="sub-buttonsmargin">
      {#each button.subButtons as subButton}
        <button on:click={subButton.method} class="button sub-button">
          <div class="image-wrapper">
            <svelte:component this={subButton.icon} color="black" height=1.5em width=1.5em/>

          </div>
          {subButton.text}
        </button>
      {/each}
    </div>
    {/if}
  </div>
{/each}

<style>
  .button {
    display: flex;
    align-items: center;
    background: none;
    border: none;
    cursor: pointer;
    width: 100%;
    height: 2.2rem;
    height: 50px;
    flex: none;
    order: 0;
    flex-grow: 0;
  }

  .sub-button {
    background-color: aliceblue;
    position: static;
    width: 192px;
    height: 2.5em;
    left: 0px;
    top: 1px;
    margin-left: 0.5em;
   
    font: regular Open Sans;
    padding-top: 0.5em;
    
  }
  .sub-buttonsmargin{
    margin: 0.5em;
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
  .image-wrapper {
    display: flex;
    justify-content: center;
    align-items: center;
   margin: 0.5em;
    /* filter: invert(100%); */
  }

  .button,
  .sub-button {
    transition: background-color 0.3s ease; /* Gjør overgangen jevn */
  }

  .sub-button:hover {
    background-color: #f0f0f0; /* Lys grå bakgrunn på hover */
    transform: scale(1.02);
  }
  .button:hover {
    /* Lys grå bakgrunn på hover */
    transform: scale(1.02);
  }

  .sub-button:active {
    background-color: #e6e6c8; /* Mørkere grå bakgrunn når knappen er trykket */
    transform: scale(
      0.98
    ); /* Gjør knappen litt mindre for å gi en trykkeffekt */
  }
  .button:active {
    background-color: #deddb7; /* Mørkere grå bakgrunn når knappen er trykket */
    transform: scale(
      1.02
    ); /* Gjør knappen litt mindre for å gi en trykkeffekt */
  }
</style>
