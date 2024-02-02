<script>
  import { ChatbotInterface, NavbarButtons, ShareChatIcon } from "$lib";

  function test() {
    alert("test method");
  }
  const NavbarButtonsArray = [
    { picture: ShareChatIcon, text: "text 1", method: test },
    { picture: ShareChatIcon, text: "text 2", method: test },
  ];
</script>

<nav
  style="display: flex; align-items: center; justify-content: center; height: 100vh;"
>
  <section class="container">
    <NavbarButtons {NavbarButtonsArray} />
  </section>
  <aside><ChatbotInterface /></aside>
</nav>
<nav></nav>

<style>
  .container {
    border-top: 1px solid #333;
    border-bottom: 1px solid #333;
    min-height: 200px;
    height: calc(100vh - 15em);
    width: 20%;
  }
  aside {
    /* Juster bredden etter behov */
    width: 80%; /* Eksempel: Gjør chatbot-interface 80% av skjermens bredde */
    padding: 1em; /* Legger til litt padding rundt chatbot-interface for estetikk */
  }
</style>
