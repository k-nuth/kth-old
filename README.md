<!-- <a target="_blank" href="http://semver.org">![Version][badge.version]</a> -->
<!-- <a target="_blank" href="https://cirrus-ci.com/github/k-nuth/node-exe">![Build Status][badge.Cirrus]</a> -->

## ⚠️ Project Status: Archived / Deprecated

**This repository is kept only for historical purposes and because it contains open Issues that we will still be addressing.**  
It is no longer under active development.

Knuth development continues in the new monorepo, which replaces this project and concentrates all current work:

👉 **Active repository:** https://github.com/k-nuth/kth-mono

We recommend using and following that repository for the latest updates, releases, and documentation.

---

# knuth <a target="_blank" href="https://github.com/k-nuth/node-exe/releases">![Github Releases][badge.release]</a> <a target="_blank" href="https://github.com/k-nuth/node-exe/actions">![Build status][badge.GithubActions]</a> <a href="#">![CPP][badge.cpp]</a> <a target="_blank" href="https://t.me/knuth_cash">![Telegram][badge.telegram]</a> <a target="_blank" href="https://k-nuth.slack.com/">![Slack][badge.slack]</a>

> High performance Bitcoin development platform.

Knuth is a high performance implementation of the Bitcoin protocol focused on users requiring extra performance and flexibility, what makes it the best platform for wallets, exchanges, block explorers and miners.

## Not just a node

Knuth is a multi-crypto full node, but it is also a development platform.

Knuth's core is written in C++20, on top of it we provide a set of libraries and modules written in various programming languages that you can use as basis for building your application.

At the moment we have libraries in the following languages: [C++](https://github.com/k-nuth/node), [C](https://github.com/k-nuth/c-api), [C#](https://github.com/k-nuth/cs-api), [Python](https://github.com/k-nuth/py-api), [Javascript](https://github.com/k-nuth/js-api) and [Golang](https://github.com/k-nuth/go-api).
You can build your own library in the language of your choice on top of our [C library](https://github.com/k-nuth/c-api).

## Performance matters

We designed Knuth to be a high performance node, so our build system has the ability to automatically detect the microarchitecture of your processor and perform an optimized build for it.

For those who don't want to wait for compilation times, we provide pre-built binaries compatible with [Intel's Haswell microarchitecture](https://en.wikipedia.org/wiki/Haswell_(microarchitecture)). But you don't have to worry about that, our build system will do everything for you.

## Modular architecture

Knuth is based on a modular architecture simple to modify, expand and learn.

Any protocol change can be introduced in Knuth much faster and more efficiently than in reference implementations.

## Cross-platform

Knuth can be used in any computer architecture and operating system, it only requires a 64-bit system.

Knuth has been well tested on x86-64 processors and on the following operating systems: FreeBSD, Linux, macOS and Windows. However, it is not limited to these, Knuth can be used in any computer architecture and any operating system, the only requirement is a 64-bit system.

If you find a problem in any other platform, please [let us know](https://github.com/k-nuth/kth/issues).

## Getting started

Install and run Knuth is very easy:

1. Install and configure the Knuth build helper:
```
$ pip install kthbuild --user --upgrade

$ conan config install https://github.com/k-nuth/ci-utils/raw/master/conan/config2023.zip

```

2. Install the appropriate node executable:

```
$ conan install --requires=kth/0.46.0 --update --deploy=direct_deploy
```

3. Run the node:

```
$ ./kth/bin/kth
```
For more more detailed instructions, please refer to our [documentation](https://k-nuth.github.io/docs/).

## Donation

See [fund.kth.cash](https://fund.kth.cash/) for active Flipstarter campaigns.

Our general donation address is:
`bitcoincash:qrlgfg2qkj3na2x9k7frvcmv06ljx5xlnuuwx95zfn`

## License

Knuth node is released under the terms of the MIT license. See COPYING for more information or see https://opensource.org/licenses/MIT.

## Issues

Each of our modules has its own Github repository, but in case you want to create an issue, please do so in our [main repository](https://github.com/k-nuth/kth/issues).

## Contact

You can contact us through our [Telegram](https://t.me/knuth_cash) and [Slack](https://k-nuth.slack.com/) groups or write to us at info@kth.cash.

## Security Disclosures
To report security issues please contact:

Fernando Pelliccioni (fpelliccioni@gmail.com) - GPG Fingerprint: 8C1C 3163 AAE1 0EFA 704C 8A00 FE77 07B7 4C29 E389

<!-- Links -->
[badge.Travis]: https://travis-ci.org/k-nuth/node-exe.svg?branch=master
[badge.Appveyor]: https://ci.appveyor.com/api/projects/status/github/k-nuth/node-exe?svg=true&branch=master
[badge.Cirrus]: https://api.cirrus-ci.com/github/k-nuth/node-exe.svg?branch=master
[badge.GithubActions]: https://img.shields.io/endpoint.svg?url=https%3A%2F%2Factions-badge.atrox.dev%2Fk-nuth%2Fnode-exe%2Fbadge&style=for-the-badge
[badge.version]: https://badge.fury.io/gh/k-nuth%2Fkth-node-exe.svg
[badge.release]: https://img.shields.io/github/v/release/k-nuth/node-exe?display_name=tag&style=for-the-badge&color=3b009b&logo=bitcoincash
[badge.cpp]: https://img.shields.io/badge/C++-20-blue.svg?logo=c%2B%2B&style=for-the-badge
[badge.telegram]: https://img.shields.io/badge/telegram-badge-blue.svg?logo=telegramlogo=slack&style=for-the-badge
[badge.slack]: https://img.shields.io/badge/slack-badge-orange.svg?logo=slacklogo=slack&style=for-the-badge
<!-- [badge.Gitter]: https://img.shields.io/badge/gitter-join%20chat-blue.svg -->
