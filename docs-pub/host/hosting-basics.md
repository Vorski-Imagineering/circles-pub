# Hosting basics

A host owns rooms: they create them, choose how they look and behave, and have
moderation controls inside them.

Everything in [the circle docs](../circle) applies to you as well — a host in a
circle is a participant with extra buttons, not a different kind of user.

## Becoming a host

An admin invites you. See [People and access](../admin/people-and-access.md).

## Getting into your room

Two ways in, and they behave differently:

- **Signed in, no key** — open `/<room-name>`. You arrive as the host, with host
  controls.
- **Through a participant link** (with `?key=`) — you arrive as an ordinary
  participant, even though you are the host. The menu then offers **Go Host
  Mode**, which drops the key from the URL and reloads you in as host.

This is useful deliberately: you can see exactly what your participants see.

## The room menu

Everyone gets **Settings** (back to the device screen) and the bug report link.
As host you also get:

- **Join URL** — copies the participant link. See
  [Inviting people](inviting-people.md).
- **Room Admin** — opens that room's settings page in a new tab.
- **Round Mode** — start or stop a round. See
  [Running a round](running-a-round.md).
- **The End** — finishes the circle for everyone. See
  [Ending a circle](ending-a-circle.md).

## Removing someone

Hover over a participant's circle and a kick control appears. It removes that
person from the circle. They are not banned — the join link still works — so
this is for accidents and disruption, not permanent exclusion.

## What you cannot do

- **You cannot turn a participant's camera off**, and neither can they. Circles
  is a cameras-on space.
- **There is no "mute all" button.** The capability exists in the system but is
  not currently exposed in the menu. Muting is otherwise automatic — see
  [Sound and camera](../circle/sound-and-camera.md).
