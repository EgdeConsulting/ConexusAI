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
  import * as ButtonMethods from "$lib/components/navbar/buttonMethods";
  import { onMount, onDestroy } from "svelte";

  function test() {
    alert("test method");
  }

  let buttons = [
    {
      id: "LagGraf",
      icon: Graph,
      text: "Lag graf...",
      subButtons: [
        {
          text: "Linjediagram",
          method: ButtonMethods.lineChartGraph,
          icon: LineChart,
        },
        {
          text: "Søylediagram",
          method: ButtonMethods.barChartGraph,
          icon: BarChart,
        },
        {
          text: "Kakediagram",
          method: ButtonMethods.pieChartGraph,
          icon: PieChart,
        },
      ],
    },
    {
      id: "download",
      icon: DownloadIcon,
      text: "Download",
      subButtons: [
        {
          text: "Download as PDF",
          method: ButtonMethods.downloadPDF,
          icon: DownloadAsPDF,
        },
        {
          text: "Download as Excel",
          method: ButtonMethods.downloadExcel,
          icon: DownloadAsExcel,
        },
      ],
    },
    {
      id: "send",
      icon: SendIcon,
      text: "Send",
      subButtons: [
        { text: "Send as PDF", method: ButtonMethods.sendPDF, icon: DownloadAsPDF },
        { text: "Send as Excel", method: ButtonMethods.sendExcel, icon: DownloadAsExcel },
      ],
    },
    {
      id: "DelChat",
      icon: ShareChatIcon,
      text: "Del chat...",
      method: ButtonMethods.shareChat,
    },
    {
      id: "Hjelp",
      icon: HelpIcon,
      text: "hjelp...",
      method: ButtonMethods.helpButtonMethod,
    },
  ];
  let showNavbar = true;

  onMount(() => {
    window.addEventListener("resize", () => {
      showNavbar = window.innerWidth < window.screen.width * 0.5 ? false : true;
    });
  });
</script>

<div class="main-container">
  {#if showNavbar}
    <section class="navbar-container">
      <NavbarSet {buttons} {showNavbar} />
    </section>
  {/if}
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
