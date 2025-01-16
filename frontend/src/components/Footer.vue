<template>
  
  <footer id="Fotter" class="footer is-fixed-bottom">
    <hr class="divider"/>

    <div class="level">

      <div class="level-left">
        <div class="level-item">
          <div class="is-size-7 has-text-centered">
            <strong>"ЧИБГУрёнок"</strong> © 2025. Все права защищены.
          </div>
        </div>
      </div>

      <div class="level-right">
        <div class="level-item buttons">

          <a class="button" href="https://bgu-chita.ru/" target="_blank" rel="noopener noreferrer">
            <span class="icon is-small">
              <i class="fa-solid fa-building-columns fa-2x"></i>
            </span>
          </a>

          <a class="button" href="https://vk.com/bguchita?ysclid=m5y5efnnte162940526" target="_blank" rel="noopener noreferrer">
            <span class="icon is-small">
              <i class="fa-brands fa-vk fa-2x"></i>
            </span>
          </a>

          <a class="button" href="https://t.me/s/bguchita/1230" target="_blank" rel="noopener noreferrer">
            <span class="icon is-small">
              <i class="fa-brands fa-telegram fa-2x"></i>
            </span>
          </a>

        </div>
      </div>

    </div>
  </footer>
  
</template>

<style>
  .footer.is-fixed-bottom {
    --bulma-footer-padding: 1rem;
    position: fixed;
    right: 0;
    left: 0;
    bottom: 0%;
  }

  .divider {
    background-color: hsla(221,14%,29%,1);
    border: none;
    display: block;
    height: 1px;
    margin: 1.0rem 0;
  }
</style>
