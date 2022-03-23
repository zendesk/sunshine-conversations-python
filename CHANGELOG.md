# Changelog

## [9.6.0] - 2022-03-23

### Added

- Added `user:update` event. This event currently fires when an anonymous user is converted to an authenticated user.
- Added missing `reason` in the `user:merge` webhook payload example.

## [9.5.7] - 2022-01-04

- Added missing pageId and pageName properties on Messenger integration.

## [9.5.6] - 2021-11-30

- Dependencies security update; Python wrapper not affected.

## [9.4.6] - 2021-09-23

- Added channel linking events
- Added `canUserSeeConversationList` in the `web` integration
- Updated RESTeasy to the latest version

## [9.4.5] - 2021-08-23

- Added page[before|after|size] query parameter constraints.

## [9.4.4] - 2021-04-12

### Added

- Added `messagingServiceSid` field when creating a Twilio integration that will use Messaging Services.

## [9.4.3] - 2021-02-16

### Fixed

- Fixed: query `Page1` instead of `Page` being used in the v2 List Messages API
- Fixed: property `displayName` should not be `nullable` in v2 App Key API

## [9.4.2] - 2021-01-06

### Added

- Added `phoneNumber` to the `integration` whatsapp response
- Added a message type `template` in the Post Message API

### Changed

- Removed `channelId` and `channelSecret` as required fields when creating a LINE integration

### Fixed

- Fixed: property `messageSchema` should be `schema` in v2 Post Message API

## [9.4.1] - 2020-12-16

### Changed

- Changed the limit of the `select` field options from 20 to 100

## [9.4.0] - 2020-12-15

### Added

- Added a new user profile field `locale`

## [9.3.0] - 2020-11-18

### Added

- Added a new optional field `altText` to the [message schema](https://docs.smooch.io/rest/#operation/postMessage) when sending an image or a file

## [9.2.0] - 2020-11-16

### Added

- Added support for Instagram Direct

## [9.1.1] - 2020-11-11

### Fixed

- Fixed pypi upload issues

## [9.1.0] - 2020-11-11

### Added

- Release of Python wrappers
