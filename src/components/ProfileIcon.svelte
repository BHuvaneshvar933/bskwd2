<script>
  let userImageUrl = 'path_to_user_image.jpg'; // Replace with actual image path or URL
</script>

<style>
  .circle {
    width: 10rem;
    height: 10rem;
    border-radius: 50%;
    overflow: hidden;
    /* position: absolute;
    top: 20px;
    right: 20px; */
    background-color: #D9D9D9;
  }
  .circle img {
    width: 100%;
    height: 100%;
    object-fit: cover; /* Ensures the image fits within the circle */
  }
</style>

<div class="circle">
  <!-- <img src={userImageUrl} alt="User Image" /> -->
</div>
