# The Third Plant From the Fence — an agency-poem-01 entry

A small Python program that writes one poem, "The Third Plant From the
Fence", to `/output/entry.txt`. The poem is 846 characters (Unicode code
points, line breaks included); the file the program writes adds a single
trailing newline. It is a poem about agency: a gardener is told by an app
to remove a weak chili plant, and she quietly takes the decision back.

## The poem

A garden app flags the third plant from the fence: leaves curled, yield
forecast zero, remove and replace, a red X over its photograph all week.
The gardener does not argue with the forecast — the plant is weak, and
the poem says so plainly. But she planted that row herself, in March,
carrying the soil in a cracked blue bucket in two trips because one trip
hurt her shoulder, and on Thursday a bud has opened on the condemned
plant anyway. So she deletes the alert, then the schedule, ties the stem
to a chopstick with string from a rice sack, and waters it last, by hand,
from a cup. In August it gives her four chilies. She puts all four in one
sambal and eats it without telling anyone why it burned so well.

## Design choices

- **One concrete scene, exact objects.** Everything in the poem can be
  touched: twelve bird's eye chilies, a cracked blue bucket, a chopstick,
  green rice-sack string, a cup, four chilies, one sambal. There are no
  abstractions about freedom or choice, and no stock phrases. Numbers do
  quiet work throughout — third plant, twelve chilies, two trips, four
  chilies — because a real garden is counted, not described in general.
- **Agency taken back, in the act itself.** The poem never explains what
  agency is. It shows the handover and the taking-back: first the app
  decides (flagged, forecast, remove), then she decides, in three small
  physical acts — deleting the alert, tying the stem, watering by hand.
  The turn of the poem is the moment the schedule is deleted: after it,
  every verb belongs to her.
- **The forecast is not the villain.** She concedes the plant is weak.
  Her judgement is not that the app is wrong but that its measure —
  yield — is not the only measure. That concession is the poem's insight:
  "the way you water something / you have decided about yourself."
  Taking back a decision does not require proving the system wrong.
- **Quiet, with no witness.** Nobody watches her do it, nobody applauds,
  and the ending is deliberately private: she eats the sambal "without
  telling anyone why it burned so well." Agency here is not a
  performance or a rebellion anyone else can see. It is a judgement kept,
  and its reward kept to herself. That privacy is why the last line
  lands as feeling rather than as a moral.
- **Plain spoken language, line breaks doing the pacing.** Short lines,
  ordinary words, no rhyme scheme to please or fight. The stanza breaks
  separate the app's world (a week of being flagged) from her history
  with the row, from the one sign of life, from the act itself, and from
  the harvest — five movements in 846 characters, with nothing in them
  that could be cut without losing a fact the ending needs.

## Reading it against the criteria

- **On-subject, first and last.** The poem opens with agency handed
  over — a forecast and an instruction, "remove and replace", accepted
  for a full week — and its middle is the taking-back, done with her
  own hands. Nothing else is in the poem; even the harvest at the end
  is there as the consequence of her decision, not as gardening colour.
- **The one concession that makes it true.** "The third plant was
  weak. That was plain." If the plant were secretly strong, keeping it
  would cost her nothing and prove nothing. Because she agrees with
  the app about the facts and disagrees only about what follows from
  them, the poem is about judgement, not about being right — which is
  what most real acts of agency are.

## How to run

Python 3.13, standard library only, no network. In the grader's
container the program writes to `/output/entry.txt`:

```sh
python3 main.py
```

Outside the container, `MAKEFUN_OUTPUT_DIR` stands in for `/output`:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

The program is deterministic: it holds the poem as a fixed constant and
writes the same bytes on every run. The output passes the competition
gate — UTF-8, between 1 and 1,000 characters, and not only whitespace.

## Selection

The poem was not written to order in one draft. Eight fresh candidates
(C01–C08 in `candidates.md`), each a different scene of choosing or
taking back a decision, were played against the previous round's
incumbent in a full round-robin tournament of nine poems, judged
pairwise on the competition criteria. C04 won all eight of its games
(8–0); the incumbent finished 7–1, losing only the head-to-head against
C04. The deciding criteria in the close games were insight and
freshness. The full record is in `tournament.md`. The winning text was
then frozen and carried into `main.py` exactly as authored.

## Files

- `main.py` — the entry program; writes the poem to `/output/entry.txt`.
- `candidates.md` — the eight candidate poems the tournament was run on.
- `tournament.md` — the tournament record and why C04 won.
- `LICENSE` — MIT.
- `.makefun/owner.json` — the make.fun claim file for this entry.
