<template>
  <div class="notification-container">
    <header data-role="Accordion" class="notification-header">
      <span class="notification-text">
        <span>Chat Forum</span>
        <br />
      </span>
      <div class="notification-separator"></div>
      <nav class="notification-nav"></nav>
      <app-notificationhead
        rootClassName="notificationhead-root-class-name"
      ></app-notificationhead>
      <div data-type="AccordionHeader" class="notification-accordion-header">
        <svg viewBox="0 0 1024 1024" class="notification-icon">
          <path
            d="M128 554.667h768c23.552 0 42.667-19.115 42.667-42.667s-19.115-42.667-42.667-42.667h-768c-23.552 0-42.667 19.115-42.667 42.667s19.115 42.667 42.667 42.667zM128 298.667h768c23.552 0 42.667-19.115 42.667-42.667s-19.115-42.667-42.667-42.667h-768c-23.552 0-42.667 19.115-42.667 42.667s19.115 42.667 42.667 42.667zM128 810.667h768c23.552 0 42.667-19.115 42.667-42.667s-19.115-42.667-42.667-42.667h-768c-23.552 0-42.667 19.115-42.667 42.667s19.115 42.667 42.667 42.667z"
          ></path>
        </svg>
      </div>
      <div data-type="AccordionContent" class="notification-accordion-content">
        <div class="notification-nav1">
          <app-homehead rootClassName="homehead-root-class-name21"></app-homehead>
        </div>
      </div>
    </header>
    <notification-message
      rootClassName="notification-message-root-class-name"
    ></notification-message>
    <notification-message
      rootClassName="notification-message-root-class-name1"
    ></notification-message>
    <notification-message
      rootClassName="notification-message-root-class-name2"
    ></notification-message>
  </div>
</template>

<script>
import AppNotificationhead from '../components/notificationhead'
import AppHomehead from '../components/homehead'
import NotificationMessage from '../components/notification-message'

export default {
  name: 'Notification',
  components: {
    AppNotificationhead,
    AppHomehead,
    NotificationMessage,
  },
  metaInfo: {
    title: 'Notification - Chat Forum',
    meta: [
      {
        property: 'og:title',
        content: 'Notification - Chat Forum',
      },
    ],
  },
}
</script>

<style scoped>
.notification-container {
  width: 100%;
  display: flex;
  overflow: auto;
  min-height: 100vh;
  align-items: center;
  flex-direction: column;
  justify-content: flex-start;
}
.notification-header {
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
.notification-text {
  font-style: normal;
  font-weight: 500;
}
.notification-separator {
  width: 100%;
  height: 1px;
  margin-top: var(--dl-space-space-oneandhalfunits);
  margin-bottom: var(--dl-space-space-oneandhalfunits);
}
.notification-nav {
  border: 2px dashed rgba(120, 120, 120, 0.4);
}
.notification-accordion-header {
  display: flex;
  align-items: center;
  flex-direction: column;
}
.notification-icon {
  width: var(--dl-size-size-xsmall);
  height: var(--dl-size-size-xsmall);
  display: none;
}
.notification-accordion-content {
  display: flex;
  overflow: hidden;
  max-height: 0;
  transition: 0.3s ease-in-out;
  align-items: center;
  flex-direction: column;
}
.notification-nav1 {
  display: flex;
  align-items: center;
  flex-direction: column;
}
@media(max-width: 991px) {
  .notification-nav1 {
    padding-top: 16px;
  }
}
@media(max-width: 767px) {
  .notification-header {
    padding-left: var(--dl-space-space-twounits);
    padding-right: var(--dl-space-space-twounits);
  }
  .notification-separator {
    margin-top: var(--dl-space-space-oneandhalfunits);
    margin-bottom: var(--dl-space-space-oneandhalfunits);
  }
  .notification-nav {
    display: none;
  }
  .notification-icon {
    width: var(--dl-size-size-small);
    height: var(--dl-size-size-small);
    display: flex;
  }
}
@media(max-width: 479px) {
  .notification-header {
    padding: var(--dl-space-space-unit);
  }
  .notification-separator {
    margin-top: var(--dl-space-space-unit);
    margin-bottom: var(--dl-space-space-unit);
  }
  .notification-icon {
    width: var(--dl-size-size-small);
    height: var(--dl-size-size-small);
  }
}
</style>
