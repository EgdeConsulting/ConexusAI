<script>
  import { ChatbotInterface, NavbarSet, SendIcon, ExpandedButton } from "$lib";

  function test() {
    alert("test method");
  }
  // const NavbarButtonsArray = [
  //   { icon: SendIcon, text: "text 1", method: test },
  //   { icon: SendIcon, text: "text 2", method: test },
  //   { icon: SendIcon, text: "text 3", method: test },
  // ];
  let buttons = [
    {
      id: "LagGraf",
      icon: SendIcon,
      text: "Lag graf...",
      subButtons: [
        { text: "Linjediagram", method: test, icon: SendIcon },
        { text: "Søylediagram", method: test, icon: SendIcon },
        { text: "Kakediagram", method: test, icon: SendIcon },
      ],
    },
    {
      id: "download",
      icon: SendIcon,
      text: "Download",
      subButtons: [
        { text: "Download as PDF", method: test, icon: SendIcon },
        { text: "Download as Excel", method: test, icon: SendIcon },
      ],
    },
    {
      id: "send",
      icon: SendIcon,
      text: "Send",
      subButtons: [
        { text: "Send as PDF", method: test, icon: SendIcon },
        { text: "Send as Excel", method: test, icon: SendIcon },
      ],
    },
    {
      id: "send",
      icon: SendIcon,
      text: "Del chat...",
      method: test,
    },
    {
      id: "send",
      icon: SendIcon,
      text: "hjelp...",
      method: test,
    },
  ];
  let showNavbar = true;
</script>

<div class="main-container">
  <section class="navbar-container">
    <NavbarSet {buttons} {showNavbar} />
    <!-- <ExpandedButton {buttons} /> -->
  </section>
  <aside class="chat-interface {showNavbar ? '' : 'full-width'}">
    <ChatbotInterface />
  </aside>
</div>

<style>
  div {
    font-family: "Open Sans";
  }
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
    flex-grow: 1; /* Tar opp resterende plass */
    background-color: #f0f0f0; /* Eksempel på bakgrunnsfarge */
    height: auto;
  }
  .chat-interface.full-width {
    width: 100%; /* Tar opp hele bredden når navbar ikke vises */
    position: center;
  }
</style>
