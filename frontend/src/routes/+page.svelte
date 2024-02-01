<script>
  import { ChatbotInterface, NavbarButtons, ShareChatIcon } from "$lib";

  function test() {
    alert("test method");
  }
  const NavbarButtonsArray = [
    { picture: ShareChatIcon, text: "hei", method: test },
  ];
</script>

<main
  style="display: flex; align-items: center; justify-content: center; height: 100vh;"
>
  <ChatbotInterface />
  <div>
    
    <NavbarButtons {NavbarButtonsArray} />
  </div>
</main>
