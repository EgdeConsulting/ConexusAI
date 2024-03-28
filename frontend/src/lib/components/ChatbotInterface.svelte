<script>
  import { LoadingIcon } from "$lib";
  import SendIcon from "$lib/images/send.png";
  import LoadingsIcon from "$lib/images/tube-spinner.svg"
  import { onMount } from "svelte";
  let messages = [];
  let userInput = "";
  let isBotTyping = false;
  let isLoading = false; // Tilstandsvariabel for å spore om forespørselen er under behandling

  async function sendMessage() {
    if (userInput.trim() === "") {
      return;
    }

    const newUserMessage = { sender: "user", text: userInput };

    const newPrompt = JSON.stringify({ prompt: "new quation to handel: " + newUserMessage.text });

    messages = [...messages, newUserMessage]; // Legg til brukerens melding

    userInput = ""; // Nullstill inputfeltet
    isBotTyping = true;
    isLoading = true;
    messages = [...messages, { sender: "bot", text: "" }]; // Viser at boten "skriver"
    const typingIndex = messages.length - 1;
    await new Promise((resolve) => setTimeout(resolve, 2000));
    try {
      // Kall lokale SvelteKit API-endepunkt istedenfor det eksterne
      console.log("Sending message to backend:", newUserMessage.text);
      const response = await fetch("/api/posts", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ prompt: newUserMessage.text }),
      });

      if (!response.ok) {
        throw new Error("Network response was not ok");
      }

      const { answer } = await response.json(); // Anta at responsen inneholder et felt "answer"
      isBotTyping = false;
      messages.splice(typingIndex, 1); // Fjern "boten skriver" meldingen
      simulateTypingResponse(answer); // Vis svaret i chat
    } catch (error) {
      console.error("There was a problem with the fetch operation:", error);
      
    }
    finally {
      //isLoading = false; // Sett isLoading til false uansett om forespørselen var vellykket eller ikke
      isBotTyping = false;
      messages.splice(typingIndex, 1); // Fjern "boten skriver" meldingen ved feil
    }
  }

  async function simulateTypingResponse(text) {
    console.log("Simulating response for text:", text);
    try {
      if (typeof text !== "string") {
        throw new Error("Expected text to be a string");
      }
      let partialText = "";
      for (let char of text) {
        partialText += char;
        messages = [...messages, { sender: "bot", text: partialText }];
        await new Promise((resolve) => setTimeout(resolve, 10));
        messages.pop();
      }
      messages = [...messages, { sender: "bot", text: text }];
      isLoading = false;
    } catch (error) {
      console.error("The answer is empty or not iterable:", error);
    }
  }
</script>

<div class="chat-container">
  <div class="messages">
    {#each messages as message}
      <div class={`message ${message.sender}`}>
        <span class="sender"
          >{message.sender === "user" ? "Du:" : "ConexusAI:"}</span
        >
        {#if message.text}
          <span class="text">{message.text}</span>
        {/if}
        {#if message.image}
          <img src={message.image} alt="Bilde fra AI" class="image-response" />
        {/if}
      </div>
    {/each}
    {#if isBotTyping}
      <div>
        <span class="text">
          <span class="dot"><strong>.</strong></span>
          <span class="dot"><strong>.</strong></span>
          <span class="dot"><strong>.</strong></span>
        </span>
      </div>
    {/if}
  </div>
  <div class="input-container">
    <div class="input-area">
      <input
        type="textarea"
        bind:value={userInput}
        on:keydown={(e) => e.key === "Enter" && sendMessage()}
        placeholder="Spør AI...."
      />
    </div>

    <div class="btn-tull">
      <button on:click={sendMessage}>
        {#if isLoading}
        <img src = {LoadingsIcon} alt="Laster"/>
        
        {:else}
        <img src={SendIcon} alt="Send" />
        {/if}
        
    </div>
  </div>
</div>

<style>
  .chat-container {
    display: flex;
    flex-direction: column;
    height: 100%;
    border: 0px solid #ccc;
    padding: 0px;
  }
  .messages {
    flex-grow: 1;
    overflow-y: auto;
    background-color: #ffffff;
    height: auto;
    margin: 0 0 0.625em 0;
    padding: 0.625em;
    filter: drop-shadow(0px 4px 4px rgba(0, 0, 0, 0.25));
    border-radius: 5px;
    border: 1px solid #ccc;
  }
  .message {
    margin: 5px 0;
    padding: 5px;
    border-radius: 5px;
  }
  .message.user {
    /* background-color: #007bff; */
    color: rgb(22, 20, 20);
    align-self: flex-end;
    text-align: left;
  }
  .message.bot {
    background-color: #e9ecef;
    color: black;
    align-self: flex-start;
    text-align: left;
  }
  .sender {
    font-weight: bold;
    display: block; /* Gjør at sender-labelen vises over meldingsteksten */
    text-align: left;
  }
  .text {
    word-wrap: break-word; /* Sikrer at lange ord ikke strekker containeren */
  }
  .input-container {
    display: flex;
    margin-bottom: 0.625em;
  }
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

  .btn-tull button {
    font-size: 1em;
    width: 100%; /* Juster bredden etter behov */
    height: 100%;
  }
  /* Stil for bildet inne i knappen */
  button img {
    width: 3em; /* Juster bredden etter behov */
    height: 3em; /* Beholder bildets aspektforhold */
  }
  .image-response {
    max-width: 100%;
    height: auto;
    border-radius: 5px;
  }
  @keyframes bounce {
    0%,
    100% {
      transform: translateY(0);
    }
    50% {
      transform: translateY(-5px);
    }
  }

  .dot {
    animation: bounce 1s infinite;
    display: inline-block;
    margin: 0 2px;
  }

  .dot:nth-child(1) {
    animation-delay: 0s;
  }
  .dot:nth-child(2) {
    animation-delay: 0.2s;
  }
  .dot:nth-child(3) {
    animation-delay: 0.4s;
  }
</style>
