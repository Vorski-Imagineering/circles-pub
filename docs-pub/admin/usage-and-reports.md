# Usage and reports

**Usage** in the sidebar. Admin-only, and covers the whole site. Hosts get a
**Stats** entry showing only their own rooms.

Every tab has a **Day / Week / Month** period selector at the top; it applies to
whichever tab you are on.

## Overview

The headline numbers for the period:

| Figure | Means |
|---|---|
| **Sessions** | How many circles were held |
| **Duration** | Total time across them |
| **Active rooms** | Rooms that were actually used, not rooms that exist |
| **Active hosts** | Hosts who actually ran something |
| **Peak concurrent** | The busiest simultaneous moment |
| **Unique participants (est.)** | Roughly how many different people took part |

Participant counts are an **estimate** and labelled as one. Participants have no
accounts, so the figure is inferred rather than counted — good for trends,
wrong for anything that needs to be exact.

## Rooms

Every room used in the period, with its host, session count and duration.
Searchable by room or meeting ID — use it to answer "how much is this group
actually meeting?"

## Hosts

The same, grouped by host: who is running circles and how much. Useful for
spotting both the people carrying the load and the accounts that have gone quiet.

## Reports

Generated summaries for a period, and snapshots of the underlying data. Use
these when the numbers need to leave the admin area — a funder update, a board
paper, an invoice.

Reports are generated on request and kept, so a report of last month reads the
same today as it did when you made it.

## Sync health

Usage figures come from reconciling the video provider's records against our own
rooms. This tab shows whether that reconciliation is working: when it last ran,
whether it succeeded, and anything it could not match.

Unmatched entries are usually a meeting whose title does not correspond to a
Firebase room. A few are unremarkable; a growing pile means the numbers on the
other tabs are drifting from reality and want investigating before you rely on
them.

You can re-run the sync for a chosen start and end date if something looks wrong
or a period needs rebuilding.

## What is not here

There is no per-participant tracking, no attendance list, and no record of who
said what. Circles does not identify participants, so usage reporting is about
volume rather than people.
