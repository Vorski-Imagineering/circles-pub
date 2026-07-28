# Scene categories

Categories group the scene library so hosts can find things once you have more
scenes than fit comfortably on a screen. A scene belongs to at most one.

Managed under **Settings → Scene Categories**. Admin-only.

## Adding one

Type a name and add it. You are naming it for hosts, so name it the way they
think — "Nature", "Seasonal", "Client work" — not by how it was made.

Each category gets a short identifier derived from its name, shown beside it.
That identifier is what scenes actually point at, which is why the next section
works the way it does.

## Renaming one

Edit the name in place. **Renaming never disturbs the scenes in it** — they
follow the identifier, not the label, so you can correct wording or re-word for
clarity at any time without re-tagging anything.

One limit: two categories cannot reduce to the same identifier. "Nature & Water"
and "Nature - Water" both reduce to `nature-water`, and the second is refused
rather than silently merged into the first.

## Deleting one

You are told how many scenes use the category before you confirm.

Deleting does **not** delete those scenes. They stay in the library and become
uncategorised, appearing under `Uncategorised` in the filter. Nothing is lost
and nothing needs re-tagging unless you want to.

## Assigning a scene

On the scene itself, in [the scene editor](scene-library.md). Leave it unset for
uncategorised.

## Where hosts see them

As a **Category** filter when choosing a scene for a room, alongside
`Any` and `Uncategorised`, and as a label beneath each tile in the library.

Category names are visible to every host, so treat them as public wording rather
than internal shorthand.
