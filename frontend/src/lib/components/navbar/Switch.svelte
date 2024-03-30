<script>
  export let checked = false;
  let color = "ADBDCE";
</script>

<label class="switch">
  <input type="checkbox" bind:checked />
  <span class="slider"></span>
</label>

<style>
  .switch {
    position: relative;
    display: inline-block;
    width: 30px; /* Redusert fra 60px til 40px */
    height: 15px; /* Redusert fra 34px til 22px */
  }

  .switch input {
    opacity: 0;
    width: 0;
    height: 0;
  }

  .slider {
    position: absolute;
    cursor: pointer;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-color: #ccc;
    -webkit-transition: 0.4s;
    transition: 0.4s;
    border-radius: 15px; /* Oppdatert for å matche høyden */
  }

  .slider:before {
    position: absolute;
    content: "";
    height: 10px; /* Redusert fra 26px til 18px */
    width: 10px; /* Redusert fra 26px til 18px */
    left: 4px; /* Justert for mindre størrelse */
    bottom: 2px; /* Justert for mindre størrelse */
    background-color: #00244e;
    -webkit-transition: 0.4s;
    transition: 0.4s;
    border-radius: 50%;
  }

  input:checked + .slider {
    background-color: #2196f3;
  }

  input:checked + .slider:before {
    -webkit-transform: translateX(15px); /* Justert for mindre størrelse */
    -ms-transform: translateX(15px); /* Justert for mindre størrelse */
    transform: translateX(15px); /* Justert for mindre størrelse */
  }
</style>
