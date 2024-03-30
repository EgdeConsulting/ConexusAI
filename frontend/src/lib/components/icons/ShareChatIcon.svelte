<script>
  export let color = "currentColor";
  export let height;
  export let width;
</script>

<svg
  width={width}
  height={height}
  viewBox="0 0 24 24"
  fill="none"
  xmlns="http://www.w3.org/2000/svg"
>
  <g clip-path="url(#clip0_15_72)">
    <rect width="24" height="24" fill="none" />
    <circle
      cx="7"
      cy="12"
      r="2"
      stroke={color}
      stroke-linejoin="round"
      stroke-width="2"
    />
    <circle
      cx="17"
      cy="6"
      r="2"
      stroke={color}
      stroke-linejoin="round"
      stroke-width="2"
    />
    <path d="M15 7L8.5 11" stroke={color}  stroke-width="2"/>
    <circle cx="17" cy="18" r="2" stroke={color} stroke-linejoin="round" stroke-width="2"/>
    <path d="M8.5 13.5L15 17" stroke={color}  stroke-width="2"/>
  </g>
  <defs>
    <clipPath id="clip0_15_72">
      <rect width="24" height="24" fill="white" />
    </clipPath>
  </defs>
</svg>
