<template>
  <div class="home-container">
    <header data-role="Accordion" class="home-header">
      <span class="home-text">
        <span>Chat Forum</span>
        <br />
      </span>
      <div class="home-separator"></div>
      <nav class="home-nav"></nav>
      <app-homehead rootClassName="homehead-root-class-name18"></app-homehead>
      <div data-type="AccordionHeader" class="home-accordion-header">
        <svg viewBox="0 0 1024 1024" class="home-icon">
          <path
            d="M128 554.667h768c23.552 0 42.667-19.115 42.667-42.667s-19.115-42.667-42.667-42.667h-768c-23.552 0-42.667 19.115-42.667 42.667s19.115 42.667 42.667 42.667zM128 298.667h768c23.552 0 42.667-19.115 42.667-42.667s-19.115-42.667-42.667-42.667h-768c-23.552 0-42.667 19.115-42.667 42.667s19.115 42.667 42.667 42.667zM128 810.667h768c23.552 0 42.667-19.115 42.667-42.667s-19.115-42.667-42.667-42.667h-768c-23.552 0-42.667 19.115-42.667 42.667s19.115 42.667 42.667 42.667z"
          ></path>
        </svg>
      </div>
      <div data-type="AccordionContent" class="home-accordion-content">
        <div class="home-nav1">
          <app-homehead rootClassName="rootClassName20"></app-homehead>
        </div>
      </div>
    </header>
    <home-post rootClassName="home-post-root-class-name"></home-post>
    <home-post rootClassName="home-post-root-class-name1"></home-post>
    <home-post rootClassName="home-post-root-class-name2"></home-post>
    <router-link to="/login" class="home-navlink">login</router-link>
  </div>
</template>

<script>
import AppHomehead from '../components/homehead'
import HomePost from '../components/home-post'

export default {
  name: 'Home',
  components: {
    AppHomehead,
    HomePost,
  },
  metaInfo: {
    title: 'Chat Forum',
    meta: [
      {
        property: 'og:title',
        content: 'Chat Forum',
      },
    ],
  },
}
</script>

<style scoped>
.home-container {
  width: 100%;
  display: flex;
  overflow: auto;
  min-height: 100vh;
  align-items: center;
  flex-direction: column;
  justify-content: flex-start;
}
.home-header {
  width: 100%;
  height: 204px;
  display: flex;
  position: relative;
  max-width: var(--dl-size-size-maxwidth);
  align-items: center;
  padding-top: var(--dl-space-space-twounits);
  padding-left: var(--dl-space-space-threeunits);
  padding-right: var(--dl-space-space-threeunits);
  flex-direction: column;
  padding-bottom: var(--dl-space-space-twounits);
  background-color: rgba(217, 217, 217, 0.55);
}
.home-text {
  font-style: normal;
  font-weight: 500;
}
.home-separator {
  width: 100%;
  height: 1px;
  margin-top: var(--dl-space-space-oneandhalfunits);
  margin-bottom: var(--dl-space-space-oneandhalfunits);
}
.home-nav {
  border: 2px dashed rgba(120, 120, 120, 0.4);
}
.home-accordion-header {
  display: flex;
  align-items: center;
  flex-direction: column;
}
.home-icon {
  width: var(--dl-size-size-xsmall);
  height: var(--dl-size-size-xsmall);
  display: none;
}
.home-accordion-content {
  display: flex;
  overflow: hidden;
  max-height: 0;
  transition: 0.3s ease-in-out;
  align-items: center;
  flex-direction: column;
}
.home-nav1 {
  display: flex;
  align-items: center;
  flex-direction: column;
}
.home-navlink {
  text-decoration: underline;
}
@media(max-width: 991px) {
  .home-nav1 {
    padding-top: 16px;
  }
}
@media(max-width: 767px) {
  .home-header {
    padding-left: var(--dl-space-space-twounits);
    padding-right: var(--dl-space-space-twounits);
  }
  .home-separator {
    margin-top: var(--dl-space-space-oneandhalfunits);
    margin-bottom: var(--dl-space-space-oneandhalfunits);
  }
  .home-nav {
    display: none;
  }
  .home-icon {
    width: var(--dl-size-size-small);
    height: var(--dl-size-size-small);
    display: flex;
  }
}
@media(max-width: 479px) {
  .home-header {
    padding: var(--dl-space-space-unit);
  }
  .home-separator {
    margin-top: var(--dl-space-space-unit);
    margin-bottom: var(--dl-space-space-unit);
  }
  .home-icon {
    width: var(--dl-size-size-small);
    height: var(--dl-size-size-small);
  }
}
</style>
