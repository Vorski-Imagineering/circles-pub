# Circles user documentation

These are the docs for people who *use* Circles. Anything about building,
deploying or testing it lives in [`docs/dev`](../dev).

## Who each section is for

| Section | Audience | Scope |
|---|---|---|
| [`circle/`](circle) | Anyone in a circle | Being in a room: joining, seeing, speaking, reacting |
| [`host/`](host) | Hosts | Creating and running rooms |
| [`admin/`](admin) | Site admins | People, scenes, branding, usage |

## The one rule for writing these

**Every capability is described exactly once.** Its home is wherever it is
*performed or configured*, not wherever it is felt:

- A host is also a participant, so everything in `circle/` already applies to
  them and is never restated in `host/`.
- An admin who hosts a circle reads `host/` for that, not a second copy inside
  `admin/`.

Where a topic spans sections, link to the single description instead of
repeating it. `host/running-a-round.md` covers starting and stopping a round;
what a round *feels like* to take part in is `circle/rounds.md`, linked, not
copied.

If you find yourself explaining something twice, one of the two is in the wrong
place.

## Contents

### `circle/` — for everyone in a circle

- [Joining a circle](circle/joining-a-circle.md) — the link, the entry screen,
  choosing devices, and the cameras-on rule
- [What you are looking at](circle/the-circle.md) — the circles, the centre,
  the scene, and when people appear
- [Speaking and the centre](circle/speaking-and-the-centre.md) — taking the
  centre, the talking stick, the three layouts
- [Sound and camera](circle/sound-and-camera.md) — muting, the temporary
  unmute window, losing your camera
- [Rounds](circle/rounds.md) — taking part in a round
- [Reactions](circle/reactions.md) — the heart
- [When something goes wrong](circle/when-something-goes-wrong.md) —
  connection trouble, frozen video, getting back in

### `host/` — for hosts

- [Hosting basics](host/hosting-basics.md) — what a host is, host mode, the
  room menu
- [Creating a room](host/creating-a-room.md) — the room settings
- [Choosing a scene](host/choosing-a-scene.md) — picking, searching, filtering
- [Personalising a room](host/personalising-a-room.md) — room-specific media
- [Inviting people](host/inviting-people.md) — the join URL and room keys
- [Running a round](host/running-a-round.md) — starting, timing, aborting
- [Ending a circle](host/ending-a-circle.md) — The End, and the goodbye URL
- [Your host profile](host/your-host-profile.md) — name, photo, host logo

### `admin/` — for site admins

- [Admin overview](admin/admin-overview.md) — the admin area and what is
  admin-only
- [People and access](admin/people-and-access.md) — users, invites, roles
- [Scene library](admin/scene-library.md) — what a scene is, creating and
  editing one
- [Scene categories](admin/scene-categories.md) — grouping the library
- [Rooms administration](admin/rooms-administration.md) — every room, across
  every host
- [Branding and settings](admin/branding-and-settings.md) — logos, colours,
  welcome copy
- [Usage and reports](admin/usage-and-reports.md) — overview, rooms, hosts,
  reports, sync health
