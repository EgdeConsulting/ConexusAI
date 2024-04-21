<script>
  import SendIcon from "$lib/images/send.png";
  import LoadingsIcon from "$lib/images/tube-spinner.svg";
  import MessageList from "./MessageList.svelte";
  import InputArea from "./InputArea.svelte";
  let messages = [];
  let userInput = "";
  let isBotTyping = false;
  let isLoading = false; // Tilstandsvariabel for å spore om forespørselen er under behandling
  import { writable } from 'svelte/store';
  export const isDarkMode = writable(false);
  async function sendMessage(newMessage) {
    
    // messages = [...messages, { sender: "user", text: newMessage }];
    const newUserMessage = { sender: "user", text: newMessage };

    const newPrompt = JSON.stringify({
      prompt: "new quation to handel: " + newUserMessage.text,
    });

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
      console.log(JSON.stringify({ prompt: newUserMessage.text }));
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
      console.log("Received answer from backend:", answer);
      simulateTypingResponse(answer); // Vis svaret i chat
    } catch (error) {
      console.error("There was a problem with the fetch operation:", error);
      isLoading = false; // Sett isLoading til false
    } finally {
      isBotTyping = false;
      //messages.splice(typingIndex, 1); // Fjern "boten skriver" meldingen ved feil
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
  <MessageList {messages} {isBotTyping} />
  <InputArea {sendMessage} {userInput} {isLoading} />
</div>

<style>
  .chat-container {
    display: flex;
    flex-direction: column;
    height: 100%;
    border: 0px solid #ccc;
    padding: 0px;
  }
</style>
