# 0009 Architectural Decision Record Template

- Date: 2026-04-23
- Author(s): [Laura Corkin][nzlaura]
- Status: `Active`

## Decision

Adopting [djangofmt][djangofmt] as a linting tool for Django templates

## Context

Through development on a number of codebases, one of the challenges that comes up for readability and maintenance
when working with django templates has been inconsistent formatting our django templates. We don't currently have
any tools that we're using to format or lint our django templates. In the past, finding a library to format our 
Django templates has been challenging, because often tools used for formatting `.html` files have a negative impact
on template tags, thus causing issues with functionality. 

We found a tool [djangofmt][djangofmt]- which consistently lints templates without impacting functionality of the 
template tags we use in Django templates. It has a small number of configuration options that you can use to suit 
your preferences for how the tool works.

Another package considered was [djLint][djLint] as it is a well established Django template formatting library. 
There were a number of drawbacks with using this package, for example it had some less than ideal formatting for 
attributes. 
 
The library also has a large number of configuration options, which can at times make it challenging to decide on a
set of sensible defaults for how we'd like to use it within our projects. 

## Implications

This adds a tool which has a slightly different configuration to our usual python code, using two spaces for indenting. 
Two space indenting matches the tooling we use for frontend code formatting, and can improve readability in django templates.

In addition, we've chosen to retain self-closing void tags, which again is in line with frontend tooling like prettier.

<!-- Links -->
[nzlaura]: mailto:laura.corkin@ackama.com
[djangofmt]: https://github.com/UnknownPlatypus/djangofmt
[djLint]: https://github.com/djlint/djLint
