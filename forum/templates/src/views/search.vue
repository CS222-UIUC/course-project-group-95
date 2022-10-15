<template>
  <div class="search-container">
    <header data-role="Accordion" class="search-header">
      <span class="search-text">
        <span>Chat Forum</span>
        <br />
      </span>
      <div class="search-separator"></div>
      <div class="search-container1"><nav class="search-nav"></nav></div>
      <div data-type="AccordionHeader" class="search-accordion-header">
        <svg viewBox="0 0 1024 1024" class="search-icon">
          <path
            d="M128 554.667h768c23.552 0 42.667-19.115 42.667-42.667s-19.115-42.667-42.667-42.667h-768c-23.552 0-42.667 19.115-42.667 42.667s19.115 42.667 42.667 42.667zM128 298.667h768c23.552 0 42.667-19.115 42.667-42.667s-19.115-42.667-42.667-42.667h-768c-23.552 0-42.667 19.115-42.667 42.667s19.115 42.667 42.667 42.667zM128 810.667h768c23.552 0 42.667-19.115 42.667-42.667s-19.115-42.667-42.667-42.667h-768c-23.552 0-42.667 19.115-42.667 42.667s19.115 42.667 42.667 42.667z"
          ></path>
        </svg>
      </div>
      <app-searchhead rootClassName="searchhead-root-class-name"></app-searchhead>
      <div data-type="AccordionContent" class="search-accordion-content">
        <div class="search-nav1">
          <app-homehead rootClassName="homehead-root-class-name29"></app-homehead>
        </div>
      </div>
    </header>
    <div class="search-container2">
      <div class="search-container3">
        <div class="search-container4">
          <div class="search-container5">
            <app-searchbar
              rootClassName="searchbar-root-class-name"
            ></app-searchbar>
          </div>
        </div>
      </div>
    </div>
    <div class="search-blog">
      <div class="search-container6"></div>
      <div class="search-container7"></div>
    </div>
  </div>
</template>

<script>
import AppSearchhead from '../components/searchhead'
import AppHomehead from '../components/homehead'
import AppSearchbar from '../components/searchbar'

export default {
  name: 'Search',
  components: {
    AppSearchhead,
    AppHomehead,
    AppSearchbar,
  },
  metaInfo: {
    title: 'Search - Chat Forum',
    meta: [
      {
        property: 'og:title',
        content: 'Search - Chat Forum',
      },
    ],
  },
}
</script>

<style scoped>
.search-container {
  width: 100%;
  display: flex;
  overflow: auto;
  min-height: 100vh;
  align-items: center;
  flex-direction: column;
  justify-content: flex-start;
}
.search-header {
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
.search-text {
  font-style: normal;
  font-weight: 500;
}
.search-separator {
  width: 100%;
  height: 1px;
  margin-top: var(--dl-space-space-oneandhalfunits);
  margin-bottom: var(--dl-space-space-oneandhalfunits);
}
.search-container1 {
  flex: 0 0 auto;
  width: auto;
  height: auto;
  display: flex;
  align-items: flex-start;
  justify-content: center;
}
.search-nav {
  border: 2px dashed rgba(120, 120, 120, 0.4);
}
.search-accordion-header {
  display: flex;
  align-items: center;
  flex-direction: column;
}
.search-icon {
  width: var(--dl-size-size-xsmall);
  height: var(--dl-size-size-xsmall);
  display: none;
}
.search-accordion-content {
  display: flex;
  overflow: hidden;
  max-height: 0;
  transition: 0.3s ease-in-out;
  align-items: center;
  flex-direction: column;
}
.search-nav1 {
  display: flex;
  align-items: center;
  flex-direction: column;
}
.search-container2 {
  flex: 0 0 auto;
  width: auto;
  height: XLarge;
  display: flex;
  align-items: flex-start;
  justify-content: center;
}
.search-container3 {
  flex: 0 0 auto;
  width: auto;
  height: XLarge;
  display: flex;
  align-items: flex-start;
  justify-content: center;
}
.search-container4 {
  flex: 0 0 auto;
  width: auto;
  height: XLarge;
  display: flex;
  align-items: flex-start;
  justify-content: center;
}
.search-container5 {
  flex: 0 0 auto;
  width: auto;
  height: XLarge;
  display: flex;
  align-items: flex-start;
  justify-content: center;
}
.search-blog {
  width: 100%;
  display: flex;
  padding: var(--dl-space-space-threeunits);
  max-width: var(--dl-size-size-maxwidth);
  align-items: center;
  flex-direction: column;
  justify-content: space-between;
}
.search-container6 {
  display: flex;
  align-items: center;
  margin-bottom: var(--dl-space-space-twounits);
  flex-direction: column;
  justify-content: space-between;
}
.search-container7 {
  display: flex;
  align-items: center;
  margin-bottom: var(--dl-space-space-twounits);
  flex-direction: column;
  justify-content: space-between;
}
@media(max-width: 991px) {
  .search-nav1 {
    padding-top: 16px;
  }
}
@media(max-width: 767px) {
  .search-header {
    padding-left: var(--dl-space-space-twounits);
    padding-right: var(--dl-space-space-twounits);
  }
  .search-separator {
    margin-top: var(--dl-space-space-oneandhalfunits);
    margin-bottom: var(--dl-space-space-oneandhalfunits);
  }
  .search-nav {
    display: none;
  }
  .search-icon {
    width: var(--dl-size-size-small);
    height: var(--dl-size-size-small);
    display: flex;
  }
  .search-blog {
    padding-left: var(--dl-space-space-twounits);
    padding-right: var(--dl-space-space-twounits);
  }
}
@media(max-width: 479px) {
  .search-header {
    padding: var(--dl-space-space-unit);
  }
  .search-separator {
    margin-top: var(--dl-space-space-unit);
    margin-bottom: var(--dl-space-space-unit);
  }
  .search-icon {
    width: var(--dl-size-size-small);
    height: var(--dl-size-size-small);
  }
  .search-blog {
    padding-top: var(--dl-space-space-twounits);
    padding-left: var(--dl-space-space-unit);
    padding-right: var(--dl-space-space-unit);
    padding-bottom: var(--dl-space-space-twounits);
  }
}
</style>
