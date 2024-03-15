<script>
  import {
    ChatbotInterface,
    NavbarSet,
    SendIcon,
    Graph,
    LineChart,
    BarChart,
    PieChart,
    DownloadIcon,
    ShareChatIcon,
    DownloadAsPDF,
    DownloadAsExcel,
    HelpIcon,
  } from "$lib";
  
 
  

  function test() {
    alert("test method");
  }

  let buttons = [
    {
      id: "LagGraf",
      icon: Graph,
      text: "Lag graf...",
      subButtons: [
        { text: "Linjediagram", method: test, icon: LineChart },
        { text: "Søylediagram", method: test, icon: BarChart },
        { text: "Kakediagram", method: test, icon: PieChart },
      ],
    },
    {
      id: "download",
      icon: DownloadIcon,
      text: "Download",
      subButtons: [
        { text: "Download as PDF", method: test, icon: DownloadAsPDF },
        { text: "Download as Excel", method: test, icon: DownloadAsExcel },
      ],
    },
    {
      id: "send",
      icon: SendIcon,
      text: "Send",
      subButtons: [
        { text: "Send as PDF", method: test, icon: DownloadAsPDF },
        { text: "Send as Excel", method: test, icon: DownloadAsExcel },
      ],
    },
    {
      id: "DelChat",
      icon: ShareChatIcon,
      text: "Del chat...",
      method: test,
    },
    {
      id: "Hjelp",
      icon: HelpIcon,
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
