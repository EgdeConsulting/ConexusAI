<script>
    export let messages = [];
    export let isBotTyping;
  </script>
  
  <div class="messages">
    {#each messages as message}
      <div class={`message ${message.sender}`}>
        <span class="sender">{message.sender === "user" ? "Du:" : "ConexusAI:"}</span>
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
  .message {
    margin: 5px 0;
    padding: 5px;
    border-radius: 5px;
  }
  .sender {
    font-weight: bold;
    display: block; /* Gjør at sender-labelen vises over meldingsteksten */
    text-align: left;
  }
  .text {
    word-wrap: break-word; /* Sikrer at lange ord ikke strekker containeren */
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