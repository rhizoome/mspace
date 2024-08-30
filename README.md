Music Space
===========

How it works
============

Find a QR Code in public space, scan it, listen to the music, download it.

Why
===

The internet is a shit place to put your hobby art out. You compete with
everyone on the planet, people will be mean to you, expectations are usually too
high. You are not a big record-label, you put yourself into your music and you
love some people experience it, maybe like it and download it.

At least that is my position and I was searching for a solution for years.

Planning
========

Phase 1
-------

There is a page per song, that shows:

* A cover
* A view counter
* A play-button, with a click counter
* Downloads (aac, opus, mp3, alac, flac), with a download counter
* A like-button, with a counter

The counters should give people a sense, that they are not alone in the space.
I'd want to add some more ways to give people a sense of commonality without
using comments [^1].

The QR Code "sticker" needs to have a design that allows people to recognize them
as `Music Space` instantly.

[^1]: I feel comments are one of the big evils on the internet.

Phase 2
-------

Show a map where other songs can be found in public space. Yes one QR Code gives
you access to one track only. To access more songs you need to play geo-caching.

* A feature to report missing QR Codes.

Maybe more.

Phase 3
-------

Give people a sense of commonality.

Brainstoming:

* Post images
  * Problem: abuse/spam
* Share lococation: I am currently standing beside that QR Code
  * Problem will happen too seldom
* Share location at a central metting point
  * There is one location for the whole `Music Space`
  * People can post that they are there

Currently I don't think I've found the right idea yet.

Features
--------

### Phase 1

* Uses [caddy](https://caddyserver.com/), [quat](https://gitlab.com/pgjones/quart)
  and [hypercorn](https://caddyserver.com/)
* The database is just a set of toml files
  * [aiofiles](https://www.twilio.com/blog/working-with-files-asynchronously-in-python-using-aiofiles-and-asyncio)
  * Lock the file (actually the path in lock-table)
* https://[site]/[ID] displays the track
* ID looks like this `wczj-tmqg`
* https://[site]/static gives access to images/downloads/streams
* CSS
  * Place track cover full-site blured in the background
  * Track cover, containing a play button
  * View count is top-right
  * Play count below the track cover
  * Download section below that
* Also add Dockerfiles, but docker-compose is delegated to the user

_

TODO
----

Lets start with Phase 1:

- [x] Host the site somewhere
- [x] Create poetry project
- [x] Add basic dependnecies
- [x] Design toml-file
- [x] Read toml
- [x] Display track (no CSS yet)
- [ ] Create config.toml??
- [x] Create a demo track
- [x] Create a CSS
- [ ] Adjust blur-background color/brightness via toml??
- [x] Early deploy
   - [x] Dockerfile
   - [ ] Update features/TODO according to problems encountered
     - [x] View only route (no count updates)
     - [x] Some basic error handling
     - [ ] Display soundcloud comments only if needed
     - [x] Configure access.log to file for statistics??
     - [x] Translate downloads into cover
     - [x] Move control down with 75vmin
     - [x] Remove unneeded z-indexs
     - [x] Stream doesn't need absolute anymore right?
     - [x] Favicon
     - [x] Touch icon
     - [x] Messenger preview
     - [x] Access log
     - [x] Docker access log anaylizer
     - [x] Docker-compose map database to outside
     - [ ] resonate.is
     - [ ] Stream aac [^2]
- [ ] QR Code
   - [ ] Design sticker
   - [ ] Write script to generate sticker
   - [ ] Print it, test it, deploy it

[^2]: ffmpeg -i aaaa-aaaa-aaaa-download.flac -movflags +faststart
aaaa-aaaa-aaaa-stream.m4a
