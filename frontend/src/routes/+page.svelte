<script>
  import { ChatbotInterface, NavbarSet, SendIcon } from "$lib";

  function test() {
    alert("test method");
  }
  const NavbarButtonsArray = [
    { icon: SendIcon, text: "text 1", method: test },
    { icon: SendIcon, text: "text 2", method: test },
    { icon: SendIcon, text: "text 3", method: test },
  ];
  let showNavbar = true;
</script>

<div class="main-container">
  <section class="navbar-container">
    <NavbarSet {NavbarButtonsArray} {showNavbar} />
  </section>
  <aside class="chat-interface">
    <ChatbotInterface />
  </aside>
</div>

<style>
  .main-container {
    display: flex;
    height: 100vh; /* Fyller hele skjermens høyde */
    margin: 0;
  }
  .navbar-container {
    width: 12em;
    overflow: hidden;
    color: white; /* Tekstfarge */
    margin-right: 0.63em;
    height: auto;
  }
  .chat-interface {
    flex-grow: 10; /* Tar opp resterende plass */
    background-color: #f0f0f0; /* Eksempel på bakgrunnsfarge */
    height: auto;
  }
</style>
