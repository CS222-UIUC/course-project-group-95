<template>
  <div class="profile-container">
    <header data-role="Accordion" class="profile-header">
      <span class="profile-text">
        <span>Chat Forum</span>
        <br />
      </span>
      <div class="profile-separator"></div>
      <nav class="profile-nav"></nav>
      <div data-type="AccordionHeader" class="profile-accordion-header">
        <svg viewBox="0 0 1024 1024" class="profile-icon">
          <path
            d="M128 554.667h768c23.552 0 42.667-19.115 42.667-42.667s-19.115-42.667-42.667-42.667h-768c-23.552 0-42.667 19.115-42.667 42.667s19.115 42.667 42.667 42.667zM128 298.667h768c23.552 0 42.667-19.115 42.667-42.667s-19.115-42.667-42.667-42.667h-768c-23.552 0-42.667 19.115-42.667 42.667s19.115 42.667 42.667 42.667zM128 810.667h768c23.552 0 42.667-19.115 42.667-42.667s-19.115-42.667-42.667-42.667h-768c-23.552 0-42.667 19.115-42.667 42.667s19.115 42.667 42.667 42.667z"
          ></path>
        </svg>
      </div>
      <app-profilehead
        rootClassName="profilehead-root-class-name"
      ></app-profilehead>
      <div data-type="AccordionContent" class="profile-accordion-content">
        <div class="profile-nav1">
          <app-homehead rootClassName="homehead-root-class-name23"></app-homehead>
        </div>
      </div>
    </header>
    <profilebasic-information
      rootClassName="profilebasic-information-root-class-name"
    ></profilebasic-information>
    <app-profilepost
      rootClassName="profilepost-root-class-name"
    ></app-profilepost>
    <app-profilepost
      rootClassName="profilepost-root-class-name1"
    ></app-profilepost>
    <app-profilepost
      rootClassName="profilepost-root-class-name2"
    ></app-profilepost>
  </div>
</template>

<script>
import AppProfilehead from '../components/profilehead'
import AppHomehead from '../components/homehead'
import ProfilebasicInformation from '../components/profilebasic-information'
import AppProfilepost from '../components/profilepost'

export default {
  name: 'Profile',
  components: {
    AppProfilehead,
    AppHomehead,
    ProfilebasicInformation,
    AppProfilepost,
  },
  metaInfo: {
    title: 'Profile - Chat Forum',
    meta: [
      {
        property: 'og:title',
        content: 'Profile - Chat Forum',
      },
    ],
  },
}
</script>

<style scoped>
.profile-container {
  width: 100%;
  display: flex;
  overflow: auto;
  min-height: 100vh;
  align-items: center;
  flex-direction: column;
  justify-content: flex-start;
}
.profile-header {
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
.profile-text {
  font-style: normal;
  font-weight: 500;
}
.profile-separator {
  width: 100%;
  height: 1px;
  margin-top: var(--dl-space-space-oneandhalfunits);
  margin-bottom: var(--dl-space-space-oneandhalfunits);
}
.profile-nav {
  border: 2px dashed rgba(120, 120, 120, 0.4);
}
.profile-accordion-header {
  display: flex;
  align-items: center;
  flex-direction: column;
}
.profile-icon {
  width: var(--dl-size-size-xsmall);
  height: var(--dl-size-size-xsmall);
  display: none;
}
.profile-accordion-content {
  display: flex;
  overflow: hidden;
  max-height: 0;
  transition: 0.3s ease-in-out;
  align-items: center;
  flex-direction: column;
}
.profile-nav1 {
  display: flex;
  align-items: center;
  flex-direction: column;
}
@media(max-width: 991px) {
  .profile-nav1 {
    padding-top: 16px;
  }
}
@media(max-width: 767px) {
  .profile-header {
    padding-left: var(--dl-space-space-twounits);
    padding-right: var(--dl-space-space-twounits);
  }
  .profile-separator {
    margin-top: var(--dl-space-space-oneandhalfunits);
    margin-bottom: var(--dl-space-space-oneandhalfunits);
  }
  .profile-nav {
    display: none;
  }
  .profile-icon {
    width: var(--dl-size-size-small);
    height: var(--dl-size-size-small);
    display: flex;
  }
}
@media(max-width: 479px) {
  .profile-header {
    padding: var(--dl-space-space-unit);
  }
  .profile-separator {
    margin-top: var(--dl-space-space-unit);
    margin-bottom: var(--dl-space-space-unit);
  }
  .profile-icon {
    width: var(--dl-size-size-small);
    height: var(--dl-size-size-small);
  }
}
</style>
