<script>
  import SendIcon from "$lib/images/send.png";
  import LoadingIcon from "$lib/images/tube-spinner.svg";
  export let sendMessage;
  export let userInput;
  export let isLoading;
  let placeholderInput = "Spør AI....";
  function handleKeyDown(event) {
    // Send message when Enter is pressed, the input is not loading, not empty, and not placeholder text
    if (event.key === "Enter") {
      sendMessageIfValid();
    }
  }

  function sendMessageIfValid() {
    if (
      !isLoading &&
      userInput.trim() !== "" &&
      userInput !== placeholderInput
    ) {
      sendMessage(userInput);
      console.log("User input:", userInput);
      userInput = ""; // Reset input field
    }
  }
</script>

<div class="input-container">
  <div class="input-area">
    <input
      type="textarea"
      bind:value={userInput}
      on:keydown={handleKeyDown}
      placeholder={placeholderInput}
    />
  </div>
  <div class="btn-tull">
    <button on:click={sendMessageIfValid} disabled={isLoading}>
      {#if isLoading}
        <img src={LoadingIcon} alt="Laster" />
      {:else}
        <img src={SendIcon} alt="Send" />
      {/if}
    </button>
  </div>
</div>

<style>
  .input-container {
    display: flex;
    margin-bottom: 0.625em;
  }
  .input-area {
    background-color: #ffffff;
    height: 3em;
    filter: drop-shadow(0px 4px 4px rgba(0, 0, 0, 0.25));
    border-radius: 0.3125em;
    border: 1px solid #00244e;
    padding: 0.3125em;
    margin-right: 0.625em;
    width: 95.6%;
  }
  .input-area input {
    color: #7a828b;
    text-align: left;
    vertical-align: text-top;
    /* font-size: 14px; */
    font-family: Open Sans;
    line-height: auto;
    border-style: hidden;
    outline: none;
    height: 100%;
    width: 100%;
  }
  .input-container button {
    background-color: #ffffff;
    height: 3em;
    width: 3em;
    filter: drop-shadow(0px 4px 4px rgba(0, 0, 0, 0.25));
    border-radius: 0.3125em;
    border: 1px solid #00244e;
  }

  button img {
    width: 3em; /* Juster bredden etter behov */
    height: 3em; /* Beholder bildets aspektforhold */
  }
  .btn-tull button {
    font-size: 1em;
    width: 100%; /* Juster bredden etter behov */
    height: 100%;
  }
</style>
