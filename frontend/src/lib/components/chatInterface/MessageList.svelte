<script>
  import BotIcon from "../icons/BotIcon.svelte";
  export let messages = [];
  export let isBotTyping;
  import isDarkMode  from "../navbar/NavbarSet.svelte";
  
</script>

<div class="messages" >
  {#each messages as message}
    <div class={`message ${message.sender}`}>
      <span class="sender"
        >{message.sender === "user" ? "Du:" : ""}
        {#if message.sender !== "user"}
          <BotIcon class="bot-icon" />
          ConexusAI:
        {/if}
      </span>
      <!-- må endre ifra message.text til message.type === "text" for å få det til å funke -->
      {#if message.text}
        <span class="text">{message.text}</span>
      {:else if message.type === "list"}
        <ul>
          {#each message.content as item}
            <li>{item}</li>
          {/each}
        </ul>
      {:else if message.type === "image"}
        <img src={message.content} alt="Bilde fra AI" class="image-response" />
      {:else if message.type === "pdf"}
        <!-- Implementer visning av PDF -->
      {:else if message.type === "excel"}
        <!-- Implementer visning eller nedlasting av Excel-fil -->
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

<style>
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
  .dark-mode {
    background-color: #000; /* Svart bakgrunn for mørkt tema */
    color: #140c0c; /* Hvit tekst for mørkt tema */
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
    display: flex;
    align-items: center;
    font-weight: bold;
    text-align: left;
  }
  .bot-icon {
    margin-right: 1.5em; /* Plasserer bot-ikonet til høyre for sender-labelen */
  }
  .text {
    word-wrap: break-word; /* Sikrer at lange ord ikke strekker containeren */
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
