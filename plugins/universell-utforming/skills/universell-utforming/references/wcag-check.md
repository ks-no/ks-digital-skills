# WCAG 2.1 check of interface code

Read this file for a check of a full page or flow, or when the user asks for a full
WCAG check. It lists the 50 success criteria of WCAG 2.1 at level A and AA, by number,
with what to look for in code. The text is a paraphrase, not the text of WCAG. Read
the criterion at w3.org/TR/WCAG21 when you are not sure what it requires.

- Public bodies in Norway must meet 48 of these criteria: all except 1.2.3 and 1.2.4.
  1.2.5 applies to recorded video published on 1 February 2024 or later.
- Other businesses must meet 35 criteria from WCAG 2.0: the criteria not marked "2.1",
  without 1.2.3, 1.2.4 and 1.2.5.
- The criteria marked "2.1" are the twelve that WCAG 2.1 adds.
- Check against the list for public bodies, unless the user says that a smaller set
  applies. The rules change, so tell the user that uutilsynet.no has the current list.

A check of the code cannot show all of these. Give the criteria that need a person, a
browser or the real content in one line at the end, and do not report them as met.

## Text alternatives and media

- 1.1.1: each image, icon and control that gives information has a text alternative.
  A decorative image has an empty `alt` or is hidden from assistive technology.
- 1.2.1: recorded audio only has a text alternative, such as a transcript. Recorded
  video only has a text alternative or an audio track.
- 1.2.2: recorded video with sound has captions.
- 1.2.3: recorded video has audio description or a text alternative. Not required in
  Norway.
- 1.2.4: live video with sound has captions. Not required in Norway.
- 1.2.5: recorded video has audio description. Required only for public bodies, for
  video published on 1 February 2024 or later.

## Structure and meaning

- 1.3.1: headings, lists, tables, labels and groups that the screen shows are also in
  the markup. A table for data has header cells. No criterion requires landmarks.
- 1.3.2: the order in the code gives the same meaning as the order on the screen.
- 1.3.3: an instruction does not depend only on shape, size, place or sound.
- 1.3.4 (2.1): the content works in both portrait and landscape.
- 1.3.5 (2.1): a field for personal data about the person who fills in the form has
  the correct `autocomplete` value.

## Colour, contrast and layout

- 1.4.1: colour is not the only way to give information, such as an error or a link in
  text.
- 1.4.2: sound that plays by itself for more than 3 seconds can be stopped.
- 1.4.3: text has a contrast of at least 4.5:1, and large text at least 3:1. Disabled
  controls and logos are exempt.
- 1.4.4: text can be enlarged to 200 % without loss of content or function. The
  viewport does not block zoom.
- 1.4.5: text is text, not an image of text, where text is possible.
- 1.4.10 (2.1): the content works at 320 CSS pixels width (400 % zoom) without scroll
  in two directions. Content that needs two dimensions, such as a data table or a map,
  can scroll.
- 1.4.11 (2.1): the parts that are needed to identify a control and its state, focus
  indicators and graphics that give information have a contrast of at least 3:1 to the
  colours next to them. A control that its text identifies needs no border or fill with
  3:1. Disabled controls are exempt, and so is a focus style from the browser that the
  author did not change.
- 1.4.12 (2.1): content stays readable when the user sets line height to 1.5 times the
  font size, paragraph spacing to 2 times, letter spacing to 0.12 em and word spacing
  to 0.16 em. Look for a fixed height on a text container.
- 1.4.13 (2.1): content that shows on hover or focus can be closed without a move of
  the pointer or the focus (usually with Esc), the pointer can move onto it, and it
  stays until the user moves away or closes it. A close button alone does not meet it.

## Keyboard and time

- 2.1.1: each function works with the keyboard.
- 2.1.2: the focus does not get stuck in a part of the page.
- 2.1.4 (2.1): a shortcut with one character can be turned off or changed, or works
  only when its control has focus.
- 2.2.1: the user can turn off, adjust or extend each time limit.
- 2.2.2: content that moves, blinks or scrolls by itself, lasts more than 5 seconds
  and shows together with other content, can be paused, stopped or hidden. The same
  applies to content that updates by itself.
- 2.3.1: nothing flashes more than three times in one second.

## Navigation and focus

- 2.4.1: the user can skip blocks that repeat, such as a header or a menu.
- 2.4.2: each page has a title that tells its topic or purpose.
- 2.4.3: the focus moves in an order that keeps the meaning and the operation.
- 2.4.4: the purpose of each link is clear from its text, or from its text and its
  context.
- 2.4.5: there is more than one way to find a page in a set of pages, except a page
  that is a step in a process.
- 2.4.6: headings and labels tell the topic or purpose.
- 2.4.7: the keyboard focus is visible.

## Pointer and touch

- 2.5.1 (2.1): a function that uses a path or more than one finger also works with one
  pointer without a path.
- 2.5.2 (2.1): a function starts on the up event, or the user can stop or undo it.
- 2.5.3 (2.1): the accessible name of a control contains its visible text.
- 2.5.4 (2.1): a function that starts when the user moves the device also has a
  control, and can be turned off.

## Language and behaviour

- 3.1.1: the page has the correct language in `lang`.
- 3.1.2: a part in another language has its own `lang`.
- 3.2.1: focus on an element does not change the context, such as a new page.
- 3.2.2: a change of a value does not change the context, unless the user knows that
  it will.
- 3.2.3: navigation that repeats on several pages is in the same relative order on
  each page.
- 3.2.4: functions that are the same have the same name on each page.

## Forms and errors

- 3.3.1: the page tells the user which field has an error, and what the error is, in
  text.
- 3.3.2: each field has a label or an instruction. A placeholder that disappears when
  the user types is not a label.
- 3.3.3: an error message tells how to correct the error, when this is known.
- 3.3.4: for legal, financial or data changes, the user can check, correct or undo the
  input before it is final.

## Code for assistive technology

- 4.1.1: the regulation still lists it, but W3C now treats it as always met for HTML.
  Report an ID that is not unique and that a label or an ARIA attribute points to
  under 1.3.1 or 4.1.2.
- 4.1.2: each control has a name, a role, and a state or a value that assistive
  technology can read, and changes to them are announced.
- 4.1.3 (2.1): a status message is announced without a change of focus.
