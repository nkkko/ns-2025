Project Path: marp

Source Tree:

```
marp
├── marp.png
├── LICENSE
├── netlify.toml
├── website
│   ├── tailwind.config.js
│   ├── css
│   │   ├── index.css
│   │   └── plugin-rem.js
│   ├── next.config.js
│   ├── utils
│   │   ├── title.ts
│   │   ├── date.ts
│   │   ├── markdown
│   │   │   ├── index.tsx
│   │   │   ├── renderer
│   │   │   │   ├── sanitize.ts
│   │   │   │   └── index.ts
│   │   │   └── parse
│   │   │       ├── marp-code-block.ts
│   │   │       ├── image-paragrpah-to-figure.ts
│   │   │       └── index.ts
│   │   ├── url.ts
│   │   └── hooks
│   │       └── useFontFace.tsx
│   ├── docs
│   │   ├── guide
│   │   │   ├── image-syntax.md
│   │   │   ├── fragmented-list.md
│   │   │   ├── how-to-write-slides.md
│   │   │   ├── directives.md
│   │   │   ├── heading-divider.md
│   │   │   ├── theme.md
│   │   │   ├── math-typesetting.md
│   │   │   └── fitting-header.md
│   │   ├── tools
│   │   │   ├── marp-cli.md
│   │   │   └── marp-for-vs-code.md
│   │   ├── introduction
│   │   │   ├── whats-marp.md
│   │   │   └── install.md
│   │   └── manifest.yaml
│   ├── next-env.d.ts
│   ├── blog
│   │   ├── re-creation-of-marp-website.md
│   │   ├── the-story-of-marp-next.md
│   │   ├── marp-for-vs-code-v1.md
│   │   ├── marpit-v2-marp-core-v2-and-marp-cli-v1.md
│   │   ├── how-to-make-custom-transition.md
│   │   └── 202205-ecosystem-update.md
│   ├── components
│   │   ├── top
│   │   │   ├── Hero.tsx
│   │   │   ├── Features.tsx
│   │   │   ├── Description.tsx
│   │   │   └── GetStarted.tsx
│   │   ├── Marp.tsx
│   │   ├── Title.tsx
│   │   ├── ScrollToTop.tsx
│   │   ├── markdown
│   │   │   ├── Pre.tsx
│   │   │   ├── Heading.tsx
│   │   │   ├── Image.tsx
│   │   │   └── Anchor.tsx
│   │   ├── Typography.tsx
│   │   ├── docs
│   │   │   ├── Breadcrumb.tsx
│   │   │   ├── layouts
│   │   │   │   ├── Desktop.tsx
│   │   │   │   └── Mobile.tsx
│   │   │   ├── Layout.tsx
│   │   │   └── Navigation.tsx
│   │   ├── blog
│   │   │   └── BlogHeader.tsx
│   │   ├── Footer.tsx
│   │   ├── Layout.tsx
│   │   ├── Header.tsx
│   │   ├── Button.tsx
│   │   └── CodeBlock.tsx
│   ├── public
│   │   ├── apple-touch-icon-180x180.png
│   │   ├── blog
│   │   ├── favicon.png
│   │   ├── og-images
│   │   │   ├── 202205-ecosystem-update.jpg
│   │   │   ├── the-story-of-marp-next.png
│   │   │   ├── marp-for-vs-code-v1.jpg
│   │   │   └── how-to-make-custom-transition.jpg
│   │   └── assets
│   │       ├── hero-background.svg
│   │       ├── marp-cli.png
│   │       ├── marp.svg
│   │       ├── hero-background.jpg
│   │       ├── og-image.png
│   │       ├── marp-for-vs-code-v1
│   │       │   ├── auto-completion.png
│   │       │   ├── plan-sidebar.gif
│   │       │   ├── diagnostics.png
│   │       │   └── hover-help.png
│   │       ├── docs
│   │       │   └── directives.png
│   │       ├── marp-for-vs-code.png
│   │       ├── 202205-ecosystem-update
│   │       │   └── transition-showcase-poster.jpg
│   │       ├── marpit.svg
│   │       ├── marp-logo.svg
│   │       ├── how-to-make-custom-transition
│   │       │   ├── dissolve-opacity.mp4
│   │       │   ├── slide-up-wrong-direction.gif
│   │       │   ├── slide-up-translate-y.png
│   │       │   ├── transition-diagram.jpg
│   │       │   └── slide-up-correct-direction.gif
│   │       └── noise.svg
│   ├── babel.config.js
│   ├── package.json
│   ├── global.d.ts
│   ├── tsconfig.json
│   ├── assets.d.ts
│   ├── postcss.config.js
│   └── pages
│       ├── index.tsx
│       ├── 404.tsx
│       ├── docs
│       │   └── [[...slug]].tsx
│       ├── _document.tsx
│       ├── blog
│       │   └── [slug].tsx
│       ├── blog.tsx
│       └── _app.tsx
├── marp-dark.png
├── README.md
├── yarn.lock
├── package.json
└── tsconfig.json

```

`/Users/nikola/dev/marp/LICENSE`:

```
MIT License

Copyright (c) 2018-2023 Marp team (marp-team@marp.app)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

```

`/Users/nikola/dev/marp/netlify.toml`:

```toml
[build]
  publish = "website/out"
  command = "yarn workspace @marp-team/marp-website export"

[[headers]]
  for = "/*"
  [headers.values]
    Permissions-Policy = "interest-cohort=()"

```

`/Users/nikola/dev/marp/website/tailwind.config.js`:

```js
const { fontFamily } = require('tailwindcss/defaultTheme')

const marp = {
  // Brand colors
  brand: '#0288d1',
  light: '#67b8e3',
  dark: '#02669d',

  // Color variations
  darken: '#0277b7',
  darkest: '#1b4d68',
}

const gray = {
  100: '#f7fafc',
  200: '#edf2f7',
  300: '#e2e8f0',
  400: '#cbd5e0',
  500: '#a0aec0',
  600: '#718096',
  700: '#4a5568',
  800: '#2d3748',
  900: '#1a202c',
}

module.exports = {
  content: ['@(components|pages|utils)/**/*.[jt]s?(x)'],
  theme: {
    borderColor: (theme) => ({ ...theme('colors'), DEFAULT: gray[300] }),
    colors: {
      black: '#000',
      current: 'currentColor',
      gray,
      transparent: 'transparent',
      white: '#fff',
      background: '#f8f8f8',
      foreground: gray[800],
      marp,
    },
    ringColor: (theme) => ({ ...theme('colors'), DEFAULT: marp.light }),
    ringOffsetColor: (theme) => ({ ...theme('colors'), DEFAULT: marp.light }),
    fontFamily: {
      ...fontFamily,
      sans: ['Inter', ...fontFamily.sans],
      rounded: ['Quicksand', 'Avenir', 'Century Gothic', ...fontFamily.sans],
    },
    screens: {
      sm: '640px',
      md: '768px',
      lg: '1024px',
      xl: '1280px',
    },
    extend: { transitionDuration: { 0: '0s' } },
  },
}

```

`/Users/nikola/dev/marp/website/css/index.css`:

```css
@tailwind base;
@tailwind components;
@tailwind utilities;

:root {
  --noise-image: url('/assets/noise.svg');
  --header-height: 4rem;
  --anchor-margin: var(--header-height);

  scroll-padding-top: var(--anchor-margin);
}

@screen md {
  :root {
    --header-height: 5rem;
  }
}

* {
  scrollbar-color: theme('colors.gray.500') theme('colors.gray.300');
  scrollbar-width: thin;
}
*::-webkit-scrollbar {
  width: 8px;
  height: 8px;
}
*::-webkit-scrollbar-track {
  @apply bg-gray-300;
}
*::-webkit-scrollbar-thumb {
  @apply rounded-full bg-gray-500 bg-clip-padding;

  border: 1px solid transparent;
}
*::-webkit-scrollbar-thumb:hover {
  @apply bg-gray-600;
}
*::-webkit-scrollbar-thumb:hover:active {
  @apply bg-gray-700;
}

html:not(.translating) {
  scroll-behavior: smooth;
}

body {
  @apply text-foreground bg-background relative min-h-full;
}

body::before {
  @apply bg-background fixed inset-0 block;

  background-image: var(--noise-image),
    linear-gradient(
      to bottom,
      theme('colors.gray.100'),
      theme('colors.background') 50%
    );
  content: '';
  z-index: -1;
}

a:not(.custom-anchor) {
  @apply text-marp-darken;
}

a:not(.custom-anchor):hover {
  @apply text-marp-dark underline transition-colors duration-300;
}

a:not(.custom-anchor):hover:active {
  @apply text-marp-darkest duration-0;
}

mark {
  background: none;
  color: inherit;
  box-shadow: inset 0 -0.2em theme('colors.marp.light');
}

/* NProgress */
#nprogress .bar {
  @apply bg-marp-brand;
}
#nprogress .peg {
  @apply shadow-none;
}

/* Helper classes */
.text-gradient {
  @apply text-marp-brand leading-tight;
}

@supports (background-clip: text) {
  .text-gradient {
    @apply bg-marp-brand bg-clip-text text-transparent;

    background-image: linear-gradient(
      -1deg,
      theme('colors.marp.light'),
      theme('colors.marp.brand'),
      theme('colors.marp.dark')
    );
  }
}

```

`/Users/nikola/dev/marp/website/css/plugin-rem.js`:

```js
// Based on Marpit PostCSS rem plugin
// https://github.com/marp-team/marpit/blob/main/src/postcss/root/rem.js

const rootFontSizeCustomProp = '--root-font-size'
const skipParsingMatcher = /("[^"]*"|'[^']*'|(?:attr|url|var)\([^)]*\))/g

module.exports = () => ({
  postcssPlugin: 'marp-rem',
  Once: (css) =>
    css.walkDecls((decl) => {
      if (decl.prop === rootFontSizeCustomProp) return

      decl.value = decl.value
        .split(skipParsingMatcher)
        .map((v, i) => {
          if (i % 2) return v

          return v.replace(
            /(-?\d*\.?\d+)rem\b/g,
            (_, num) => `calc(var(${rootFontSizeCustomProp}, 1rem) * ${num})`
          )
        })
        .join('')
    }),
})

module.exports.postcss = true

```

`/Users/nikola/dev/marp/website/next.config.js`:

```js
const path = require('path')
const withBundleAnalyzer = require('@next/bundle-analyzer')({
  enabled: !!process.env.ANALYZE,
})
const { devDependencies } = require('./package.json')

// Build test function to ignore devDependencies in client build
const ignoreIncludedPaths = Object.keys(devDependencies).map(
  (m) => path.join(path.resolve(__dirname, '../node_modules'), m) + path.sep
)
const ignoreExcludedPaths = [require.resolve('@marp-team/marp-core/browser')]

const testToignoreDevDependenciesInClient = (id) =>
  !ignoreExcludedPaths.some((p) => id.startsWith(p)) &&
  ignoreIncludedPaths.some((p) => id.startsWith(p))

// Environments
const env = { BUILD_YEAR: new Date().getFullYear().toString() }
if (process.env.URL) env.NEXT_PUBLIC_HOST = process.env.URL // for Netlify's deploy preview

module.exports = withBundleAnalyzer({
  env,
  transpilePackages: [
    'hast-util-sanitize',
    'hast-util-whitespace',
    'unist-util-is',
    'unist-util-remove-position',
    'unist-util-visit',
  ],
  webpack: (config, { isServer }) => {
    config.module.rules.push({ test: /\.md$/, type: 'asset/source' })
    config.module.rules.push({
      test: /\.ya?ml$/,
      type: 'json',
      use: {
        loader: 'yaml-loader',
        options: { asJSON: true },
      },
    })
    config.module.rules.push({
      test: /\.svg$/,
      use: '@svgr/webpack',
    })

    if (!isServer) {
      config.module.rules.push({
        test: testToignoreDevDependenciesInClient,
        issuer: [__dirname],
        use: 'null-loader',
      })
    }

    return config
  },
})

```

`/Users/nikola/dev/marp/website/utils/title.ts`:

```ts
export const generateTitle = (breadcrumbs: string[] = []) =>
  [
    ...breadcrumbs,
    `Marp${
      breadcrumbs.length === 0 ? ': Markdown Presentation Ecosystem' : ''
    }`,
  ].join(' | ')

```

`/Users/nikola/dev/marp/website/utils/date.ts`:

```ts
const monthNames = [
  'January',
  'February',
  'March',
  'April',
  'May',
  'June',
  'July',
  'August',
  'September',
  'October',
  'November',
  'December',
] as const

const nth = (day) => {
  if (day > 3 && day < 21) return `${day}th`

  const firstPlace = day % 10
  if (firstPlace === 1) return `${day}st`
  if (firstPlace === 2) return `${day}nd`
  if (firstPlace === 3) return `${day}rd`

  return `${day}th`
}

export const formatDate = (date: Date) =>
  `${monthNames[date.getMonth()]} ${nth(date.getDate())}, ${date.getFullYear()}`

export const formatDateShort = (date: Date) =>
  `${date.getFullYear()}-${`${date.getMonth() + 1}`.padStart(
    2,
    '0'
  )}-${`${date.getDate()}`.padStart(2, '0')}`

```

`/Users/nikola/dev/marp/website/utils/markdown/index.tsx`:

```tsx
import matter from 'gray-matter'
import { parse as mdParse } from './parse'
import { renderer } from './renderer'
import { AnchorLinkProvider } from 'components/markdown/Heading'

const toJSON = (value: any) => JSON.parse(JSON.stringify(value))

export const parseMatter = (md: string) =>
  matter(md, { excerpt_separator: '<!-- more -->' })

export const parse = async (markdown: string) => {
  const md = parseMatter(markdown)
  const mdast = toJSON(await mdParse(md.content))

  return { markdown, mdast, data: toJSON(md.data) }
}

export const renderToReact = (
  mdast: any,
  { anchorLink = true }: { anchorLink?: boolean } = {}
) => (
  <AnchorLinkProvider value={anchorLink}>{renderer(mdast)}</AnchorLinkProvider>
)

```

`/Users/nikola/dev/marp/website/utils/markdown/renderer/sanitize.ts`:

```ts
import { defaultSchema } from 'hast-util-sanitize'

export const sanitize = {
  ...defaultSchema,
  attributes: {
    ...defaultSchema.attributes,
    '*': [...(defaultSchema.attributes?.['*'] ?? []), 'data*'],
  },
  clobberPrefix: '',
  tagNames: [...(defaultSchema.tagNames ?? []), 'marp-slides'],
}

```

`/Users/nikola/dev/marp/website/utils/markdown/renderer/index.ts`:

```ts
import { createElement, FunctionComponent } from 'react'
import RemarkReact, { Options } from 'remark-react'
import { sanitize } from './sanitize'
import { MarpSlides } from 'components/Marp'
import { Anchor } from 'components/markdown/Anchor'
import * as Heading from 'components/markdown/Heading'
import { Image } from 'components/markdown/Image'
import { Pre, toHastCodeHandler } from 'components/markdown/Pre'

const remarkReactComponents: Record<string, FunctionComponent<any>> = {
  a: Anchor,
  h1: Heading.H1,
  h2: Heading.H2,
  h3: Heading.H3,
  h4: Heading.H4,
  h5: Heading.H5,
  h6: Heading.H6,
  'marp-slides': MarpSlides,
  pre: Pre,
  img: Image,
}

export const { Compiler: renderer } = new RemarkReact({
  createElement: createElement as Options['createElement'],
  remarkReactComponents,
  sanitize,
  toHast: { handlers: { code: toHastCodeHandler } },
})

```

`/Users/nikola/dev/marp/website/utils/markdown/parse/marp-code-block.ts`:

```ts
import type { Literal } from 'unist'
import { visit } from 'unist-util-visit'
import { RenderedMarp, generateRenderedMarp } from 'components/Marp'

export const marpCodeBlock = () => async (tree) => {
  const marpNodes = new Set<Literal<string> & { marp?: RenderedMarp }>()

  visit(tree, 'code', (node) => {
    const lang = node.lang as string
    const langSub = lang.split(':').pop() as string

    if (langSub === 'marp') marpNodes.add(node)
  })

  await Promise.all(
    [...marpNodes].map((node) =>
      (async () => {
        node.marp = await generateRenderedMarp(node.value)
      })()
    )
  )
}

```

`/Users/nikola/dev/marp/website/utils/markdown/parse/image-paragrpah-to-figure.ts`:

```ts
import { whitespace } from 'hast-util-whitespace'
import { visit } from 'unist-util-visit'

// Based on remark-unwrap-images
// https://github.com/remarkjs/remark-unwrap-images/blob/main/index.js
const applicable = (node, inLink = false): string | false | null => {
  const { children } = node
  const { length } = children

  let image: string | false | null = null
  let index = -1

  while (++index < length) {
    const child = children[index]

    if (whitespace(child)) {
      // No ops
    } else if (child.type === 'image' && typeof child.title === 'string') {
      image = child.title.trim()
      child.title = image || null
    } else if (
      !inLink &&
      (child.type === 'link' || child.type === 'linkReference')
    ) {
      const linkResult = applicable(child, true)

      if (linkResult === false) return false
      if (typeof linkResult === 'string') image = linkResult
    } else {
      return false
    }
  }

  return image
}

// Transform wrapping paragraph for images with title to <figure>.
export const imageParagraphToFigure = () => (tree) => {
  visit(tree, 'paragraph', (node) => {
    const figureCaption = applicable(node)

    if (typeof figureCaption === 'string') {
      node.data = node.data ?? {}
      node.data.hName = 'figure'

      if (figureCaption.trim()) {
        ;(node.children as any[]).push({
          type: 'strong',
          data: { hName: 'figcaption' },
          children: [{ type: 'text', value: figureCaption }],
        })
      }
    }
  })
}

```

`/Users/nikola/dev/marp/website/utils/markdown/parse/index.ts`:

```ts
import remarkGfm from 'remark-gfm'
import remarkParse from 'remark-parse'
import remarkSlug from 'remark-slug'
import { unified, Processor } from 'unified'
import { removePosition } from 'unist-util-remove-position'
import { imageParagraphToFigure } from './image-paragrpah-to-figure'
import { marpCodeBlock } from './marp-code-block'

let parser: Processor | undefined

export const parse = async (md: string) => {
  parser =
    parser ||
    unified()
      .use(remarkParse)
      .use(remarkGfm)
      .use(remarkSlug)
      .use(imageParagraphToFigure)
      .use([marpCodeBlock])

  return removePosition(await parser.run(parser.parse(md)), true)
}

```

`/Users/nikola/dev/marp/website/utils/url.ts`:

```ts
export const absoluteUrl = (path: string) =>
  new URL(path, process.env.NEXT_PUBLIC_HOST)

```

`/Users/nikola/dev/marp/website/utils/hooks/useFontFace.tsx`:

```tsx
import { createContext, useContext, useEffect, useMemo, useState } from 'react'

interface FontFaceContextInterface {
  styles: readonly string[]
  setStyles: (styles: string[] | ((styles: string[]) => string[])) => void
}

const FontFaceContext = createContext<FontFaceContextInterface>({
  styles: [],
  setStyles: () => {
    throw new Error('Required wrapping by <FontFaceProvider>.')
  },
})

export const useFontFace = (fonts: string | string[]) => {
  const fnts = useMemo(() => ([] as string[]).concat(fonts), [fonts])
  const { setStyles } = useContext(FontFaceContext)

  useEffect(() => {
    setStyles((styles) => [...styles, ...fnts])

    return () => {
      const _fnts = [...fnts]

      setStyles((styles) =>
        styles.filter((existingStyle) => {
          const fntIdx = _fnts.indexOf(existingStyle)
          if (fntIdx >= 0) _fnts.splice(fntIdx, 1)

          return fntIdx !== -1
        })
      )
    }
  }, [fnts, setStyles])
}

// eslint-disable-next-line @typescript-eslint/ban-types
export const FontFaceProvider: React.FC<React.PropsWithChildren<{}>> = ({
  children,
}) => {
  const [styles, setStyles] = useState<string[]>([])

  return (
    <FontFaceContext.Provider value={{ styles, setStyles }}>
      {children}
    </FontFaceContext.Provider>
  )
}

export const FontFaceRenderer = () => {
  const { styles } = useContext(FontFaceContext)

  return (
    <>
      {[...new Set(styles)]
        .filter((style) => !!style)
        .map((style) => (
          <style data-type="marp-font-face" key={style}>
            {style}
          </style>
        ))}
    </>
  )
}

```

`/Users/nikola/dev/marp/website/docs/guide/image-syntax.md`:

```md
# Image syntax

### This is a stub page!

> This feature is inherited from [Marpit framework](https://marpit.marp.app/image-syntax).

```

`/Users/nikola/dev/marp/website/docs/guide/fragmented-list.md`:

```md
# Fragmented list

Marp uses some uncommon list markers to denote a **fragmented list** (also known as an incremental list or builds), which allows list content to appear incrementally.

Fragmented lists are _only available if you export to HTML_. If you export to PDF and PPTX, the fragmented list will be rendered as a normal list.

> Be careful when using fragmented lists. While fragmented lists can help focus the audience's attention on the last displayed item, they may also create confusion about hidden items. Some articles recommend never using builds (e.g. [Presentation Rules](http://www.jilles.net/perma/2020/06/05/presentation-rules.html)).

## For bullet lists

CommonMark's bullet list markers are `-`, `+`, and `*` (https://spec.commonmark.org/0.29/#bullet-list-marker). If you use `*` as the marker, Marp will parse the list as a fragmented list.

<!-- prettier-ignore-start -->

```markdown
# Bullet list

- One
- Two
- Three

---

# Fragmented list

* One
* Two
* Three
```

<!-- prettier-ignore-end -->

## For ordered list

CommonMark's [ordered list marker](https://spec.commonmark.org/0.29/#ordered-list-marker) must have `.` or `)` after digits. If you use `)` as the following character, then Marp will parse the ordered list as a fragmented list.

<!-- prettier-ignore-start -->

```markdown
# Ordered list

1. One
2. Two
3. Three

---

# Fragmented list

1) One
2) Two
3) Three
```

<!-- prettier-ignore-end -->

> These are inherited from [Marpit framework](https://marpit.marp.app/fragmented-list).
>
> [This syntax only indicates that the list _should_ be fragmented](https://marpit.marp.app/fragmented-list?id=rendering). If the tools integrated with Marp do nothing with the syntax, this list would be rendered as a normal list. In the official toolset, [Marp CLI](https://github.com/marp-team/marp-cli)'s default HTML template `bespoke` can reproduce a fragmented list as a build animation.

```

`/Users/nikola/dev/marp/website/docs/guide/how-to-write-slides.md`:

```md
# How to write slides

## Markdown

To write slides using Marp, you have to know basic Markdown syntax. It doesn't take long to learn the basics, and there are many Markdown tutorials on the internet, so this guide will focus on the additional syntax used by Marp that allows you to write slides.

### Resources for learning Markdown

- **[Markdown Guide](https://www.markdownguide.org/)** - A simple guide on how to use Markdown
- **[Markdown Tutorial](https://www.markdowntutorial.com/)** - Step-by-step Markdown tutorials with interactive exercises

## Slides

OK, let's write presentation slides. Marp splits slides in the deck using the horizontal ruler (e.g. `---`).

```markdown
# Slide 1

Hello, world!

---

# Slide 2

Marp splits slides in the deck by horizontal ruler.
```

```markdown:marp
# Slide 1

Hello, world!

---

# Slide 2

Marp splits slides in the deck by horizontal ruler.
```

If you use the `---` ruler, an empty line may be required before the ruler by [the spec of CommonMark](https://spec.commonmark.org/0.29/#example-28). If you do not want to add empty lines around the ruler, you can also use the underline ruler `___`, asterisk ruler `***`, or space-included ruler `- - -` to split slides.

> This feature is inherited from [Marpit framework](https://marpit.marp.app/markdown).

## Syntaxes

Marp's Markdown syntax is based on [CommonMark](https://commonmark.org/). In addition, Marp uses some extended syntax:

- Line breaks in a paragraph will convert to `<br />` tag automatically.
  - You also can use `<br />` tag directly (Useful if you need a line break within a [fitting header](/docs/guide/fitting-header)).
- There is special meaning in some (uncommon) list markers `*` and `1)`. [▶️ Fragmented list](/docs/guide/fragmented-list).
- Some extended syntaxes that came from [GitHub Flavored Markdown (GFM)](https://guides.github.com/features/mastering-markdown/#GitHub-flavored-markdown) are enabled:
  - [Automatic linking for URLs](https://github.github.com/gfm/#autolinks-extension-)
  - Emoji shortcode (provided by [markdown-it-emoji](https://github.com/markdown-it/markdown-it-emoji) and [twemoji](https://github.com/twitter/twemoji))
  - [Strikethrough](https://github.github.com/gfm/#strikethrough-extension-) (`~~strike~~`)
  - Syntax highlighting for code blocks (via [highlight.js](https://highlightjs.org/))
  - [Tables](https://github.github.com/gfm/#tables-extension-)
- Most HTML tags are _disabled_ by default for security reasons. Marp only allows users to use two tags by default: the `<style>` tag for tweaking the theme and the `<br />` tag mentioned earlier.
  - To enable all HTML tags, you need to opt-in for the Marp tool you are using.

> Many extended syntaxes are inherited from [Marp Core](https://github.com/marp-team/marp-core).

```

`/Users/nikola/dev/marp/website/docs/guide/directives.md`:

```md
# Directives

### This is a stub page!

Marp has an extended syntax called **"Directives"** to control theme, page number, header, footer, and other slide elements.

> The syntax of directives is inherited from [Marpit framework](https://marpit.marp.app/directives). Please note that different directives are used by each Marp tool.

## Usage

Marp parses directives as [YAML](https://yaml.org/).

### HTML comment

```markdown
<!--
theme: default
paginate: true
-->
```

### Front matter

Like many tools (e.g. [Jekyll site generator](https://jekyllrb.com/docs/front-matter/)), Marp uses **YAML front matter**. Directives can be defined in front matter.

YAML front matter must be at the beginning of a Markdown document and enclosed by dashed rulers.

```markdown
---
theme: default
paginate: true
---
```

Note that the dashed ruler is also used to indicate where Marp should [ split slides](/docs/guide/how-to-write-slides#slides). Marp uses the first two dashed rulers to indicate YAML front matter. Subsequent dashed rulers indicate slide breaks.

> TIP: Defining directives in the front matter is equivalent to setting the directives using an HTML comment on the first page. Suppose your favorite Markdown editor does not support the front matter syntax. In that case, you can safely define the directive in an HTML comment instead.

## Type of directives

There are two types of Marp directives:

- **[Global directives](#global-directives)** - Controlling settings for the all slides (e.g. `theme`, `size`)
- **[Local directives](#local-directives)** - Controlling setting values for one slide (e.g. `paginate`, `header`, `footer`)

You can define both directives in the same way. You can mix definitions too. The only difference is that some settings apply to all slides, and some apply to only one slide.

### Global directives

**Global directives** are settings for the entire slide deck.

| Name             | Description                                                                    |
| ---------------- | ------------------------------------------------------------------------------ |
| `theme`          | [Set a theme name for the slide deck ▶️](/docs/guide/theme)                    |
| `style`          | Specify CSS for tweaking theme                                                 |
| `headingDivider` | [Specify heading divider option ▶️](/docs/guide/heading-divider)               |
| `size`           | Choose the slide size preset provided by theme                                 |
| `math`           | [Choose a library to render math typesetting ▶️](/docs/guide/math-typesetting) |
| `title`          | Set a title of the slide deck                                                  |
| `author`         | Set an author of the slide deck                                                |
| `description`    | Set a description of the slide deck                                            |
| `keywords`       | Set comma-separated keywords for the slide deck                                |
| `url`            | Set canonical URL for the slide deck (for HTML export)                         |
| `image`          | Set Open Graph image URL (for HTML export)                                     |
| `marp`           | Set whether or not enable Marp feature in VS Code                              |

If you set the same global directive multiple times, Marp will use the last defined value.

### Local directives

**Local directives** are settings for a specific slide.

| Name                 | Description                                                                                                                               |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| `paginate`           | [Show page number on the slide if set to `true` ▶️](#page-number)                                                                         |
| `header`             | [Specify the content of the slide header ▶️](#header-and-footer)                                                                          |
| `footer`             | [Specify the content of the slide footer ▶️](#header-and-footer)                                                                          |
| `class`              | Set [HTML `class` attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/class) for the slide element `<section>` |
| `backgroundColor`    | Set [`background-color` style](https://developer.mozilla.org/en-US/docs/Web/CSS/background-color) of the slide                            |
| `backgroundImage`    | Set [`background-image` style](https://developer.mozilla.org/en-US/docs/Web/CSS/background-image) of the slide                            |
| `backgroundPosition` | Set [`background-position` style](https://developer.mozilla.org/en-US/docs/Web/CSS/background-position) of the slide                      |
| `backgroundRepeat`   | Set [`background-repeat` style](https://developer.mozilla.org/en-US/docs/Web/CSS/background-repeat) of the slide                          |
| `backgroundSize`     | Set [`background-size` style](https://developer.mozilla.org/en-US/docs/Web/CSS/background-size) of the slide                              |
| `color`              | Set [`color` style](https://developer.mozilla.org/en-US/docs/Web/CSS/color) of the slide                                                  |

#### Inheritance

Slides will inherit setting values of local directives from the immediately previous slide **unless** a local directive is explicitly set for the current slide. In other words, defined local directives will apply to both the defined page and subsequent pages.

For example, the Markdown for this set of slides defines the `backgroundColor` directive on the second page. Because subsequent pages inherit local directives, the third page will also have the same color.

```markdown
# Page 1

Go to next page :arrow_right:

---

<!-- backgroundColor: lightblue -->

# Page 2

## This page has a light blue background.

---

# Page 3

## This page also has the same light blue background.
```

```markdown:marp
# Page 1

Go to next page :arrow_right:

---

<!-- backgroundColor: lightblue -->

# Page 2

## This page has a light blue background.

---

# Page 3

## This page also has the same light blue background.
```

#### Scoped local directives

If you want a local directive to apply only to the current page, add the underscore prefix `_` to the name of directives.

The value of a scoped directive will be given priority over an inherited value, and subsequent pages will not inherit the value of the scoped directive.

```markdown
<!-- color: red -->

# Page 1

This page has red text.

---

<!-- _color: blue -->

# Page 2

This page has blue text, specified by a scoped local directive.

---

# Page 3

Go back to red text.
```

```markdown:marp
<!-- color: red -->

# Page 1

This page has red text.

---

<!-- _color: blue -->

# Page 2

This page has blue text, specified by a scoped local directive.

---

# Page 3

Go back to red text.
```

The underscore prefix can be added to any local directives.

#### Diagram

![The diagram of local directives and scoped directives](/assets/docs/directives.png 'The diagram of local directives and scoped directives')

## Theme

<!-- TODO: Link to "Theme" section -->

## Page number

To add page number to the slide, set the **`paginate`** local directive to `true`.

```markdown
<!-- paginate: true -->

You can see the slide number in the lower right.
```

```markdown:marp
<!-- paginate: true -->

You can see the slide number in the lower right.

<style>
  @keyframes point {
    from { background-position: bottom 55px right 55px; }
    to { background-position: bottom 40px right 40px; }
  }
  section {
    animation: 0.5s ease-in-out alternate infinite point;
    background: #fff url('https://icongr.am/feather/arrow-down-right.svg?color=0288d1') no-repeat bottom 40px right 40px / 100px;
  }
  @media (prefers-reduced-motion) {
    section {
      animation: none;
    }
  }
</style>
```

Refer to [theme guide](/docs/guide/theme) for details on how to style a slide number.

### Skip pagination in the title slide

Just move the definition of the `paginate` directive to the second slide.

```markdown
# Title slide

---

<!-- paginate: true --->

## Start pagination from this slide.
```

```markdown:marp
# Title slide

---

<!-- paginate: true --->

## Start pagination from this slide.

<style scoped>
  @keyframes point {
    from { background-position: bottom 55px right 55px; }
    to { background-position: bottom 40px right 40px; }
  }
  section {
    animation: 0.5s ease-in-out alternate infinite point;
    background: #fff url('https://icongr.am/feather/arrow-down-right.svg?color=0288d1') no-repeat bottom 40px right 40px / 100px;
  }
  @media (prefers-reduced-motion) {
    section {
      animation: none;
    }
  }
</style>
```

You can also use [scoped directive](#scoped-local-directives) to disable pagination in the title slide.

```markdown
---
paginate: true
_paginate: false
---

# Title slide

---

## Start pagination from this slide.
```

## Header and footer

Use **`header`** and **`footer`** local directives to add headers and footers to slides.

```markdown
<!--
header: Header content
footer: Footer content
-->

# Header and footer
```

```markdown:marp
<!--
header: Header content
footer: Footer content
-->

# Header and footer
<style>
  @keyframes point-up {
    from { background-position: 50px 50px; }
    to { background-position: 50px 70px; }
  }
  @keyframes point-down {
    from { background-position: left 50px bottom 50px; }
    to { background-position: left 50px bottom 70px; }
  }
  section {
    animation: 0.5s ease-in-out alternate infinite point-up;
    background: #fff url('https://icongr.am/feather/arrow-up.svg?color=0288d1') no-repeat 50px 50px / 80px;
  }
  section::before {
    content: '';
    display: block;
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    pointer-events: none;
    animation: 0.5s ease-in-out alternate infinite point-down;
    background: transparent url('https://icongr.am/feather/arrow-down.svg?color=0288d1') no-repeat left 50px bottom 50px / 80px;
  }
  @media (prefers-reduced-motion) {
    section, section::before {
      animation: none;
    }
  }
</style>
```

Refer to [theme guide](/docs/guide/theme) for details on how to style header and footer.

### Markdown formatting

You can use inline Markdown formatting (italic, bold, inline image, etc) in header and footer like this:

```markdown
---
header: '**bold** _italic_'
footer: '![image](https://example.com/image.jpg)'
---
```

To make directives parsable as valid YAML, you can wrap content with (double-)quotes.

### Reset header and footer

Set the value of a directive to an empty string value to reset the header and footer in the middle of the slide deck.

```markdown
---
header: '**Header**'
footer: '_Footer_'
---

# Example

---

<!--
header: ''
footer: ''
-->

## Reset header and footer
```

```markdown:marp
---
header: '**Header**'
footer: '_Footer_'
---

# Example

---

<!--
header: ''
footer: ''
-->

## Reset header and footer
```

## Styling slide

### Shorthand

## Editor integration

<!-- By using **Marp for VS Code**, you can preview -->

```

`/Users/nikola/dev/marp/website/docs/guide/heading-divider.md`:

```md
# Heading divider

The heading divider directive tells Marp to automatically add a slide break before a heading of the specified level. This directive is particularly useful when converting an existing Markdown document to slides.

Heading dividers is similar to [Pandoc](https://pandoc.org/)'s [`--slide-level` option](https://pandoc.org/MANUAL.html#structuring-the-slide-show) and [Deckset 2](https://www.deckset.com/2/)'s "Slide Dividers" option.

> This feature is inherited from the [Marpit framework](https://marpit.marp.app/directives?id=heading-divider).

## Example

Let’s say you have a Markdown document like this:

```markdown
# Markdown document

The article of Markdown

## What is Markdown?

> Markdown is a lightweight markup language for creating formatted text using a plain-text editor.
>
> _-- https://en.wikipedia.org/wiki/Markdown_

## History

### Origin

Markdown has created by John Gruber in 2004.

https://daringfireball.net/projects/markdown/

### Standardization

CommonMark is a project for a standardization of Markdown launched in 2012.
```

Add the [`headingDivider` global directive](/docs/guide/directives#global-directives).

```markdown
<!-- headingDivider: 2 -->
```

Once you have specified the directive, Marp will automatically split the document into slides by starting a new slide whenever a section has a heading level of 2.

```markdown:marp
<!-- headingDivider: 2 -->

# Markdown document

The article of Markdown

## What is Markdown?

> Markdown is a lightweight markup language for creating formatted text using a plain-text editor.
>
> _-- https://en.wikipedia.org/wiki/Markdown_

## History

### Origin

Markdown was created by John Gruber in 2004.

https://daringfireball.net/projects/markdown/

### Standardization

CommonMark is a project for a standardization of Markdown launched in 2012.
```

The `headingDivider` global directive accepts heading levels from 1 to 6. When the heading level is set as a number, Marp will split slides at headings that are _at the specified level and at all parent levels_. So, `headingDivider: 2` will actually make new slides at headings of levels 1 and 2.

If a section has so much content that it overflows the slide, it might be better to split it by subsection. To do that, just change the base level for `headingDivider` to `3`. Check out the difference from the previous example after the 3rd page:

```markdown:marp
<!-- headingDivider: 3 -->

# Markdown document

The article of Markdown

## What is Markdown?

> Markdown is a lightweight markup language for creating formatted text using a plain-text editor.
>
> _-- https://en.wikipedia.org/wiki/Markdown_

## History

### Origin

Markdown was created by John Gruber in 2004.

https://daringfireball.net/projects/markdown/

### Standardization

CommonMark is a project for a standardization of Markdown launched in 2012.
```

> [Rulers to split pages](/docs/guide/how-to-write-slides#slides) still work normally even if enabled `headingDivider`.

## Advanced

Auto split in parent heading levels is reasonable behavior in most cases, but sometimes you may require finer control of splitting levels. If you set the directive value to an array, you also instruct Marp to split at only the specified levels.

```markdown
<!-- headingDivider: [1, 3] -->
```

This setting will instruct Marp to split slides at heading levels 1 and 3.

```

`/Users/nikola/dev/marp/website/docs/guide/theme.md`:

```md
# Theme

### This is a stub page!

```

`/Users/nikola/dev/marp/website/docs/guide/math-typesetting.md`:

```md
# Math typesetting

[Many Markdown tools support math rendering](https://github.com/cben/mathdown/wiki/math-in-markdown). We have [Pandoc's Markdown style](https://pandoc.org/MANUAL.html#math) math typesetting support. Marp renders math using [MathJax] (or, alternatively, [KaTeX]).

[katex]: https://katex.org/
[mathjax]: https://www.mathjax.org/

### Inline math

Surround your formula with a single dollar character `$...$`.

```markdown
Render inline math such as $ax^2+bc+c$.
```

### Math block

Surround the formula with double dollar characters `$$...$$`. Math in the block element will render with centering. The math in the block element will also scale down automatically if it is sticking out from the horizontal border of the slide (only in supported themes).

<!-- prettier-ignore-start -->

```markdown
$$ I_{xx}=\int\int_Ry^2f(x,y)\cdot{}dydx $$

$$
f(x) =
  \int_{-\infty}^\infty
  \hat f(\xi)\,e^{2 \pi i \xi x}
  \,d\xi
$$
```
<!-- prettier-ignore-end -->

```markdown:marp
## Inline math

Render inline math such as $ax^2+bc+c$.

## Math block

$$ I_{xx}=\int\int_Ry^2f(x,y)\cdot{}dydx $$

$$
f(x) =
  \int_{-\infty}^\infty
  \hat f(\xi)\,e^{2 \pi i \xi x}
  \,d\xi
$$
```

> This feature is inherited from [Marp Core](https://github.com/marp-team/marp-core).

## [MathJax]

By default, Marp uses **[MathJax]** to render math typesetting.

### Declare to use MathJax

Set [`math` global directive](/docs/guide/directives#global-directives) as `mathjax`.

```markdown
---
math: mathjax
---

Render inline math such as $ax^2+bc+c$.
```

For the determined rendering of slide, we recommend always to declare math library to use in the slide. No definition of math directive may bring inconsistent rendering result depending on the version of Marp Core.

## [KaTeX]

**[KaTeX]** is an alternative library to render math typesettings in Marp, and it was former default.

By defining `math` global directive as `katex`, you can can continue to render math with KaTeX.

### Enable KaTeX

Set [`math` global directive](/docs/guide/directives#global-directives) as `katex`.

```markdown
---
math: katex
---

Render inline math such as $ax^2+bc+c$.
```

### Define global macro

In KaTeX rendering, macros defined by `\def` will persist only in a local math environment. To persist defined macro for subsequent math environments in Markdown, use `\gdef` (`\global\def`) instead.

```markdown
$$
% macroA can use only in this math block.
\def\macroA{{\color{red}A}}

% macroB has defined globally so you can use it after here.
\gdef\macroB{{\color{blue}B}}

\macroA + \macroB
$$

---

$$
% macroA cannot use, but macroB can.
\macroA + \macroB
$$
```

[See the detail of supported macro functions in KaTeX documentation](https://katex.org/docs/supported.html#macros).

### Configuration

KaTeX options can be configured in [Marp Core's constructor option](https://github.com/marp-team/marp-core#constructor-options). You should use [Marp CLI](https://github.com/marp-team/marp-cli) if you need to set a custom configuration in Marp conversion.

```javascript
// marp.config.js
module.exports = {
  options: {
    math: {
      lib: 'katex',
      katexFontPath: 'https://example.com/assets/katex-fonts/'
      katexOption: {
        errorColor: '#ff0000',
        macros: {
          '\\RR': '\\mathbb{R}',
        },
      },
    },
  },
}
```

```bash
marp -c marp.config.js marp-math.md
```

[See the details of KaTeX option in the documentation.](https://katex.org/docs/options.html)

### mhchem extension

[mhchem](https://mhchem.github.io/MathJax-mhchem/) is an extension for writing chemical equations. To enable mhchem in Marp, you should use a Marp CLI configuration file and follow [a guide of KaTeX for Node.js](https://katex.org/docs/node.html#using-mhchem-extension).

```javascript
// marp.config.js
const katex = require('katex')
require('katex/dist/contrib/mhchem.js') // modify katex module
```

```bash
marp -c marp.config.js marp-mhchem.md
```

A common mistake is [using a client-side `<script>` to load the extension](https://github.com/KaTeX/KaTeX/tree/master/contrib/mhchem#usage). _This will not work because Marp's rendering will be completed within Node.js, not the browser._ See also: [marp-team/marp#99](https://github.com/marp-team/marp/discussions/99)

### Known issues for KaTeX rendering

- KaTeX rendering requires fetching Web Fonts from [jsDelivr](https://www.jsdelivr.com/) CDN. If you are in offline or the limited network by proxy, the slide may not render math.
- Safari does not shrink down the big math block rendered by KaTeX. ([marp-team/marp-core#159](https://github.com/marp-team/marp-core/issues/159))
- Rendering of `\tag{}` is incompatible with the math block. ([marp-team/marp-core#236](https://github.com/marp-team/marp-core/issues/236))

```

`/Users/nikola/dev/marp/website/docs/guide/fitting-header.md`:

```md
# Fitting header

When the `<!--fit-->` comment is placed in a heading, the heading will be scaled to fit onto a single line.

```markdown
# <!-- fit --> Fitting header
```

```markdown:marp
# <!-- fit --> Fitting header
```

The syntax is similar to [Deckset's `[fit]` keyword](https://docs.decksetapp.com/English.lproj/Formatting/01-headings.html), but Marp uses an HTML comment to hide the keyword when the Markdown is rendered.

> This feature is inherited from [Marp Core](https://github.com/marp-team/marp-core).

## Examples

### Takahashi-style

You can efficiently make [Takahashi-style](https://en.wikipedia.org/wiki/Takahashi_method) slides like the [Big](https://github.com/tmcw/big) presentation system by using the fitting header. Combining fitting headers with the [heading divider](/docs/guide/heading-divider) directive will allow you to write one slide per line.

```markdown
---
theme: uncover
headingDivider: 1
---

# <!--fit--> Takahashi-style<br />presentation

# <!--fit--> Feature

# <!--fit--> Huge text

# <!--fit--> A few words
```

```markdown:marp
---
theme: uncover
headingDivider: 1
---

# <!--fit--> Takahashi-style<br />presentation

# <!--fit--> Feature

# <!--fit--> Huge text

# <!--fit--> A few words
```

```

`/Users/nikola/dev/marp/website/docs/tools/marp-cli.md`:

```md
# Marp CLI

### This is a stub page!

```

`/Users/nikola/dev/marp/website/docs/tools/marp-for-vs-code.md`:

```md
# Marp for VS Code

### This is a stub page!

```

`/Users/nikola/dev/marp/website/docs/introduction/whats-marp.md`:

```md
# What's Marp?

### This is a stub page!

**Marp** (**Mar**kdown **P**resentation Ecosystem) provides a great experience for _writing_ presentations with Markdown.

````markdown:marp
---
marp: true
theme: uncover
---

![Marp w:240](/assets/marp-logo.svg)

# **Marp**

Markdown Presentation Ecosystem

https://marp.app/

---

<!-- paginate: true -->

## What's Marp?

Marp provides a great experience for _writing_ presentations with Markdown. :pencil:

```markdown
# Slide 1

foo

---

# Slide 2

bar
```
````

## Concepts

### Markdown

[Markdown] is one of the most popular lightweight markup languages. Markdown allows the author to write presentations quickly and focus on the logical structure of the presentation (rather than the code needed to generate the presentation).

The Marp ecosystem is based on [CommonMark], a consistent spec of Markdown. Marp uses CommonMark to ensure maximum compatibility across Markdown editors and with other Markdown files. Marp only adds a few additional features on top of CommonMark, so your Marp document will look good regardless of what software you used to edit or render Markdown.

[markdown]: https://en.wikipedia.org/wiki/Markdown
[commonmark]: https://commonmark.org/

### Theme CSS

The Marp ecosystem is designed to be intuitive to anyone who has made a webpage. As long as you know HTML and CSS, you should be able to style your presentation easily. Our theming system allows you to use plain CSS to style your slides.

Marp is designed with the "[Separation of content and style](https://en.wikipedia.org/wiki/Separation_of_content_and_presentation)" in mind. The goal is to make it easy for users to apply designs made by the community to the user's content.

### Export to PDF, PPTX, HTML

Marp has first-class support for conversion into other file formats. We prioritize reproducible rendering across formats so that users do not have to worry about different formats breaking layouts. Our goal is to make sure the PDF, PPTX, and HTML versions of your slides look exactly the same.

Note that Marp is not designed to be stand-alone presentation software. The simplest and recommended way to present is to export to PDF, which allows you to present in any environment that supports PDFs. The PDF format is particularly useful if you are presenting without access to the internet. The HTML format allows you to serve your slide deck on the internet, show interactive content, and use features like fragmented lists. If you want to add additional content manually in Powerpoint, Marp also allows you to export to the PowerPoint (PPTX) format.

### Easy to get started

Our ecosystem provides both a CLI and a GUI (as an VS Code extension) for authoring a Marp slide deck. To create a slide deck, all you need to do is install Marp and write a Markdown file in the Marp format. If you want to export to PDF/PPTX, you will also need to have Chrome, Edge, or some other Chromium-flavored browser installed locally.

The Marp CLI can convert Markdown into HTML/PDF/PPTX easily. VS Code extension gives real-time slide preview, Marp Markdown language features, and export commands.

### Pluggable architecture

Marp is based on **[Marpit framework]**, the skinny framework for creating a slide deck from Markdown. It has a pluggable architecture, and developers can add features via plugin.

End users can customize the conversion engine by using Marp CLI and plugins: Add new Markdown syntax (compatible with markdown-it plugins), add custom directives, provide custom theme set, and so on. Push the limits of Marp as you like!

[marpit framework]: https://marpit.marp.app

## Author

We're [Marp team](https://github.com/marp-team). (Having said that, currently, Marp is a solo project by maintainer. The best way to join us is many contributions into Marp!)

- **Yuki Hattori ([@yhatt](https://github.com/yhatt))** - Project owner / maintainer

## License

All tools and related libraries by Marp team are licensed by [MIT License](https://github.com/marp-team/marp/blob/main/LICENSE).

```

`/Users/nikola/dev/marp/website/docs/introduction/install.md`:

```md
# Install

### This is a stub page!

There are two ways to use Marp, through a command-line interface (**[Marp CLI][marp cli]**) or through a graphical user interface (**[VS Code extension][marp for vs code]**). To start authoring presentations, you must install either the CLI or the VS Code exension.

## Should I use the Marp CLI or Marp for VS Code?

### Basic Comparison

|                   | Marp for VS Code |   Marp CLI   |
| ----------------: | :--------------: | :----------: |
|            Editor |     VS Code      |  Any editor  |
|      Live Preview |       Yes        |     Yes      |
|     Export Method | Click to export  | Command Line |
| Use Marp plugins? |        No        |     Yes      |

### Marp for VS Code

If you are not familiar with the command line, use the VS Code extension without hesitation! All of the basic Marp features are available in Marp for VS Code.

Even if you are CLI savvy, you may prefer to author presentations through Marp for VS Code. VS Code has many convenient features for authoring a slide deck, including Marp syntax completion and live preview.

### Marp CLI

Using Marp CLI is suited for following:

- Authoring Markdown and theme CSS with your favorite editor (such as vim)
- Batch processing
- Combination with other tools (through piping and redirection)
- Continuous Integration (CI)
- Server-side conversion
- Set advanced configuration of Marp
- Use Marp in Node.js project
- Use Marp / Marpit / markdown-it plugins
- Use the other Marpit flavored engine

## Installing [Marp for VS Code]

1. Install [Visual Studio Code].
2. Install the [Marp for VS Code] extension.
3. Create and open a new Markdown file (with `.md` extension).
4. Select the `Toggle Marp feature for current Markdown` command from the Marp icon in editor actions (toolbar). This command will add Marp to the front-matter of your Markdown file:
   ```markdown
   ---
   marp: true
   ---
   ```
5. Open VS Code Markdown preview, and start writing your presentation!

[visual studio code]: https://code.visualstudio.com/
[marp for vs code]: https://marketplace.visualstudio.com/items?itemName=marp-team.marp-vscode

## Installing [Marp CLI]

[marp cli]: https://github.com/marp-team/marp-cli

### [Homebrew](https://brew.sh/) (macOS)

```bash
brew install marp-cli
```

### [Scoop](https://scoop.sh/) (Windows)

```bash
scoop install marp
```

### [Node.js](https://nodejs.org/)

If you have installed Node.js >= 12, you can try one-shot conversion without installing powered by `npx` (`npm exec`).

```bash
npx @marp-team/marp-cli@latest markdown.md
```

#### Install to Node project

```bash
npm install --save-dev @marp-team/marp-cli
npx marp markdown.md
```

```bash
yarn add --dev @marp-team/marp-cli
yarn exec markdown.md
```

[You can also install the `marp` command globally](https://github.com/marp-team/marp-cli#global-installation), but it is _not recommended_.

#### Standalone binary

[➡️ Download the latest standalone binary from the GitHub release page...][standalone binary]

[standalone binary]: https://github.com/marp-team/marp-cli/releases

#### Docker

[➡️ Check out the overview of an official container in Docker Hub...][docker]

[docker]: https://hub.docker.com/r/marpteam/marp-cli/

```

`/Users/nikola/dev/marp/website/docs/manifest.yaml`:

```yaml
introduction:
  title: Introduction
  pages:
    whats-marp:
      title: What's Marp?
    install:
      title: Install
guide:
  title: Guide
  pages:
    how-to-write-slides:
      title: How to write slides
    directives:
      title: Directives
    theme:
      title: Theme
    heading-divider:
      title: Heading divider
    image-syntax:
      title: Image syntax
    fragmented-list:
      title: Fragmented list
    fitting-header:
      title: Fitting header
    math-typesetting:
      title: Math typesetting
tools:
  title: Tools
  pages:
    marp-cli:
      title: Marp CLI
    marp-for-vs-code:
      title: Marp for VS Code

```

`/Users/nikola/dev/marp/website/next-env.d.ts`:

```ts
/// <reference types="next" />
/// <reference types="next/image-types/global" />

// NOTE: This file should not be edited
// see https://nextjs.org/docs/basic-features/typescript for more information.

```

`/Users/nikola/dev/marp/website/blog/re-creation-of-marp-website.md`:

```md
---
title: Re-creation of Marp website for the unified docs
date: 2020-08-22
description: We are announcing that Marp team is working to the re-creation of marp.app website for hosting the unified documentation.
author: Yuki Hattori
github: yhatt
---

[marpit framework]: https://marpit.marp.app/
[marp core]: https://github.com/marp-team/marp-core
[marp cli]: https://github.com/marp-team/marp-cli
[marp for vs code]: https://marketplace.visualstudio.com/items?itemName=marp-team.marp-vscode

I could not have imagined that now we are living in a unique pandemic era when I wrote [the last article](/blog/the-story-of-marp-next). Even under those severe circumstances, I'm still making progress of Marp.

Marp gives some tools for making a convincing slide deck with fewer efforts, and they get loved by a lot of users. In early this year, [Marp Core] has reached the stable v1 release, and our tools around the core are keeping steps with it. Needless to mention here, we will keep going to enhance our tools.

Today we are announcing that **Marp team is working to the re-creation of [marp.app](/) website for hosting the unified documentation**. If you are reading this article, you should have already seen the re-created website! Currently the unified docs is not yet ready but we are going to announce here as soon as getting ready.

<!-- more -->

# For the unified documentation

As Marp ecosystem spreads out, Marp team has become to regard the lack of unified documentation as an important issue. Our docs are scattered to many repos per tool, and it would make confusion when learning overall of Marp. In addition, we often have been asked basics of Marp in the issue tracker and sometimes even prevent our works for evolving Marp.

For making users take advantage of Marp easier, I'm going to work improving the documentation together with evolving Marp tools.

## Re-created [marp.app](/)

The re-created web page is the first step for building the unified docs. I had tried various tools to build the website and found a place to rest in [Next.js](https://nextjs.org/) and [Tailwind CSS](https://tailwindcss.com/). I believe we will be able to build more useful documentation pages by these.

It is managed in our entrance repository [marp-team/marp](https://github.com/marp-team/marp) as same as before. If shipped new documentation, we would accept some improvements in the documentation from the community.

---

## Mid-term plans for Marp tools

Might as well, finally let me share some mid-term plans for each tools I'll work shortly.

- [Marpit framework]: Enhance directives
- [Marp Core]: Add new built-in theme and simplify auto-scaling feature
- [Marp CLI]: Handout template
- [Marp for VS Code]: Better auto-completion for Marp directives

We also had announced [long-term plans earlier](/blog/the-story-of-marp-next): [Marp Web](https://web.marp.app/), Marp integration modules with [React](https://github.com/marp-team/marp-react) and [Vue](https://github.com/marp-team/marp-react), and [Marpit v2](https://github.com/marp-team/marpit/issues/194). However, _they are not yet in active and may need to reconsider plans because we have not enough positive feedbacks from community._

```

`/Users/nikola/dev/marp/website/blog/the-story-of-marp-next.md`:

```md
---
title: The story of Marp Next
date: 2019-06-06
description: Today, I'm so excited to introduce the story of Marp Next! The full-rewritten Marp is not only just a writer. To be usable in various situations, we build a brand-new Marp ecosystem consisted of multiple modules.
author: Yuki Hattori
github: yhatt
image: /og-images/the-story-of-marp-next.png
---

The first version of [Marp](https://yhatt.github.io/marp/) was released at almost 3 years ago. At first, it was started from a simple tool for personal usage called "mdSlide". And now, Marp has been used by a lot of users who would recognize the real value of the presentation writer. Marp is amassed around [8,000 stars](https://github.com/yhatt/marp/stargazers) until now.

However, our headache brought from lacked maintainability to develop. We had received so many requests to the old Marp app, and it has to evolve to keep providing the best writing environment of presentation deck.

Today, I'm so excited to introduce the story of Marp Next! The full-rewritten Marp is not only just a writer. To be usable in various situations, we build **a brand-new Marp ecosystem** consisted of multiple modules. They are developed with JavaScript and TypeScript, and much more maintainable than the previous Marp.

<!-- more -->

# Marp ecosystem

Marp Next has two core components: **[Marpit]** framework and **[Marp Core]**. Tools by Marp ecosystem are usually based on these.

## Marpit

**[Marpit]** is _the skinny framework_ for creating HTML slide deck from Markdown. It is designed to convert Markdown into only minimum assets consisted of static HTML and CSS, and the output can convert into PDF slide deck by printing through Chrome / Chromium.

Marpit has created for using as the base of Marp ecosystem, but it is also independent framework. You may integrate Marpit's Markdown conversion with your tool, even if it's not Marp: [reveal.js](https://codesandbox.io/embed/nw80vrxvpp), [WebSlides](https://codesandbox.io/embed/j3wo2091yw), and so on.

[marpit]: https://marpit.marp.app/

### [Marpit Markdown]: Keep compatibillity with a plain Markdown document

We had received [many requests][issues] to the old Marp, about the additional syntax to help creating beautiful slide deck. On the other hand, we also have received a request that [must respect Markdown syntax strictly](https://github.com/yhatt/marp/issues/87). We have to deal with these contradicted issues.

Additional syntax provided by Marpit should never break [CommonMark](https://commonmark.org/) document. Thus, the result of rendering keeps looking nice even if you open the Marpit Markdown in a general Markdown editor. And you can even extend the additional syntax via [markdown-it plugins](https://marpit.marp.app/usage?id=extend-marpit-by-plugins) if you need.

[marpit markdown]: https://marpit.marp.app/markdown
[issues]: https://github.com/yhatt/marp/issues

### [Theme CSS]: Design your deck with clean markup

Marpit has the theming system to allow designing everything of slides by CSS.

The old Marp had the _limited_ theming system and required deep diving to internal for customization: Build system, [Sass], the logic of Marp app, and so on. So we had to create a brand-new theming system for easy customization of theme with only general CSS knowledge.

Marpit's it only requires a pure CSS, and no additional knowledges! You have only to focus styling HTML semantic elements. It means that you can create theme CSS from now!

In addition, Marpit has the pixel-perfect slide system like PowerPoint and Keynote. Theme creator never needs to worry about the responsive layout, and could provide design exactly as the author wanted with less effort.

[theme css]: https://marpit.marp.app/theme-css
[sass]: https://sass-lang.com/

### [Inline SVG slide]&nbsp;(Experimental)

Our unique idea is wrapping each slides by inline SVG. It might feel a bit strange, but makes many advantages.

- Supports pixel-perfect scaling via style definition and **realizes Zero-JS slide deck**.
- Isolates Markdown contents and prevents that injected DOM by Marpit's advanced feature breaks design defined in theme CSS.

Thanks to the power of SVG, we can keep a framework simple and maintainable. [Marp Core] is based on inline SVG slide by default.

[inline svg slide]: https://marpit.marp.app/inline-svg

## Marp Core

**[Marp Core]** is a base converter for our projects extended from Marpit. In short, it is a battery-included Marpit.

Marpit only has bare essential features, so it might have not enough to start writing your deck. Marp Core provides the practical syntax, additional features, and built-in themes.

Many of the features are based on the old desktop app, and have improved to be suitable to Marpit. Of course, we added the new features for creating more beautiful deck.

[marp core]: https://github.com/marp-team/marp-core

- Built-in themes (Default, Gaia, and _new_ Uncover theme)
- Included Emoji support 😁
- [KaTeX](https://katex.org/) Math typesetting
- `size` global directive
- Auto scaling features (_new_)
  - Fitting header via `<!-- fit -->` annotation
  - Scale-down overflowed fence, code, and math block

# Applications

## Marp CLI

[marp cli]: https://github.com/marp-team/marp-cli

**[Marp CLI]** is a CLI interface of Marpit and Marp Core converter. It's a Swiss-Army knife for Marp slide deck!

[![Marp CLI](https://raw.githubusercontent.com/marp-team/marp-cli/main/docs/images/marp-cli.gif ' ')][marp cli]

You can use it right now by running `npx @marp-team/marp-cli` if [Node.js](https://nodejs.org/) is installed.

- Export to HTML, PDF, and image
- Watch the change of your Markdown and theme (`--watch`)
- Open preview window for presentation (`--preview`)
- Full-customizable engine based on Marpit framework

Marp had a text editor originally, but you might think that want to write the slide deck with your favorite editor. If you use Vim, you would feel uncomfortable not to be usable Vim style key-binding. From now on, use Marp CLI's watch mode together with original Vim!

And Marp CLI can create really practicable static HTML as like as a presentation mode! It is powered by deep integration with [Bespoke.js](https://github.com/bespokejs/bespoke).

Thanks to [Netlify], [Now], and more hosting services, Marp CLI also brings a efficient Git management for creating slide deck just like [GitPitch]. I've created [an example slide](https://yhatt-marp-cli-example.netlify.com/) managed via [GitHub repository](https://github.com/yhatt/marp-cli-example) as a good starter to help writing your slide deck. Try to use it via "Deploy to Netlify" button on [README](https://github.com/yhatt/marp-cli-example/blob/master/README.md#usage)!

[netlify]: https://www.netlify.com/
[now]: https://zeit.co/now/
[gitpitch]: https://gitpitch.com/

## Marp Web (_tech demo_)

**[Marp Web]** is a Web interface of Marp presentation writer. It allows writing your slide deck as like as a traditional desktop app.

> The current Marp Web is just a tech demo. We are planning to re-implement Marp Web based on well-known framework (like React) for building SPA.

[marp web]: https://web.marp.app/

### Progressive Web Apps

It made [some strong oppositions by users that is using Marp in offline](https://github.com/yhatt/marp/issues/174#issuecomment-294594856) when an idea of migration to web-based app is proposed for keeping maintainability of Marp. It was caused that a thinking of PWA was not general at that time.

And 2 years later, the time has come to use PWA! After the first access to **[https://web.marp.app/][marp web]**, Marp Web would be ready to use in both of online and offline. Online resources to use the web interface would be cached in your browser, and use them when network is offline.

[![Marp Web + Progressive Web Apps](https://raw.githubusercontent.com/marp-team/marp-web/master/desktop-pwa.png ' ')][marp web]

### Use via any devices

By migrating to the web-based app, Marp will be able using in mobile device: Android and iOS. That's sure it's well suited to the tablet device like iPad.

![Marp Web on iPad](https://user-images.githubusercontent.com/3993388/50569518-5305c800-0daa-11e9-8fa4-08053c9b51cd.png ' ')

Marp Web would work also in Chrome OS well. Marp especially has many users in the field of education, and supporting Chrome OS that has large share in its field is meaningful.

### Blazing-fast live preview ⚡️

We think Marp's important feature is a blazing-fast live preview. In the web-based app, realizing the same feature had many difficulties.

In currently published tech-demo, you can try Marp's really fast preview on the web. The preview applies as soon as typing, and it would not block your typing even if you have a large Markdown slides over than 100 pages.

# Integrations

The modulized Marp Core brought Marp integrations for some tools.

## [Marp for VS Code][marp vscode]

Honestly, I don't think to want to make a new editor because there are many great Markdown editors in the world. I had been thinking it would be awesome if Marp could integrate with a something else powerful Markdown editor. And now, Marp can use in [Visual Studio Code](https://code.visualstudio.com/)!

![Marp for VS Code](/assets/marp-for-vs-code.png ' ')

It was realized because VS Code is using the same Markdown engine (markdown-it) as Marpit framework. Of course you can export slides as PDF and HTML easily, powered by [Marp CLI].

[marp vscode]: https://marketplace.visualstudio.com/items?itemName=marp-team.marp-vscode

## [Marp React] &amp; [Marp Vue] (In development)

[marp react]: https://github.com/marp-team/marp-react
[marp vue]: https://github.com/marp-team/marp-vue

Marp's blazing fast live-preview is not only for ours! We provide Marp renderer component into [React][marp react] and [Vue][marp vue]. Both Marp React and Marp Vue have supported the incremental update using framework's virtual DOM, and they are been easy to build your app.

Especially, Marp React would become to the base of the future of [Marp Web].

# Migration plan

## Desktop app ([yhatt/marp](https://github.com/yhatt/marp))

If you are using an old Marp application, **you should migrate to use Marp Next tools.** I NEVER recommend continue to use the old Marp, because _its maintainance has stopped 2 years ago and there is concern about security issues._

In future, the main interface would become to Marp Web. We have bet to PWA technology that has a lot of advantages. The desktop app is planned as "Marp Desktop" but it just may become a wrapper of Web interface.

I would stop publishing the old Marp and archive its repository if Marp Web has grown to become replacable the old Marp.

## Your slide deck

Your Markdown slides written in the old Marp syntax should rewrite to suit to the brand-new Marp ecosystem.

In a new Marp, we have reconsidered Markdown syntax based on feedback to the old Marp app. So, some syntaxs are losing compatibillity.

### Syntax

- In Marp Core, non-whitelisted HTML elements are disabled by default because of security reason. Currently our whitelist includes only `<br>` element. Some Marp Next tools has provided preference to enable HTML, but you should take care for enabling HTML in untrusted Markdown.

### Directives

- Directives would be parsed by YAML parser tuned for Marp (Marpit). Thus spot directive prefix `*` is changed to `_` for keeping YAML syntax.
- `$` prefix no longer required to global directives.
- Slide size still can choose from "16:9" and "4:3", through `size` global directive (provided by Marp Core). If you want to use custom size or you're using Marpit framework, please use [theme CSS](https://marpit.marp.app/theme-css?id=slide-size).
- `page_number` directive is renamed to `paginate`.
- `template` directive is renewed to use `class` directive. It can define HTML class per slides.
- `prerender` directive is removed. It brings user confusing about exported PDF quality.

### Image

- Background image `![bg]()` has no filter applied by default. Try using `![bg opacity]()` if you want.
- The inline image is no longer scalable by percentage `![50%]()`. (It's not supported in Firefox) Instead you can use `width` (`w`) and `height` (`w`) keyword to resize image as like as `![width:300px]()`.
- `![center]()` won't work. It requires changing image to the block element and brings confusion to theme author. You can tweak style if you still want.

```html
<style>
  img[alt~='center'] {
    display: block;
    margin-left: auto;
    margin-right: auto;
  }
</style>
```

# Try Marp Next!

Marp Next just focuses to build the ecosystem for Markdown slide deck with pure open source. We expect to expand Marp productivity together with open source community.

We still have stood at the beginning of the brand-new ecosystem. Are you interested to Marp team and our ecosystem? We welcome to start your contribution! See [our contributing guideline](https://github.com/marp-team/.github/blob/master/CONTRIBUTING.md) and get started!

> PS. [GitHub Sponsors](https://github.com/sponsors/yhatt) is also good contribution if you want to help my working for open source.

```

`/Users/nikola/dev/marp/website/blog/marp-for-vs-code-v1.md`:

```md
---
title: 'Marp for VS Code v1: IntelliSense for Marp directives'
date: 2021-05-20
description: I'm happy to announce Marp for VS Code has reached to the stable release v1! This release includes IntelliSense for Marp directives and getting more affinity with VS Code features to get better writing experience.
author: Yuki Hattori
github: yhatt
image: /og-images/marp-for-vs-code-v1.jpg
---

We are continuing development to make stable Marp tools. And today, I'm happy to announce [Marp for VS Code] has reached to the stable release v1!

Tools of Marp ecosystem are made for potentially covering various situations, and especially Marp for VS Code is made for the daily use for the most of users.

This extension can change the familiar Markdown preview into slides preview during editing Marp Markdown. You can write and edit slides by text rapidly together with checking the appearance of slides, and export into PDF/PPTX easily. [Custom theme support](https://github.com/marp-team/marp-vscode#use-custom-theme-css-shield) is useful to create your own theme with CSS.

In this release, we have added IntelliSense extension for Marp directives and got more affinity with [VS Code] features. It provides better experience as integrated environment to write the presentation.

[vs code]: https://code.visualstudio.com/
[marp for vs code]: https://marketplace.visualstudio.com/items?itemName=marp-team.marp-vscode

<!-- more -->

[**➡️ Go to Visual Studio Marketplace to get Marp for VS Code**][marp for vs code]

# History

[![Marp for VS Code](https://raw.githubusercontent.com/marp-team/marp-vscode/main/docs/screenshot.png ' ')][marp for vs code]

Marp for VS Code has started development since 2019, to replace GUI interface from [the classic Marp app](https://yhatt.github.io/marp). It is focusing to provide better experience for writing Marp presentation.

[We had also thought making another Web app as a primary project at that time](/blog/the-story-of-marp-next#marp-web-tech-demo), but VS Code has drastically grown as time goes by. It is covering Web and mobile devices through [GitHub Codespaces](https://visualstudio.microsoft.com/services/github-codespaces/). Thus, we are still continuing development VS Code extension as an official Marp integration for GUI.

# New features

## IntelliSense for Marp directives 🤓

[Directives](https://marpit.marp.app/directives), the inherited feature from [Marpit framework](https://marpit.marp.app/), is an important syntax to write the deck in Marp.

Our extension is depending on 3 different Marp projects that have unique directives. User had been hard to know all of supported directives because the guidance of them has scattered into each tools.

So we have extended [IntelliSense](https://code.visualstudio.com/docs/editor/intellisense) to cover all of supported Marp directives! Marp for VS Code is now providing powerful editing features for directives: Auto completion, syntax highlight, hover help, and diagnostics.

### Auto completion

Hit `Ctrl` + `Space` within [the front-matter](https://marpit.marp.app/directives?id=front-matter) or [HTML comment](https://marpit.marp.app/directives?id=html-comment) to show the list of directives. You can peek the help of selected directive by hitting `Ctrl` + `Space` again.

![Auto completion](/assets/marp-for-vs-code-v1/auto-completion.png 'We remember all, you may forget them 😛')

I worked hard into refactor of a parser for Marp Markdown to get this improvement. This change would make easier to add new language feature like auto-completion for [the extended image syntax](https://marpit.marp.app/image-syntax) in the future.

### Syntax highlight and hover help

When enabled Marp feature, recognized directives are highlighted by the different color from around. It's useful for finding out meaningless definitions.

And you can peek the help of directive when hovering the cursor.

![Syntax highlight and hover help](/assets/marp-for-vs-code-v1/hover-help.png 'Point at the directive if you were lost 👆')

### Diagnostics

It is accurately not new feature but I'm sure the most of users have not seen because it had used just for migrating outdated syntax.

In this update, we have added some helpful diagnostics for Marp directives. For example, Marp for VS Code can notify not recognized theme name that is specified by `theme` directive.

![Diagnostics](/assets/marp-for-vs-code-v1/diagnostics.png 'Detected diagnostics will be listed in "Problems"')

## Virtual workspace support 🌐

VS Code is still evolving to cover various situations: [Editing remote files](https://code.visualstudio.com/docs/remote/remote-overview), [collaborating with others](https://code.visualstudio.com/learn/collaboration/live-share), and something usefuls provided by [a lot of third-party extension](https://marketplace.visualstudio.com/vscode). Marp for VS Code is also making an effort to cover them as far as possible.

In the recent update, we have improved the export command and custom theme support within a virtual workspace by followed [the call to action from VS Code team](https://code.visualstudio.com/updates/v1_56#_define-whether-your-extension-supports-a-virtual-workspace).

No problem even if you don't know the virtual workspace! In short, Marp features will become to work correctly in various situation.

### Details

Previously an export command had assumed to deal only local files. So the result of command might miss some resources that have not located in local file system.

We are dealing with this by internally serving resources located in a virtual workspace via HTTP while processing of export ([marp-team/marp-vscode#225](https://github.com/marp-team/marp-vscode/pull/225)). By doing this, the result of export command within [a remote repository](https://code.visualstudio.com/updates/v1_56#_remote-repositories-remotehub), a coming feature of VS Code to edit the content of GitHub repository without clone/download, can include resources correctlly.

This behavior is under verifying and may fail to resolve resources in some cases (e.g. [marp-team/marp-vscode#238](https://github.com/marp-team/marp-vscode/issues/238)). We are welcome more feedbacks about the export command in a virtual workspace!

## Workspace Trust 🛡️

[Workspace Trust](https://github.com/microsoft/vscode/issues/106488) is a unified security model for the whole of VS Code. Currently it's an opt-in feature (VS Code 1.56) but it's going to be enabled by default soon. [VS Code team is calling to action into extension authors also for this.](https://code.visualstudio.com/updates/v1_56#_workspace-trust-extension-api)

Based on reflection of [the outdated Marp app](https://yhatt.github.io/marp), Marp team is thinking about users security first. Actually we were passive for supporting a feature that have potentially security concerns (e.g. [marp-team/marp-vscode#123](https://github.com/marp-team/marp-vscode/pull/123)). Making ready for Workspace Trust will become available to contain more advanced features.

Marp for VS Code v1 is supporting Workspace Trust. If the current workspace is not trusted, you can only use basic Marp features (Markdown preview and IntelliSense).

### Restricted features in untrusted workspace

- Export command
- Using custom themes configured in workspace: `markdown.marp.themes`
- Enabling HTML tags in Markdown: `markdown.marp.enableHtml`

# Conclusion

Marp for VS Code is focusing into providing the great experience to write presentation. IntelliSense for Marp directives is a big improvement for that. We are going to continue making an effort to cover update of VS Code.

And Marp team is always thinking about security. Supporting VS Code's Workspace Trust is an important thing to save you from maliciouses.

In addition, a way of thinking about the trusted workspace would open the door to more useful features that were prevented by security concerns: Custom Marp CLI configuration, playing presentation, and so on.

## What's next?

There are no determined things. But supporting Workspace Trust has taken a step toward some advanced features.

We are planning some well-known features in the other presentation software to reduce friction of moving from familiar tools: the sidebar with slide thumbnails ([marp-team/marp#42](https://github.com/marp-team/marp/discussions/42)), presentation button in lower-right, and so on.

![Sidebar in development](/assets/marp-for-vs-code-v1/plan-sidebar.gif 'Sidebar in development')

Enjoy writing presentation with our extension! And join to [our discussion forum](https://github.com/marp-team/marp/discussions) if you want more Marp tips.

[**➡️ Go to Visual Studio Marketplace to get Marp for VS Code**][marp for vs code]

```

`/Users/nikola/dev/marp/website/blog/marpit-v2-marp-core-v2-and-marp-cli-v1.md`:

```md
---
title: Marpit v2, Marp Core v2, and Marp CLI v1
date: 2021-05-06
description: I'm so glad to announce shipping Marpit framework v2, Marp Core v2, and Marp CLI v1! Especially, Marp CLI is getting stable now!
author: Yuki Hattori
github: yhatt
---

[marpit framework]: https://marpit.marp.app/
[marp core]: https://github.com/marp-team/marp-core
[marp cli]: https://github.com/marp-team/marp-cli

I'm so glad to announce shipping [Marpit framework] v2, [Marp Core] v2, and [Marp CLI] v1! Especially, Marp CLI is getting stable now!

They are major update that may be including some breaking changes. However, we have not intended to include any drastic changes. We have recognized well that user hates to break the existing slide.

The biggest reason why bumped major version is ending support for outdated Node.js 10. It has reached to End-of-Life and we are just following that.

Marpit and Marp Core still can use in EOL Node 10, but we are just making a window time for transition. By the security reason, we don't recommend to use outdated Node.js.

<!-- more -->

# Release notes

## [Marpit framework: v2.0.0](https://github.com/marp-team/marpit/releases/tag/v2.0.0)

### Breaking

- Marpit requires Node.js >= 10 to install ([#284](https://github.com/marp-team/marpit/pull/284))

### Fixed

- Reset CSS columns in advanced background ([#283](https://github.com/marp-team/marpit/pull/283))

### Changed

- Upgrade to PostCSS 8 ([#260](https://github.com/marp-team/marpit/issues/260), [#284](https://github.com/marp-team/marpit/pull/284))
- Upgrade Node and dependent packages to the latest version ([#285](https://github.com/marp-team/marpit/pull/285))

### Removed

- Remove deprecated `markdownItPlugins`, the getter of plugin interface for markdown-it ([#286](https://github.com/marp-team/marpit/pull/286))

## [Marp Core: v2.0.0](https://github.com/marp-team/marp-core/releases/tag/v2.0.0)

### Added

- Allow color customization through CSS variables in Gaia and Uncover theme ([#209](https://github.com/marp-team/marp-core/issues/209), [#221](https://github.com/marp-team/marp-core/pull/221))

> May break appearance of existing presentation if you have a slide with custom style.

### Changed

- Upgrade Marpit to [v2.0.0](https://github.com/marp-team/marpit/releases/v2.0.0) ([#220](https://github.com/marp-team/marp-core/pull/220))
- Upgrade Node LTS and dependent packages to the latest version ([#222](https://github.com/marp-team/marp-core/pull/222))

## [Marp CLI: v1.0.0](https://github.com/marp-team/marp-cli/releases/tag/v1.0.0)

### Breaking

- Dropped Node 10 support ([#338](https://github.com/marp-team/marp-cli/pull/338))

### Added

- Build Docker container image for ARM64 ([#328](https://github.com/marp-team/marp-cli/issues/328), [#339](https://github.com/marp-team/marp-cli/pull/339))
- Allow `MARP_USER` env for Docker image to set an explicit UID/GID ([#334](https://github.com/marp-team/marp-cli/pull/334) by [@davebaird](https://github.com/davebaird))
- Test against Node 16 for Windows ([#338](https://github.com/marp-team/marp-cli/pull/338))

### Changed

- Upgrade [Marpit v2.0.0](https://github.com/marp-team/marpit/releases/tag/v2.0.0) and [Marp Core v2.0.0](https://github.com/marp-team/marp-core/releases/tag/v2.0.0) ([#338](https://github.com/marp-team/marp-cli/pull/338))
- Upgrade Node and dependent packages to the latest version ([#338](https://github.com/marp-team/marp-cli/pull/338))

# What's Next?

I've posted about [the unified docs, and future plans for our toolset in the last article](/blog/re-creation-of-marp-website). But it was a mistake! Marp team is still alone and I cannot take full-time working for that, so the most of planned features are delayed. Sorry for late.

For helping us, contribution in [Marp discussion forum](https://github.com/marp-team/marp/discussions) will be good start.

## Marpit framework v3

We have ve already started for working Marpit v3 on [`v3` branch](https://github.com/marp-team/marpit/tree/v3).

It's going to be rewritten fully by TypeScript. We are planning to separate Marp slide specific plugins internally, for improvement of collaboration with other slide renderers. In addition, I want to support async conversion by returning Promise in `render()`.

We also had considered about changing Markdown parser, but we decided not to change. Some Marp users are depending on third party plugins, and it would make a lot of breakings if changed.

# Thanks

Over 5 years have passed from the first release of classic Marp. For keeping maintainability for long time, Marp ecosystem is still aiming to "minimal". And now, Marp has used by projects hosted on [Microsoft](https://github.com/microsoft/lage), [Google](https://github.com/google/applied-machine-learning-intensive), and [Facebook](https://github.com/facebookincubator/cargo-guppy).

In the last year, we opened our [discussion forum](https://github.com/marp-team/marp/discussions) to accept asking and reporting for the whole of Marp toolset. And we have received many feedbacks and contributions from users.

Thanks for our community! Marp will keep a growth with users.

```

`/Users/nikola/dev/marp/website/blog/how-to-make-custom-transition.md`:

```md
---
title: 'Marp CLI: How to make custom transition'
date: 2022-05-28
description: Marp CLI v2.4.0+ and Marp for VS Code v2.5.0+ have a stable support for page transitions with many useful built-in effects. But if you had not satisfied with any effects? Make your effects with CSS!
author: Yuki Hattori
github: yhatt
image: /og-images/how-to-make-custom-transition.jpg
---

[readme]: https://github.com/marp-team/marp-cli/blob/main/docs/bespoke-transitions/README.md
[built-in]: https://github.com/marp-team/marp-cli/blob/main/docs/bespoke-transitions/README.md#built-in-transitions
[view transitions api]: https://www.w3.org/TR/css-view-transitions-1/

**[Marp CLI v2](/blog/202205-ecosystem-update#marp-cli-v2)** has supported [brand-new page transitions for the `bespoke` HTML template](/blog/202205-ecosystem-update#slide-transition-experiment). You can use this stable transition support in either Marp CLI v2.4.0+ or Marp for VS Code v2.5.0+.

Effective transitions will help make a dramatic presentation. Adding a touch of effects to slides is often common in great talks. By viewing HTML slide in the browser that supports [View Transitions API] (Chrome 110+), or Marp CLI with `--preview` option, you can start to use [varied 33 transition effects][built-in] out of the box, by [just a simple definition `transition` directive](https://github.com/marp-team/marp-cli/blob/main/docs/bespoke-transitions/README.md#transition-local-directive).

Built-in transitions should be useful for 90% of Marp users. But what you can do if there are no effects you are satisfied with? Make your effects in CSS! Marp can register your custom animation set declared in CSS as a named transition, and use it in the Markdown slide.

<!-- more -->

### Index

This article will describe the following things:

1. **[The anatomy of a transition](#the-anatomy-of-a-transition)**: How the transition effect will work in Marp
1. **[Declare custom transitions](#declare-custom-transitions)**: How to register custom transitions by CSS
1. **[Helpful tips for making your transition](#tips)**

[See also the official documentation about transitions in Marp CLI.][readme]

_If using [built-in transitions made by us][built-in] was enough, you don't need to read this article._ Please save your time, with keeping enjoying our transitions in your Markdown slide! :)

> In this article, the word "transition" is meaning the slide transition effect in Marp. Please note that it is not meaning [`transition` property in CSS](https://developer.mozilla.org/docs/Web/CSS/CSS_Transitions/Using_CSS_transitions).

# The anatomy of a transition

The first what the custom transition author has to know is "How the page transition effect is realized in a presentation slide".

Let's consider what is happening when the slide page was navigated from 1 to 2. If no transitions were set to the slide, the first page will just disappear, and appear on the second page immediately. If it has a transition effect, a certain time for playing animations will insert between switching pages.

![The anatomy of a transition](/assets/how-to-make-custom-transition/transition-diagram.jpg 'The anatomy of a transition')

An important thing during transition is that 2 slides are presented in the view at the same time like layers. All kinds of effects produce smooth transitions by applying specific animations to one or both slides.

In Marp, the slide page that was shown before transition calls as **"Outgoing slide"**, and the next page to appear after transition calls as **"Incoming slide"**. Slide pages may have an inverse relationship when brought the backward navigation, but the meaning of "incoming" and "outgoing" is always consistent.

If you could figure them out, you probably also grasp that you have to respect the following 2 principles:

- **The outgoing slide** should have **an animation to hide** the slide.
- **The incoming slide** should have **an animation to show** the slide.

If either or both was not respected in a transition effect, it would become a weird transition.

> Marp CLI's `bespoke` template will make two slide layers when navigated, and apply suitable animation keyframes declared in CSS.

# Declare custom transitions

## Simple keyframe declaration

Let's get started with a simple keyframe declaration for [the dissolve effect (also known as the cross-fade effect)](<https://en.wikipedia.org/wiki/Dissolve_(filmmaking)>), to learn how to set custom transition animation. Marp uses [standard syntax for CSS animation `@keyframes`](https://developer.mozilla.org/docs/Web/CSS/@keyframes) to declare transitions.

When applying the dissolve effect to transition principles, you can derive that the effect needs these animations:

- The outgoing slide has an animation to **decrease opacity from 100% to 0%**.
- The incoming slide has an animation to **increase opacity from 0% to 100%**.

There are opposite changes with each other. In this case, you can define animations for both slide layers by one `@keyframes` declaration.

First, declare `@keyframes` at-rule with the conventional name specified by Marp in your Markdown.

```markdown
---
transition: dissolve
style: |
  @keyframes marp-transition-dissolve {
    /* ... */
  }
---

# Slide 1

---

<!-- _class: invert -->

# Slide 2
```

**`marp-transition-xxxxxxxx`** is the rule of animation name to register the transition with a simple declaration. For using declared transition in Marp slide, assign `transition` local directive with the name declared in `xxxxxxxx`.

> This example is using [`style` global directive](https://marpit.marp.app/directives?id=tweak-theme-style) to declare keyframes. Of course, you also can use [the inline `<style>` element](https://marpit.marp.app/theme-css?id=tweak-style-through-markdown) or [custom theme CSS](https://marpit.marp.app/theme-css) to declare.

Well, declare animation details at keyframes. In a simple declaration, you only have to set animation for the outgoing slide. For the incoming slide, Marp will set the animation in the reverse direction automatically.

```css
@keyframes marp-transition-dissolve {
  from {
    opacity: 1;
  }
  to {
    opacity: 0;
  }
}
```

> This example has been declared `from` keyframe for clarity, but you can omit it because `opacity: 1` is a default style.

Did you want more? That's it! Try to test this transition in the HTML slide with the browser that supports [View Transitions API], or [a preview window in Marp CLI](https://github.com/marp-team/marp-cli#preview-window---preview---p).

```bash
npx @marp-team/marp-cli@^2.4.0 --preview ./transition.md
```

You have made the first custom transition!

![autoplay The dissolve effect with timeline diagram](/assets/how-to-make-custom-transition/dissolve-opacity.mp4)

In this article, the example is simplified for teaching how to make a custom transition, and there is a bit of difference from the built-in transition `fade` for getting the same effect. `dissolve` effect is looking good, but there is [a general pitfall about cross fading](https://jakearchibald.com/2021/dom-cross-fade/).

## Split animations into outgoing and incoming

A simple declaration should work in some transition types well, but it's not that all transitions have exactly contrary animations to each other. In reality, different animations for the outgoing slide and incoming slide are required in most cases.

For example, the slide up effect must have these animations:

- The outgoing slide should **move from the viewport to the upper outer**.
- The incoming slide should **move from the lower outer to the viewport**.

So you can declare split animations for each layer rather than declaring a single animation. Set `@keyframes` with the prefix of the target transition: **`marp-outgoing-transition-xxxxxxxx`** and **`marp-incoming-transition-xxxxxxxx`**.

```markdown
---
transition: slide-up
style: |
  @keyframes marp-outgoing-transition-slide-up {
    from { transform: translateY(0%); }
    to { transform: translateY(-100%); }
  }
  @keyframes marp-incoming-transition-slide-up {
    from { transform: translateY(100%); }
    to { transform: translateY(0%); }
  }
---

# Slide 1

---

<!-- _class: invert -->

# Slide 2
```

Unlike the simple transition, there is no auto-reversed animation in the incoming slide. Each animation should define in the right direction.

![The timeline diagram of slide-up transition](/assets/how-to-make-custom-transition/slide-up-translate-y.png 'The timeline diagram of slide-up transition')

## Transition for backward navigation

If you have tested the above slide-up transition example, you may have noticed that is having a move to up also when slide navigation going to back has occurred.

![Wrong direction in slide up transition](/assets/how-to-make-custom-transition/slide-up-wrong-direction.gif ' ')

It brings a wrong user interaction and is not intuitive. You should want to provide the animation for the correct direction when occurred backward navigation.

We are providing several solutions to deal with this.

### `--marp-transition-direction` CSS variable

While playing transition, `--marp-transition-direction` [CSS custom property (as known as CSS variables)](https://developer.mozilla.org/docs/Web/CSS/Using_CSS_custom_properties) will be available in `@keyframes`.

It provides `1` in forwarding navigation, or `-1` in backward navigation. Using [`var(--marp-transition-direction)`](https://developer.mozilla.org/docs/Web/CSS/var) together with [`calc()`](https://developer.mozilla.org/docs/Web/CSS/calc) function would be useful to calculate the position in response to the direction of slide navigation.

<!-- prettier-ignore-start -->

```css
@keyframes marp-outgoing-transition-slide-up {
  from { transform: translateY(0%); }
  to { transform: translateY(calc(var(--marp-transition-direction, 1) * -100%)); }
}
@keyframes marp-incoming-transition-slide-up {
  from { transform: translateY(calc(var(--marp-transition-direction, 1) * 100%)); }
  to { transform: translateY(0%); }
}
```

<!-- prettier-ignore-end -->

And now, the slide-up custom transition is working completely in both directional navigation!

![Slide up transition with correct directions](/assets/how-to-make-custom-transition/slide-up-correct-direction.gif ' ')

> NOTE: Any other CSS variables defined in the context of animation keyframes cannot use in keyframes.

### Set custom animations for backward transition

Alternatively, you also can set more animation keyframes that are specific for backward navigation.

Declare `@keyframes` with the **`backward-` prefix to the custom transition name**, just like as **`marp-transition-backward-xxxxxxxx`**. It is available in both simple keyframes declaration and split keyframes declaration.

<!-- prettier-ignore-start -->

```css
@keyframes marp-incoming-transition-triangle {
  /* Wipe effect from left top */
  from { clip-path: polygon(0% 0%, 0% 0%, 0% 0%); }
  to { clip-path: polygon(0% 0%, 200% 0%, 0% 200%); }
}

@keyframes marp-incoming-transition-backward-triangle {
  /* Wipe effect from right bottom */
  from { clip-path: polygon(100% 100%, 100% 100%, 100% 100%); }
  to { clip-path: polygon(-100% 100%, 100% -100%, 100% 100%); }
}
```

<!-- prettier-ignore-end -->

In backward navigation, each layer will try to use the backward keyframes first, and fallback to the normal keyframes if not declared. To disable unintended fallback in backward animations, set an empty declaration of `@keyframes`.

<!-- prettier-ignore-start -->

```css
@keyframes marp-outgoing-transition-zoom-out {
  from { transform: scale(1); }
  to { transform: scale(0); }
}
@keyframes marp-incoming-transition-zoom-out {
  /* Send the incoming slide layer to back */
  from { z-index: -1; }
  to { z-index: -1; }
}

/* ⬇️ Declare empty keyframes to disable fallback ⬇️ */
@keyframes marp-outgoing-transition-backward-zoom-out {}
@keyframes marp-incoming-transition-backward-zoom-out {
  from { transform: scale(0); }
  to { transform: scale(1); }
}
```

<!-- prettier-ignore-end -->

OK, I've described all about declarations for the custom transition!

# Tips

## Easing function

Each transition has a linear easing by default. You can specify [`animation-timing-function` property within individual keyframes](https://developer.mozilla.org/en-US/docs/Web/CSS/animation-timing-function#:~:text=A%20keyframe%27s%20timing%20function%20is%20applied%20on%20a%20property%2Dby%2Dproperty%20basis%20from%20the%20keyframe%20on%20which%20it%20is%20specified%20until%20the%20next%20keyframe%20specifying%20that%20property%2C%20or%20until%20the%20end%20of%20the%20animation%20if%20there%20is%20no%20subsequent%20keyframe%20specifying%20that%20property) if you want.

> Setting [`animation-timing-function: step-end;`](https://developer.mozilla.org/docs/Web/CSS/animation-timing-function#step-end) to a keyframe can make paused animation until the next keyframe.

## Duration

We have a fixed duration time of `0.5s` as default for every transition. If you want to set a different default duration for your custom transition, please set `--marp-transition-duration` property in the first keyframe (`from` or `0%`).

<!-- prettier-ignore-start -->

```css
@keyframes marp-incoming-transition-gate {
  from {
    /* Set the default duration of the "gate" transition as 1 second. */
    --marp-transition-duration: 1s;

    clip-path: inset(0 50%);
  }
  to { clip-path: inset(0); }
}

@keyframes marp-outgoing-transition-backward-gate {
  from {
    /* You also can set a different default for backward transition as necessary. */
    /* --marp-transition-duration: 1.5s; */

    clip-path: inset(0);
  }
  to { clip-path: inset(0 50%); }
}
@keyframes marp-incoming-transition-backward-gate {
  from { z-index: -1; }
  to { z-index: -1; }
}
```

<!-- prettier-ignore-end -->

The slide author can override the default duration at any time, through the `transition` local directive in Markdown (`<!-- transition: fade 2s -->`).

## Fixed property

If some of the properties required a fixed value while playing transition, try to set the same declaration into `from` (0%) and `to` (100%).

<!-- prettier-ignore-start -->

```css
@keyframes marp-outgoing-transition-pin {
  /* Use fixed transform-origin */
  from {
    transform-origin: top left;
    animation-timing-function: ease-in;
  }
  to {
    transform-origin: top left;
    transform: rotate(90deg);
  }
}

@keyframes marp-incoming-transition-pin {
  /* Send the incoming slide layer to back */
  from { z-index: -1; }
  to { z-index: -1; }
}
```

<!-- prettier-ignore-end -->

## Layer order

[As presented in a diagram earlier](#the-anatomy-of-a-transition), the incoming slide layer always will be stacked on the top of the outgoing slide layer. According to the kind of transition, this order may be not suitable.

A fixed property [`z-index: -1`](https://developer.mozilla.org/docs/Web/CSS/z-index) is helpful to send the incoming slide layer to back.

> A fixed `z-index: 1` to the outgoing slide (send to front) is also getting the same result, but currently setting a positive number to `z-index` may bring animation jank in Chrome.

## Change layer order during a transition

If you want to swap the order of layers during animation, try to animate `z-index` property.

<!-- prettier-ignore-start -->

```css
@keyframes marp-incoming-transition-swap {
  /* Incoming slide will swap from back to front at 50% of animation */
  from { z-index: -1; }
  to { z-index: 0; }

  /* Declarations for moving animation */
  0% { transform: translateX(0); }
  50% { transform: translateX(50%); }
  100% { transform: translateX(0); }
}

@keyframes marp-outgoing-transition-swap {
  0% { transform: translateX(0); }
  50% { transform: translateX(-50%); }
  100% { transform: translateX(0); }
}
```

<!-- prettier-ignore-end -->

`z-index` is always taking an integer value, and interpolated `z-index` value by animation does not take any decimal points too. So animating from `z-index: -1` to `z-index: 0` is exactly meaning to set `-1` at the first half of duration and `0` at the last half, except if using a non-linear easing function.

## Frequently used properties in transition

[There are a lot of animatable CSS properties](https://developer.mozilla.org/docs/Web/CSS/CSS_animated_properties), and the following properties are frequently animated in built-in transitions.

- [`opacity`](https://developer.mozilla.org/docs/Web/CSS/opacity)
- [`transform`](https://developer.mozilla.org/docs/Web/CSS/transform)
- [`filter`](https://developer.mozilla.org/docs/Web/CSS/filter)
- [`clip-path`](https://developer.mozilla.org/docs/Web/CSS/clip-path)
- [`mask-image`](https://developer.mozilla.org/docs/Web/CSS/mask-image) (`-webkit-mask-image`)
- [`box-shadow`](https://developer.mozilla.org/docs/Web/CSS/box-shadow)
- [`z-index`](https://developer.mozilla.org/docs/Web/CSS/z-index)

# Try it!

Transitions for Marp CLI's bespoke template backed by [View Transitions API] in the browser, provides flexibility to design your talk as you like. Custom transition brings out your boundless creativity, without complex JS codings, just declarative definitions in CSS.

We are really looking forward to what creative transition effects our community will create!

Share the custom transition you've made with [Marp community](https://github.com/orgs/marp-team/discussions). You can provide custom theme CSS including a bunch of custom transitions too.

```

`/Users/nikola/dev/marp/website/blog/202205-ecosystem-update.md`:

```md
---
title: 'Ecosystem update: Marp Core v3 & Slide transitions in CLI v2'
date: 2022-05-26
description: Introduce a stable release of Marp Core v3, and updated CLI v2 with an entirely new slide transition experiment.
author: Yuki Hattori
github: yhatt
image: /og-images/202205-ecosystem-update.jpg
---

We are so excited to introduce a stable release of **[Marp Core](https://github.com/marp-team/marp-core) v3**, and **[Marp CLI](https://github.com/marp-team/marp-cli) v2** update with [an entirely new slide transition experiment](#slide-transition-experiment).

- **[Marp Core v3](#marp-core-v3)**: MathJax rendering as default, updated `default` theme, and new components for auto-scaling.
- **[Marp CLI v2](#marp-cli-v2)**: Bundled core v3, and [brand-new slide transition experiment](#slide-transition-experiment) with 33 built-in effects + CSS custom transitions.

<!-- more -->

# Marp Core v3

[We had released Marp Core v3.0.0 as a release candidate in November 2021.](https://github.com/marp-team/marp-core/releases/tag/v3.0.0) For a half year, it had been available in the `next` tag as an opt-in engine of Marp CLI, and had accepted feedback from the community.

This month [v3.2.0](https://github.com/marp-team/marp-core/releases/tag/v3.2.0) has become a stable release, and **we are starting work to make v3 core the default in downstream Marp tools gradually.**

An updated Marp Core v3 has some major changes, but we also have worked to keep backward compatibility in many existing slides. Most slide authors should not be concerned about regressions as long as your tweaks to the slide theme are not complicated.

If you are a theme author, you may have to modify some of the styles. This update includes a brand-new auto scaling component, the change of `default` theme caused by the update of [`github-markdown-css`](https://github.com/sindresorhus/github-markdown-css), and so on.

Even so, you should not too worry: We worked to v3 core to reduce friction between Marp's CSS and common CSS, so I think the complex part of our theming system (e.g. styling auto-scaled element) must be easier to understand than v2.

## Notable changes

### Drop support for End-of-Life Node.js

First, Marp Core v3 has dropped support for end-of-life Node.js 10.

We have supported EoL Node.js v12 yet, but continuous support may not guarantee depending on the support status of dependency modules. We recommend following up on [the active LTS Node.js](https://nodejs.org/).

> Check out https://endoflife.date/nodejs to know which version of Node.js is EoL.

### MathJax is a default typesetting library for math

[katex]: https://katex.org/
[mathjax]: https://www.mathjax.org/

Marp Core v3 has changed the default library for rendering math, from [KaTeX] to [MathJax].

Marp had used [KaTeX] as a default library for long years for taking better performance. But currently, this opinion has become the past thinking with the advent of MathJax 3. [See this interesting insight.](https://groups.google.com/g/mathjax-users/c/aboJLMb50uQ/m/Y77FexF_AwAJ)

And some incompatibilities of KaTeX with Marp Core's auto scaling feature that are hard to fix had given us a headache. ([marp-team/marp-core#159](https://github.com/marp-team/marp-core/issues/159), [marp-team/marp-core#236](https://github.com/marp-team/marp-core/issues/236))

MathJax implementation in Marp Core has more reliable rendering than KaTeX. In addition, it also has more TeX function supports, and no network is required to show.

Now a lot of Markdown flavors have adopted MathJax for math typesetting (e.g. [GitHub](https://github.blog/2022-05-19-math-support-in-markdown/)), and we expect Marp Markdown would get higher compatibility in several Markdown services.

#### `math` global directive

If your Markdown is not yet ready to migrate math typesettings into MathJax, you can continue to use KaTeX as a math typesetting library by setting [`math` global directive](https://github.com/marp-team/marp-core#math-global-directive) as `katex`.

```markdown
---
math: katex
---

Continue to use KaTeX: $ax^2+bc+c$
```

We have no plans to remove KaTeX integration for a while. So you can keep rendering math with KaTeX if you're using KaTeX specific syntaxes or met rendering performance issues in MathJax.

> For smooth migration of exist slides to v3, Marp for VS Code is [annotating to math use without `math` global directive](https://github.com/marp-team/marp-vscode#diagnostics) since a year ago.

### Renewed auto-scaling component

Marp Core has a tiny runtime script to activate element auto-scaling for a code block, math block, and [fitting header `# <!--fit--> header`](https://github.com/marp-team/marp-core#fitting-header). v3 has updated auto scaling logic into [Web Components](https://developer.mozilla.org/docs/Web/Web_Components) based, to improve output lucidity and compatibility with some CSS selectors.

This update does not change the actual auto-scaling behavior from v2, so most Markdown slide authors should not need to take care of that. But if you have a custom theme that was styled to auto-scaling elements, you should review and modify CSS declarations in your theme to match with v3.

Please refer to the pull request **[marp-team/marp-core#263](https://github.com/marp-team/marp-core/pull/263)** for details of auto-scaling components.

### Updated `default` theme

To provide a familiar Markdown style to users as default, Marp Core `default` theme is based on [GitHub's Markdown CSS](https://github.com/sindresorhus/github-markdown-css).

The latest Marp Core has included the following updates about `default` theme:

- Updated color schemes based on the latest [github-markdown-css v5](https://github.com/sindresorhus/github-markdown-css)
- Match colors for code highlight with GitHub style
- Allow color customization through CSS variables ([See theme docs](https://github.com/marp-team/marp-core/tree/main/themes#custom-color-css-variables))

````markdown:marp
<!-- paginate: true -->
<style>:root { font-size: 40px; }</style>

# This is a new `default` theme

```markdown
<!-- theme: default -->

# This is a new `default` theme
```

---

<!-- class: invert -->

# Updated `invert` color scheme

based on GitHub dark mode

```markdown
<!-- class: invert -->
```

````

### URL without HTTP(S) scheme does no longer auto-linkify

Marp Core up to v2 had detected URL-like strings and converted them to hyperlinks automatically. However, that was too fuzzy and often brought linkify in not intended words, such as "[Amazon.com](https://amazon.com/)" and "[ML.NET](https://dotnet.microsoft.com/apps/machinelearning-ai/ml-dotnet)".

But there are no more fuzzy links in v3! Now auto link feature requires the URL string with `https://` or `http://` scheme.

Please make a Markdown link `[Amazon.com](https://amazon.com/)` explicitly if you want the hyperlink in previously auto-linked words.

# Marp CLI v2

According to the time to become core v3 stable, we also worked on **[a major update of Marp CLI](https://github.com/marp-team/marp-cli/releases/tag/v2.0.0)** to bundle a new core.

There are no major changes in the general use of Marp CLI, and I believe your CLI workflow would never break by this updation in most cases.

So what feature is a "major" update of CLI? [_Perhaps you may have interested in a hidden gem..._ 💎](#slide-transition-experiment)

## Notable changes

### Required Node.js v14 and later

The new release of Marp CLI is required **the latest Node.js v14 and later**, because depending modules such as Puppeteer (for PDF/PPTX generation) were dropped support for EoL Node.js versions v12 and older.

### Bundled Marp Core v3

As described earlier, Marp CLI v2 has bundled an updated Marp Core v3.2.0 as a core engine.

```bash
$ marp --version
@marp-team/marp-cli v2.0.0 (w/ @marp-team/marp-core v3.2.0)
```

###### Continue to use v2 core in Marp CLI

We recommend getting ready for using the updated v3 core, but Marp CLI also can stick to the v2 core by installing `@marp-team/marp-core@^2` to your project individually.

```bash
npm i --save-dev @marp-team/marp-cli @marp-team/marp-core@^2
npx marp ./your-markdown.md
```

It's useful when your Markdown slide files are not ready for v3 core. But please keep in mind we would hardly provide more updates to v2 core, and **continuous use may bring a risk of unpatched security issues.**

# Slide transitions

A really loving part of this CLI update for me is **[a brand-new slide transition in `bespoke` HTML template.](https://github.com/marp-team/marp-cli/issues/447)**

We had started testing experimental slide transition effects since [Marp CLI v1.4.0](https://github.com/marp-team/marp-cli/releases/tag/v1.4.0) (Aug 2021). `--bespoke.transition` CLI option had been working well, but not so practical compared to the common presentation tools.

As a result of catching up on the new spec of [View Transitions API proposal][view transitions api] in Marp CLI v2, I'm so excited to provide powerful transition features that are in no other Markdown slide tools, such as CSS custom transition effects and morphing animations!

[view transitions api]: https://www.w3.org/TR/css-view-transitions-1/

> The slide transitions feature has made stable in v2.4.0. You can dive into all about of transitions at [the documentation of Marp CLI transitions][transition-docs].

[transition-docs]: https://github.com/marp-team/marp-cli/blob/main/docs/bespoke-transitions/README.md

## Quick look

![Marp CLI transition showcase poster=/assets/202205-ecosystem-update/transition-showcase-poster.jpg controls](https://user-images.githubusercontent.com/3993388/169697466-283dd2f2-b6e5-4b33-86d4-b10cc0a6c3e9.mp4)

- **[33 built-in transitions](https://github.com/marp-team/marp-cli/blob/main/docs/bespoke-transitions/README.md#built-in-transitions)**: Marp CLI provides a lot of transition effects out of the box.
- **[Define custom transitions via CSS](https://github.com/marp-team/marp-cli/blob/main/docs/bespoke-transitions/README.md#custom-transitions)**: Markdown author and theme designer can define the custom transition through `@keyframes` declaration in CSS.
- **[Morphing animations](https://github.com/marp-team/marp-cli/blob/main/docs/bespoke-transitions/README.md#morphing-animations)**: [`view-transition-name` CSS property](https://www.w3.org/TR/css-view-transitions-1/#view-transition-name-prop) supplied by View Transition API helps to make morphing animation while transition.

## Usage

The slide transitions in HTML output can opt in and out through `--bespoke.transition` CLI option. _It is only working in the browser that supports [View Transitions API], such as Chrome/Chromium 110 and later._

The `--preview` CLI option is helpful see transition effects surely. Try this in Marp CLI v2.4.0+ to open a preview window for the transition showcase:

```bash
curl -o ./showcase.md https://gist.githubusercontent.com/yhatt/d9e86ee53eb8816aaf9c996e773b6f82/raw/transition-showcase.md
marp --preview ./showcase.md
```

## Showcase

You can see online demo slides about Marp CLI brand new transitions! See them in the browser that supports [View Transitions API].

- **[Marp CLI page transition showcase](https://marp-cli-page-transitions.glitch.me/)**: The showcase of built-in transitions
- **[Custom transitions example](https://marp-cli-page-transitions.glitch.me/custom.html)**: Some examples and ideas about custom transitions
- **[Transition with morphing animation](https://marp-cli-page-transitions.glitch.me/morph.html)**: An example of morphing animation powered by [View Transitions API].

## `transition` local directive

You can set and change the kind of transition through `transition` local directive.

```markdown
---
transition: fade
---

Fade transition with 0.5s duration

---

<!-- transition: cover 1s -->

Changed the kind of transition to `cover` with 1s duration

---

<!-- _transition: none -->

Disabled transition for this slide

---

Got back to cover transition
```

Each transition has a default 0.5s duration, but you can also set custom duration by space-separated value such as `<!-- transition: fade 1s -->`.

## Custom transition

The custom transition can define through just a few conventional [`@keyframes` at-rules](https://developer.mozilla.org/docs/Web/CSS/@keyframes) within the inline `<style>` element or custom theme CSS.

<!-- prettier-ignore-start -->

```css
/* Simple definition: "dissolve" custom transition */
@keyframes marp-transition-dissolve {
  from { opacity: 1; }
  to { opacity: 0; }
}

/* Splitted definitions: "triangle" custom transition */
@keyframes marp-incoming-transition-triangle {
  from { clip-path: polygon(0% 0%, 0% 0%, 0% 0%); }
  to { clip-path: polygon(0% 0%, 200% 0%, 0% 200%); }
}
@keyframes marp-incoming-transition-backward-triangle {
  from { clip-path: polygon(100% 100%, 100% 100%, 100% 100%); }
  to { clip-path: polygon(-100% 100%, 100% -100%, 100% 100%); }
}

/* With backward animations: Overloading "zoom" transition */
@keyframes marp-incoming-transition-zoom {
  from { transform: scale(0); }
  to { transform: scale(1); }
}
@keyframes marp-outgoing-transition-backward-zoom {
  from { transform: scale(1); }
  to { transform: scale(0); }
}
@keyframes marp-incoming-transition-backward-zoom {
  /* Define empty keyframes to disable fallback into incoming animation */
}
```

<!-- prettier-ignore-end -->

It only has a relatively simple definition(s) but great flexibility, and brings out boundless creativity of CSS animation! 🤩

**[👉 Marp CLI: How to make custom transition](/blog/how-to-make-custom-transition)**

We are really looking forward to what creative transition effects our community will create!

## Morphing animations

Thanks to the browser's [View Transitions API], we can apply morphing animations during a transition effect. This is similar to PowerPoint Morph and Keynote Magic Move.

Just sprinkle a few CSS properties!

![Morphing animations](https://raw.githubusercontent.com/marp-team/marp-cli/main/docs/bespoke-transitions/images/morphing-animation.gif ' ')

```markdown
---
theme: gaia
transition: fade
style: |
  /* ⬇️ Mark the image of "1" in every pages as morphable image named as "one" ⬇️ */
  img[alt="1"] {
    view-transition-name: one;
    contain: layout;
  }

  /* Generic image styling for number icons */
  img:is([alt="1"], [alt="2"], [alt="3"]) {
    height: 64px;
    position: relative;
    top: -0.1em;
    vertical-align: middle;
    width: 64px;
  }
---

# Today's topics

- ![1](https://icongr.am/material/numeric-1-circle.svg?color=666666) Introduction
- ![2](https://icongr.am/material/numeric-2-circle.svg?color=666666) Features
- ![3](https://icongr.am/material/numeric-3-circle.svg?color=666666) Conclusion

---

<!-- _class: lead -->

![1 w:256 h:256](https://icongr.am/material/numeric-1-circle.svg?color=ff9900)

# Introduction

---

# ![1](https://icongr.am/material/numeric-1-circle.svg?color=666666) Introduction

Marp is an open-sourced Markdown presentation ecosystem.
```

**[👉 See details at the documentation about transitions on Marp CLI repository...](https://github.com/marp-team/marp-cli/blob/main/docs/bespoke-transitions/README.md#morphing-animations)**

# Deprecations

Finally, we have to mention that the latest update has a deprecated Markdown syntax in the Marp ecosystem. It is still can use for now with deprecation warnings and will be obsolete in future Marp tools.

> We have planned to work on [an auto-fixable diagnostic for VS Code extension](https://github.com/marp-team/marp-vscode#diagnostics), to make it easier to update the use of deprecated syntaxes.

### Shorthand for setting colors (Marpit framework)

[Marpit framework](https://marpit.marp.app/) had been provided the color setting shorthand through Markdown image syntax, such as `![](red)` and `![bg](yellow)`. This syntax had been allowed to set a corresponding color style like `color: red` and `background-color: yellow` to only a current slide page.

These are rarely used in reality, and now we have considered as harmful from the point of view of Markdown (CommonMark) compatibility.

Marpit framework has already provided [`color` / `backgroundColor` local directives](https://marpit.marp.app/directives?id=backgrounds), and setting [scoped local directives](https://marpit.marp.app/directives?id=apply-to-a-single-page-spot-directives) to the slide will bring the same result.

If you are using these shorthands for setting colors, please replace them with the alternative scoped local directive.

|  Shorthands  |        Should replace to         |
| :----------: | :------------------------------: |
|  `![](red)`  |      `<!-- _color: red -->`      |
| `![bg](red)` | `<!-- _backgroundColor: red -->` |

> _Track the state of progress at [marp-team/marpit#331](https://github.com/marp-team/marpit/issues/331)._

# Community

Join the Marp community! Our [GitHub Discussions](https://github.com/orgs/marp-team/discussions) is a community forum that gathered discussions all about Marp, and allows you to connect with Marp team and other Marp users. Of course, we welcome your feedback for this ecosystem update too. 😀

- [**Go to GitHub Discussions**](https://github.com/orgs/marp-team/discussions)
- [The support guideline of Marp project](https://github.com/marp-team/.github/blob/master/SUPPORT.md)

<!--
# Titbit

Marpit framework is 5th year and I feel that is beginning to gather a few of dust. Therefore I'm trying to design a new polished engine, as a personal weekend experiment toward the next core v4.

Currently I don't want you too to count on it. I'm just working on for getting a long-lived ecosystem with modern CSS rules :)
-->

```

`/Users/nikola/dev/marp/website/components/top/Hero.tsx`:

```tsx
import Head from 'next/head'
import { Button } from 'components/Button'
import Marp from 'public/assets/marp.svg'

const heroBg = '/assets/hero-background.svg' as const

export const Hero = () => (
  <>
    <Head>
      <link rel="preload" href={heroBg} as="image" />
    </Head>
    <section className="border-b py-16 px-4 md:py-24 md:tracking-wider">
      <h1 className="font-rounded text-center font-bold sm:text-xl md:text-2xl">
        <Marp className="mx-auto mb-5 h-auto w-4/5 max-w-xl p-3" />
        <span className="sr-only">Marp:</span>
        Markdown Presentation Ecosystem
      </h1>
      <p className="mt-10 text-center">
        <Button
          href="#get-started"
          color="primary"
          className="text-xl md:text-2xl"
        >
          Get started!
        </Button>
      </p>
      <p className="mt-5 text-center">
        <Button
          href="https://github.com/marp-team/marp"
          target="_blank"
          rel="noopener noreferrer"
          className="text-sm md:text-base"
          color="primary"
          outline
        >
          Find Marp tools on GitHub!
        </Button>
      </p>
      <style jsx>{`
        section {
          background: #fcfcfc url('${heroBg}') no-repeat right center;
          background-size: cover;
        }
      `}</style>
    </section>
  </>
)

```

`/Users/nikola/dev/marp/website/components/top/Features.tsx`:

```tsx
import {
  CodeSquareIcon,
  FileIcon,
  HeartFillIcon,
  MarkdownIcon,
  PackageIcon,
  PaintbrushIcon,
  PlugIcon,
} from '@primer/octicons-react'
import type { ReactElement } from 'react'

type CardProps = React.PropsWithChildren<{
  name: string
  icon: string | ReactElement
  index: number
}>

const Card: React.FC<CardProps> = ({ children, name, icon, index }) => {
  let cardIcon = icon

  if (typeof icon === 'string') {
    cardIcon = <img src={icon} alt={name} width={48} height={48} />
  }

  return (
    <section className="card">
      <div>
        <div className="card-icon">{cardIcon}</div>
        <h2 className="text-gradient my-4 text-center text-2xl font-semibold">
          {name}
        </h2>
        <p className="text-sm lg:text-base">{children}</p>
      </div>
      <style jsx>{`
        .card {
          @apply relative z-10 mx-4 my-8 mb-0 flex items-center justify-center rounded-lg bg-white p-6 shadow-lg;

          grid-column: 1;
        }

        .card-icon {
          @apply my-2 text-center text-gray-700;
        }

        .card-icon :global(svg),
        .card-icon :global(img) {
          @apply inline h-12 w-12 lg:h-16 lg:w-16;
        }

        @screen md {
          .card {
            grid-row: ${index + 1} / span 2;
          }

          .card:first-child {
            @apply mt-0;
          }

          .card:nth-of-type(even) {
            grid-column: 2;
          }
        }
      `}</style>
    </section>
  )
}

const cards = [
  ({ index }) => (
    <Card
      index={index}
      name="Based on CommonMark"
      icon={<MarkdownIcon verticalAlign="top" />}
    >
      If you know how to write a document with Markdown, you already know how to
      write a Marp slide deck. Marp&apos;s format is based on{' '}
      <a
        href="https://commonmark.org/"
        target="_blank"
        rel="noopener noreferrer"
      >
        CommonMark
      </a>
      , a consistent Markdown specification. The only important difference is{' '}
      <a
        href="https://marpit.marp.app/markdown"
        rel="noopener noreferrer"
        target="_blank"
      >
        a ruler <code>---</code> for splitting pages.
      </a>
    </Card>
  ),
  ({ index }) => (
    <Card
      index={index}
      name="Directives and extended syntax"
      icon={<CodeSquareIcon verticalAlign="top" />}
    >
      Sometimes simple text content isn&apos;t enough to emphasize your voice,
      so Marp supports a variety of{' '}
      <a
        href="https://marpit.marp.app/directives"
        rel="noopener noreferrer"
        target="_blank"
      >
        directives
      </a>{' '}
      and extended syntax (
      <a
        href="https://marpit.marp.app/image-syntax"
        rel="noopener noreferrer"
        target="_blank"
      >
        image syntax
      </a>
      ,{' '}
      <a
        href="https://github.com/marp-team/marp-core#math-typesetting"
        rel="noopener noreferrer"
        target="_blank"
      >
        math typesetting
      </a>
      ,{' '}
      <a
        href="https://github.com/marp-team/marp-core#auto-scaling-features"
        rel="noopener noreferrer"
        target="_blank"
      >
        auto-scaling
      </a>
      , etc...) to create beautiful slides.
    </Card>
  ),
  ({ index }) => (
    <Card
      index={index}
      name="Built-in themes and CSS theming"
      icon={<PaintbrushIcon verticalAlign="top" />}
    >
      <a
        href="https://github.com/marp-team/marp-core/"
        rel="noopener noreferrer"
        target="_blank"
      >
        Our core engine
      </a>{' '}
      has{' '}
      <a
        href="https://github.com/marp-team/marp-core/tree/main/themes"
        rel="noopener noreferrer"
        target="_blank"
      >
        3 built-in themes called <code>default</code>, <code>gaia</code>, and{' '}
        <code>uncover</code>
      </a>
      , to tell your story beautifully. If you&apos;d rather customize your
      design, you can use Marp to{' '}
      <a
        href="https://marpit.marp.app/theme-css?id=tweak-style-through-markdown"
        rel="noopener noreferrer"
        target="_blank"
      >
        tweak styles with Markdown
      </a>
      , or{' '}
      <a
        href="https://marpit.marp.app/theme-css"
        rel="noopener noreferrer"
        target="_blank"
      >
        create your own Marp theme with plain CSS
      </a>
      .
    </Card>
  ),
  ({ index }) => (
    <Card
      index={index}
      name="Export to HTML, PDF, and PowerPoint"
      icon={<FileIcon verticalAlign="top" />}
    >
      Have you finished writing? It&apos;s time to share your deck! Marp can
      convert Markdown into presentation-ready HTML, PDF and PowerPoint files
      directly! (Powered by{' '}
      <a
        href="https://www.google.com/chrome/"
        rel="noopener noreferrer"
        target="_blank"
      >
        Google Chrome
      </a>{' '}
      /{' '}
      <a
        href="https://www.chromium.org/Home"
        rel="noopener noreferrer"
        target="_blank"
      >
        Chromium
      </a>
      )
    </Card>
  ),
  ({ index }) => (
    <Card
      index={index}
      name="Marp family: The official toolset"
      icon={<PackageIcon verticalAlign="top" />}
    >
      The Marp ecosystem contains a rich toolset to assist your work.{' '}
      <a
        href="https://marketplace.visualstudio.com/items?itemName=marp-team.marp-vscode"
        rel="noopener noreferrer"
        target="_blank"
      >
        <b>Marp for VS Code</b>
      </a>{' '}
      is an extension that allows you to edit and preview slide Markdown and
      custom theming within VS Code.{' '}
      <a
        href="https://github.com/marp-team/marp-cli/"
        rel="noopener noreferrer"
        target="_blank"
      >
        <b>Marp CLI</b>
      </a>{' '}
      is a command line tool allows you to convert Markdown with a simple CLI
      interface.{' '}
      <a
        href="https://github.com/marp-team/marp/"
        rel="noopener noreferrer"
        target="_blank"
      >
        ... and much more!
      </a>
    </Card>
  ),
  ({ index }) => (
    <Card
      index={index}
      name="Pluggable architecture"
      icon={<PlugIcon verticalAlign="top" />}
    >
      As a matter of fact,{' '}
      <em>Marp is essentially just a converter for Markdown.</em> The Marp
      ecosystem is built on{' '}
      <a
        href="https://marpit.marp.app"
        rel="noopener noreferrer"
        target="_blank"
      >
        <b>the Marpit framework</b>
      </a>
      , a skinny framework for creating HTML/CSS slide decks. It has a pluggable
      architecture and any developer can{' '}
      <a
        href="https://marpit.marp.app/usage?id=extend-marpit-by-plugins"
        rel="noopener noreferrer"
        target="_blank"
      >
        extend features via plugins
      </a>
      .
    </Card>
  ),
  ({ index }) => (
    <Card
      index={index}
      name="Fully open-source"
      icon={<HeartFillIcon verticalAlign="top" />}
    >
      The Marp team loves open source! All tools and related libraries are built
      by{' '}
      <a
        href="https://github.com/marp-team"
        rel="noopener noreferrer"
        target="_blank"
      >
        the Marp team
      </a>{' '}
      and are MIT-licensed.
    </Card>
  ),
]

export const Features = () => (
  <div className="features">
    <div className="features-grid container">
      {cards.map((Card, i) => (
        <Card index={i} key={i} />
      ))}
    </div>
    <style jsx>{`
      .features {
        @apply relative py-5;
      }

      .features::before {
        @apply absolute inset-0 block;

        background-image: var(--noise-image),
          linear-gradient(
            -8deg,
            rgba(120, 197, 233, 0),
            rgba(120, 197, 233, 0) 50%,
            rgba(120, 197, 233, 0.5)
          );
        clip-path: polygon(0 15vw, 100% 0, 100% 100%, 0 100%);
        content: '';
      }

      .features-grid {
        @apply mx-auto grid px-4;

        grid-template-columns: 1fr;
        grid-template-rows: repeat(${cards.length + 1}, auto);
      }

      @screen md {
        .features-grid {
          grid-template-columns: 1fr 1fr;
        }
      }
    `}</style>
  </div>
)

```

`/Users/nikola/dev/marp/website/components/top/Description.tsx`:

```tsx
import { ChevronDownIcon } from '@primer/octicons-react'
import classNames from 'classnames'
import { useState } from 'react'
import { Button } from 'components/Button'
import { CodeBlock } from 'components/CodeBlock'
import { Marp, RenderedMarp } from 'components/Marp'

export type DescriptionProps = {
  example: RenderedMarp
}

export const Description = ({ example }: DescriptionProps) => {
  const [showExample, setShowExample] = useState(false)

  return (
    <section className="container mx-auto py-16">
      <h2 className="text-gradient mx-auto w-5/6 text-center text-3xl font-bold md:text-4xl">
        Create beautiful slide decks using an intuitive Markdown experience
      </h2>
      <p className="mx-auto mt-8 w-5/6 md:text-lg lg:w-2/3">
        Marp (also known as the Markdown Presentation Ecosystem) provides an
        intuitive experience for creating beautiful slide decks. You only have
        to focus on writing your story in a Markdown document.
      </p>
      <figure className="m-8 mb-0 text-center">
        <Marp
          rendered={example}
          page={1}
          className="inline-block w-full max-w-sm"
        />
        <Marp
          rendered={example}
          page={2}
          className="mt-5 inline-block w-full max-w-sm lg:ml-5 lg:mt-0"
        />
        <figcaption className="mt-5 text-sm text-gray-700">
          The slides above are from generated directly from{' '}
          <a href="https://github.com/marp-team/marp-core">Marp Core</a>
        </figcaption>
      </figure>
      <p className="show-example-section">
        <Button
          className="show-example-btn"
          onClick={() => setShowExample((v) => !v)}
          aria-expanded={showExample}
        >
          {showExample ? 'Hide' : 'Show'} Markdown example...
          <ChevronDownIcon
            className={classNames(
              'show-example-btn-chevron',
              showExample && 'show'
            )}
          />
        </Button>
      </p>
      <div
        aria-hidden={!showExample}
        className="overflow-hidden transition-all duration-300"
        style={{ maxHeight: showExample ? '1000px' : '0' }}
      >
        <CodeBlock
          language="markdown"
          lineNumber
          className="mx-auto mt-5 w-5/6 xl:w-2/3"
          copyButton={showExample}
        >
          {example.markdown}
        </CodeBlock>
      </div>
      <style jsx>{`
        .show-example-section {
          @apply mx-auto mt-8 w-5/6 text-center;
        }
        .show-example-section :global(.show-example-btn) {
          @apply text-sm;
        }
        .show-example-section :global(.show-example-btn-chevron) {
          @apply ml-1 h-4 w-4 transform transition-transform duration-300 md:-my-1 md:h-6 md:w-6;
        }
        .show-example-section :global(.show-example-btn-chevron:not(.show)) {
          @apply relative;

          top: -1px;
        }
        .show-example-section :global(.show-example-btn-chevron.show) {
          @apply -rotate-180;
        }

        @screen md {
          .show-example-section :global(.show-example-btn-chevron:not(.show)) {
            top: -2px;
          }
        }
      `}</style>
    </section>
  )
}

```

`/Users/nikola/dev/marp/website/components/top/GetStarted.tsx`:

```tsx
import classNames from 'classnames'
import { Button } from 'components/Button'

type CardProps = React.PropsWithChildren<{
  badge?: string
  className?: string
  description: string
  href: string
  name: string
  screenShot?: string
  ssWidth?: number
  ssHeight?: number
  summary: string
}>

const Card: React.FC<CardProps> = ({
  badge,
  children,
  className,
  description,
  href,
  name,
  screenShot: screenshot,
  ssWidth,
  ssHeight,
  summary,
}) => (
  <section className={classNames('card', className, { screenshot })}>
    <a
      href={href}
      target="_blank"
      rel="noopener noreferrer"
      className="custom-anchor card-link"
    >
      <h4 className="text-gradient inline-block pr-3 pb-1 text-xl font-bold sm:text-2xl md:text-3xl">
        {name}
      </h4>
      {badge && (
        <img
          src={badge}
          alt=""
          className="inline rounded-sm align-text-top sm:align-baseline"
          loading="lazy"
        />
      )}
      <p className="pt-1 text-sm leading-tight text-gray-700">{summary}</p>
    </a>
    {screenshot && (
      <figure>
        <img
          src={screenshot}
          alt={name}
          loading="lazy"
          width={ssWidth}
          height={ssHeight}
        />
      </figure>
    )}
    <p className="mx-5 lg:my-3">{description}</p>
    <p className="mx-5 my-4 text-sm">{children}</p>
    <style jsx>{`
      .card {
        @apply text-foreground relative my-8 grid overflow-hidden rounded-lg bg-white p-2 shadow-xl;

        grid-template-columns: 1fr;
      }
      .card::before {
        @apply absolute right-0 h-40 w-40 transform bg-contain bg-center bg-no-repeat opacity-25;

        content: '';
        top: -2rem;
        transform: rotate(-15deg);
      }
      .card.vscode::before {
        background-image: url('https://icongr.am/simple/visualstudiocode.svg?color=67b8e3');
      }
      .card.cli::before {
        background-image: url('https://icongr.am/octicons/terminal.svg?color=67b8e3');
      }
      .card.core::before {
        background-image: url('/assets/marp-logo.svg');
      }
      .card.marpit::before {
        background-image: url('/assets/marpit.svg');
      }
      .card > * {
        @apply relative col-start-1 col-end-1;
      }
      .card > figure {
        @apply mx-auto flex items-center justify-center p-4;
      }
      .card > figure > img {
        @apply max-w-full;

        width: 28rem;
      }

      .card-link {
        @apply relative z-10 block rounded p-5 transition-all duration-150;
      }
      .card-link:hover,
      .card-link:focus {
        @apply shadow;

        background-color: rgba(255, 255, 255, 0.5);
      }
      .card-link:hover:active,
      .card-link:focus {
        @apply duration-0 outline-none ring-1 ring-white ring-offset-2;
      }

      @screen lg {
        .card.screenshot {
          grid-template-columns: 3fr 2fr;
        }
        .card > figure {
          @apply col-start-2 col-end-2 h-full w-full object-contain px-6 py-0;

          grid-row: 1 / span 9999;
        }
        .card::before {
          @apply h-64 w-64;

          top: -4rem;
        }
      }

      @screen xl {
        .card {
          @apply mx-auto w-5/6;
        }
      }
    `}</style>
  </section>
)

export const GetStarted = () => (
  <>
    <div id="get-started" className="get-started flow-root">
      <section className="container mx-auto py-10 px-8 lg:px-16">
        <h3 className="text-center text-2xl font-bold sm:text-3xl">
          <mark>Tools and integrations</mark>
        </h3>
        <Card
          description="Enhance VS Code's Markdown preview pane to support writing your beautiful presentations. You can preview the slide deck output as soon as you edit its Markdown."
          name="Marp for VS Code"
          summary="Create slide decks written in Marp Markdown right in VS Code"
          badge="https://img.shields.io/visual-studio-marketplace/v/marp-team.marp-vscode.svg?style=flat-square&amp;label=&amp;colorB=0288d1"
          href="https://marketplace.visualstudio.com/items?itemName=marp-team.marp-vscode"
          screenShot="/assets/marp-for-vs-code.png"
          ssWidth={1946}
          ssHeight={1424}
          className="vscode"
        >
          <Button
            color="primary"
            className="mr-2 mb-2"
            href="https://marketplace.visualstudio.com/items?itemName=marp-team.marp-vscode"
            target="_blank"
            rel="noopener noreferrer"
          >
            VS Marketplace
          </Button>
          <Button
            outline
            className="mr-2 mb-2"
            href="https://github.com/marp-team/marp-vscode"
            target="_blank"
            rel="noopener noreferrer"
          >
            GitHub
          </Button>
        </Card>
        <Card
          description="The Marp CLI is the swiss army knife of the Marp ecosystem. Convert your Markdown into various formats, watch changes, launch server for on-demand conversion, and customize the core engine."
          name="Marp CLI"
          summary="A CLI interface for Marp and Marpit based converters"
          badge="https://img.shields.io/npm/v/@marp-team/marp-cli.svg?style=flat-square&amp;label=&amp;colorB=0288d1"
          href="https://github.com/marp-team/marp-cli"
          screenShot="/assets/marp-cli.png"
          ssWidth={1400}
          ssHeight={800}
          className="cli"
        >
          <Button
            color="primary"
            className="mr-2 mb-2"
            href="https://github.com/marp-team/marp-cli/releases"
            target="_blank"
            rel="noopener noreferrer"
          >
            Releases
          </Button>
          <Button
            outline
            color="primary"
            className="mr-2 mb-2"
            href="https://www.npmjs.com/package/@marp-team/marp-cli"
            target="_blank"
            rel="noopener noreferrer"
          >
            npm
          </Button>
          <Button
            outline
            className="mr-2 mb-2"
            href="https://github.com/marp-team/marp-cli"
            target="_blank"
            rel="noopener noreferrer"
          >
            GitHub
          </Button>
        </Card>
        <h3 className="text-center text-2xl font-bold sm:text-3xl">
          <mark>For developers</mark>
        </h3>
        <Card
          description="All official Marp tooling uses this core as the engine. It is based on the Marpit framework and includes some extra features to help create beautiful slide decks."
          name="Marp Core"
          summary="The core of the Marp converter"
          badge="https://img.shields.io/npm/v/@marp-team/marp-core.svg?style=flat-square&amp;label=&amp;colorB=0288d1"
          href="https://github.com/marp-team/marp-core"
          className="core"
        >
          <Button
            outline
            color="primary"
            className="mr-2 mb-2"
            href="https://www.npmjs.com/package/@marp-team/marp-core"
            target="_blank"
            rel="noopener noreferrer"
          >
            npm
          </Button>
          <Button
            outline
            className="mr-2 mb-2"
            href="https://github.com/marp-team/marp-core"
            target="_blank"
            rel="noopener noreferrer"
          >
            GitHub
          </Button>
        </Card>
        <Card
          description="Marpit (independented from Marp) is the framework that transforms Markdown and CSS themes to slide decks composed of HTML/CSS. It is optimized to output only the minimum set of assets required."
          name="Marpit framework"
          summary="The skinny framework for creating slide decks from Markdown"
          badge="https://img.shields.io/npm/v/@marp-team/marpit.svg?style=flat-square&amp;label=&amp;colorB=0288d1"
          href="https://marpit.marp.app/"
          className="marpit"
        >
          <Button
            color="primary"
            className="mr-2 mb-2"
            href="https://marpit.marp.app/"
            target="_blank"
            rel="noopener noreferrer"
          >
            Documentation
          </Button>
          <Button
            outline
            color="primary"
            className="mr-2 mb-2"
            href="https://www.npmjs.com/package/@marp-team/marpit"
            target="_blank"
            rel="noopener noreferrer"
          >
            npm
          </Button>
          <Button
            outline
            className="mr-2 mb-2"
            href="https://github.com/marp-team/marpit"
            target="_blank"
            rel="noopener noreferrer"
          >
            GitHub
          </Button>
        </Card>
        <p className="mt-4 text-center">
          Find all of the Marp tools, integrations, and examples in the GitHub
          repository!
        </p>
        <p className="text-foreground mt-4 text-center text-sm">
          <Button
            href="https://github.com/marp-team/marp/"
            rel="noopener"
            target="_blank"
          >
            Check out Marp GitHub repository...
          </Button>
        </p>
      </section>
    </div>
    <style jsx>{`
      .get-started {
        @apply bg-marp-brand relative text-white;

        background-image: var(--noise-image),
          linear-gradient(
            -2deg,
            theme('colors.marp.darken'),
            theme('colors.marp.brand') 500px
          );
      }

      .get-started::before,
      .get-started::after {
        @apply absolute inset-x-0 block;

        background-image: var(--noise-image),
          linear-gradient(to bottom, rgba(255, 255, 255, 0.4), transparent 95%);
        bottom: calc(100% - 5px);
        content: '';
        transform: translateZ(0);
        z-index: -1;
      }

      .get-started::before {
        @apply bg-marp-light;

        clip-path: polygon(0 0, 100% 90%, 100% 100%, 0 100%);
        height: calc(120px + 5vw);
      }

      .get-started::after {
        @apply bg-marp-brand;

        clip-path: polygon(0 0, 100% 95%, 100% 100%, 0 100%);
        height: calc(60px + 5vw);
      }
    `}</style>
  </>
)

```

`/Users/nikola/dev/marp/website/components/Marp.tsx`:

```tsx
import { Marp as MarpCore } from '@marp-team/marp-core'
import classNames from 'classnames'
import postcss, { Plugin } from 'postcss'
import postcssImportUrl from 'postcss-import-url'
import { useCallback, useEffect, useMemo, useRef, useState } from 'react'
import type { Swiper as SwiperClass } from 'swiper'
import { Swiper, SwiperSlide } from 'swiper/react'
import { useFontFace } from 'utils/hooks/useFontFace'

export type RenderedMarp = ReturnType<
  typeof generateRenderedMarp
> extends Promise<infer T>
  ? T
  : never

export type MarpProps = {
  border?: boolean
  className?: string
  rendered: Pick<RenderedMarp, 'css' | 'html' | 'fonts'>
  page?: number
}

const postcssStripFontFace = Object.assign(
  (): Plugin => ({
    postcssPlugin: 'marp-strip-font-face',
    AtRule: (rule, { result }) => {
      if (rule.name === 'font-face') {
        result['fonts'] = [...(result['fonts'] || []), rule]
        rule.remove()
      }
    },
  }),
  { postcss: true as const }
)

export const generateRenderedMarp = async (markdown: string) => {
  const marp = new MarpCore({
    container: false,
    script: false,
    printable: false,
  })

  const { css, html } = marp.render(markdown, { htmlAsArray: true })

  const result = await postcss()
    .use(postcssImportUrl)
    .use(postcssStripFontFace)
    .process(css, { from: undefined })

  const fonts: string[] = (result['fonts'] || []).map((font) => font.toString())

  return { markdown, html, css: result.css, fonts }
}

export const Marp = ({
  border = true,
  className,
  rendered: { css, html, fonts },
  page = 1,
}: MarpProps) => {
  const element = useRef<HTMLDivElement>(null)

  useFontFace(fonts)

  useEffect(() => {
    if (!element.current) return
    if (!element.current.shadowRoot)
      element.current.attachShadow({ mode: 'open' })

    // Render Marp slide to shadow root (tailwind default styles will break Marp slide CSS)
    const root = element.current.shadowRoot as ShadowRoot

    root.innerHTML =
      html[page - 1] +
      `<style>${css}</style><style>:host{all:initial;}:host>[data-marpit-svg]{vertical-align:top;}</style>`

    // eslint-disable-next-line @typescript-eslint/no-var-requires
    return require('@marp-team/marp-core/browser').browser(root)
  }, [css, html, page])

  return (
    <div className={classNames(border && 'border shadow-lg', className)}>
      <span ref={element} />
    </div>
  )
}

export const MarpSlides = (props) => {
  const htmlRaw: string = props['data-html']
  const css: string = props['data-css']
  const fontsRaw: string = props['data-fonts']

  const [activePageIdx, setActivePageIdx] = useState(0)
  const swiper = useRef<SwiperClass>()
  const html = useMemo(() => JSON.parse(htmlRaw) as string[], [htmlRaw])
  const multiple = html.length > 1
  const fonts = useMemo(() => JSON.parse(fontsRaw) as string[], [fontsRaw])

  const handleActiveIndexChange = useCallback((instance: SwiperClass) => {
    setActivePageIdx(instance.activeIndex)
  }, [])

  const handleSwiper = useCallback(
    (instance: SwiperClass) => {
      swiper.current = instance
      handleActiveIndexChange(instance)
    },
    [handleActiveIndexChange]
  )

  return (
    <section className={classNames('marp-slides', multiple && 'multiple')}>
      {multiple && (
        <button
          aria-label="Prev"
          className="marp-navigation left-0"
          disabled={activePageIdx <= 0}
          onClick={() => swiper.current?.slidePrev()}
          translate="no"
        >
          &laquo;
        </button>
      )}
      <Swiper
        enabled={multiple.toString() as any}
        allowTouchMove={multiple}
        speed={200}
        onActiveIndexChange={handleActiveIndexChange}
        onSwiper={handleSwiper}
      >
        {html.map((h, i) => (
          <SwiperSlide key={h}>
            <div inert={activePageIdx === i ? undefined : ''}>
              <Marp
                border={false}
                rendered={{ html, css, fonts }}
                page={i + 1}
              />
            </div>
          </SwiperSlide>
        ))}
      </Swiper>
      {multiple && (
        <button
          aria-label="Next"
          className="marp-navigation right-0"
          disabled={activePageIdx >= html.length - 1}
          onClick={() => swiper.current?.slideNext()}
          translate="no"
        >
          &raquo;
        </button>
      )}
      <style jsx>{`
        .marp-slides {
          @apply relative my-6 mx-auto w-full max-w-sm border bg-gray-200 shadow-lg lg:max-w-lg;
        }
        .marp-slides.multiple {
          @apply px-8;
        }

        .marp-navigation {
          @apply absolute inset-y-0 z-10 w-8 appearance-none bg-gray-300 text-4xl text-gray-600 outline-none;

          user-select: none;
        }
        .marp-navigation:hover:not(:disabled) {
          @apply bg-gray-400;
        }
        .marp-navigation:hover:active {
          @apply text-gray-700;
        }
        .marp-navigation:disabled {
          @apply pointer-events-none text-opacity-30;
        }
        .marp-navigation:focus-visible {
          @apply ring-marp-brand ring-2;
        }
      `}</style>
    </section>
  )
}

```

`/Users/nikola/dev/marp/website/components/Title.tsx`:

```tsx
// eslint-disable-next-line @typescript-eslint/ban-types
export const Title: React.FC<React.PropsWithChildren<{}>> = ({ children }) => (
  <section className="bg-marp-brand border-b py-3  text-white">
    <h1 className="font-rounded text-center text-3xl font-bold uppercase">
      {children}
      <style jsx>{`
        & :global(a),
        & :global(a:hover),
        & :global(a:hover:active) {
          @apply text-current no-underline;
        }
        & :global(a:focus-visible) {
          @apply underline outline-none;
        }
      `}</style>
    </h1>
  </section>
)

```

`/Users/nikola/dev/marp/website/components/ScrollToTop.tsx`:

```tsx
import { ArrowUpIcon } from '@primer/octicons-react'
import { useCallback } from 'react'

export const ScrollToTop = () => {
  const handleClick = useCallback<React.MouseEventHandler<HTMLElement>>((e) => {
    window.scrollTo({ top: 0 })
    e.currentTarget.blur()
  }, [])

  return (
    <div className="scroll-to-top">
      <button onClick={handleClick} title="Scroll to top">
        <ArrowUpIcon className="scroll-to-top-icon" />
        <span className="sr-only">Scroll to top</span>
      </button>
      <style jsx>{`
        .scroll-to-top {
          @apply pointer-events-none fixed right-0 bottom-0 z-50;

          filter: drop-shadow(0 0px 7px rgba(0, 0, 0, 0.3))
            drop-shadow(0 0px 4px rgba(0, 0, 0, 0.15));
        }
        button {
          @apply bg-marp-light pointer-events-auto h-20 w-20 appearance-none align-top text-white;

          clip-path: polygon(100% 0, 100% 100%, 0 100%);
        }
        button:hover {
          @apply bg-marp-brand;
        }
        button:focus {
          @apply outline-none;
        }
        button:focus,
        button:hover:active {
          @apply bg-marp-dark;
        }
        button :global(.scroll-to-top-icon) {
          height: auto;
          left: 52%;
          position: absolute;
          top: 52%;
          width: 35%;
        }
      `}</style>
    </div>
  )
}

```

`/Users/nikola/dev/marp/website/components/markdown/Pre.tsx`:

```tsx
import { CodeBlock } from '../CodeBlock'

export const Pre: React.FC = (props) => {
  if (props['data-code'] === undefined) return <pre {...props} />

  return (
    <CodeBlock
      className="sm:mx-auto sm:w-11/12 lg:w-5/6"
      language={props['data-language']}
      copyButton
    >
      {props['data-code']}
    </CodeBlock>
  )
}

export const toHastCodeHandler = (h, { position, lang, value, marp }) => {
  if (marp) {
    return h(position, 'marp-slides', {
      'data-comments': JSON.stringify(marp.comments),
      'data-css': marp.css,
      'data-html': JSON.stringify(marp.html),
      'data-fonts': JSON.stringify(marp.fonts),
    })
  }

  return h(
    position,
    'pre',
    { 'data-code': value, 'data-language': lang?.trim() },
    []
  )
}

```

`/Users/nikola/dev/marp/website/components/markdown/Heading.tsx`:

```tsx
import { createContext, useContext } from 'react'

// eslint-disable-next-line @typescript-eslint/ban-types
type HOCProps<P extends {} = Record<string, any>> = React.PropsWithChildren<P>

const anchorLinkContext = createContext(true)

const Heading: React.FC<HOCProps<{ level: number; id?: string }>> = ({
  children,
  level,
  id,
  ...rest
}) => {
  const anchorLink = useContext(anchorLinkContext)
  const HeadingTag: any = 'h' + level

  return (
    <HeadingTag id={id} {...rest}>
      {id && anchorLink && (
        <a
          aria-hidden
          className="anchor-link"
          href={`#${id}`}
          tabIndex={-1}
        ></a>
      )}
      {children}
    </HeadingTag>
  )
}

export const H1: React.FC<HOCProps> = ({ children, ...rest }) => (
  <Heading level={1} {...rest}>
    <span>
      {children}
      <style jsx>{`
        & {
          box-shadow: inset 0 -0.2em theme('colors.marp.light');
        }
      `}</style>
    </span>
  </Heading>
)

export const H2: React.FC<HOCProps> = ({ children, ...rest }) => (
  <Heading level={2} {...rest}>
    <span className="headingLv2">
      <span className="content">{children}</span>
      <span className="divider"></span>
    </span>
    <style jsx>{`
      .headingLv2 {
        @apply flex items-center;
      }

      .content {
        @apply flex-initial;
      }

      .divider {
        @apply ml-6 h-0 flex-1 border-t border-gray-400;
      }
    `}</style>
  </Heading>
)

// export const H2: React.FC = (props) => <Heading level={2} {...props} />
export const H3: React.FC<HOCProps> = (props) => (
  <Heading level={3} {...props} />
)
export const H4: React.FC<HOCProps> = (props) => (
  <Heading level={4} {...props} />
)
export const H5: React.FC<HOCProps> = (props) => (
  <Heading level={5} {...props} />
)
export const H6: React.FC<HOCProps> = (props) => (
  <Heading level={6} {...props} />
)

export const AnchorLinkProvider = anchorLinkContext.Provider

```

`/Users/nikola/dev/marp/website/components/markdown/Image.tsx`:

```tsx
export type ImageProps = {
  src: string
  alt: string
  [attr: string]: string
}

export const Image = ({ src, alt, ...rest }: ImageProps) => {
  const isVideo = src.endsWith('.mp4')

  if (isVideo) {
    let autoplay: boolean | undefined
    let controls: boolean | undefined
    let poster: string | undefined

    const normalizedAlt = (alt || '')
      .replace(
        /\b(?:autoplay|controls|poster=([^\s]+))\s*\b/g,
        (matched, value) => {
          if (matched.startsWith('autoplay')) autoplay = true
          if (matched.startsWith('controls')) controls = true
          if (matched.startsWith('poster')) poster = value

          return ''
        }
      )
      .trim()

    return (
      <video
        className="markdown-video"
        src={src}
        playsInline
        controls={controls}
        loop
        preload="metadata"
        poster={poster}
        autoPlay={autoplay}
        muted={autoplay}
        {...rest}
      >
        <a href={src} target="_blank" rel="noopener noreferrer">
          {normalizedAlt}
        </a>
        <style jsx>{`
          .markdown-video {
            @apply mx-auto block w-full max-w-xl shadow-md;
            @apply my-6 !important;
          }
        `}</style>
      </video>
    )
  }

  return <img src={src} alt={alt} {...rest} />
}

```

`/Users/nikola/dev/marp/website/components/markdown/Anchor.tsx`:

```tsx
import Link from 'next/link'

export const Anchor: React.FC<{ href?: string }> = ({ href, ...rest }) => {
  if (!href) return <a {...rest} />

  if (href && (href.startsWith('http://') || href.startsWith('https://'))) {
    return <a href={href} {...rest} target="_blank" rel="noreferrer noopener" />
  }

  return <Link href={href} {...rest} />
}

```

`/Users/nikola/dev/marp/website/components/Typography.tsx`:

```tsx
// eslint-disable-next-line @typescript-eslint/ban-types
export const Typography: React.FC<React.PropsWithChildren<{}>> = ({
  children,
}) => (
  <div className="typography">
    {children}
    <style jsx>{`
      .typography {
        @apply break-words text-base leading-relaxed;
      }
      .typography :global(p) {
        @apply my-4;
      }
      .typography :global(h1) {
        @apply relative mt-8 mb-5 text-3xl font-bold;
      }
      .typography :global(h2) {
        @apply relative mt-8 mb-5 text-2xl font-bold;
      }
      .typography :global(h3) {
        @apply relative mt-8 mb-4 text-xl font-bold;
      }
      .typography :global(h4) {
        @apply relative mt-6 mb-4 text-lg font-bold;
      }
      .typography :global(h5) {
        @apply relative mt-6 mb-4 text-base font-bold;
      }
      .typography :global(h6) {
        @apply relative mt-6 mb-4 text-sm font-bold text-gray-600;
      }
      .typography :global(.anchor-link) {
        @apply absolute inset-0 my-auto -ml-5 hidden w-5 overflow-hidden whitespace-nowrap bg-left bg-no-repeat;

        background-size: 1rem 1rem;
        background-image: url('https://icongr.am/octicons/link.svg?color=718096');
      }
      .typography :global(h1:hover > .anchor-link),
      .typography :global(h2:hover > .anchor-link),
      .typography :global(h3:hover > .anchor-link),
      .typography :global(h4:hover > .anchor-link),
      .typography :global(h5:hover > .anchor-link),
      .typography :global(h6:hover > .anchor-link) {
        @apply block;
      }
      .typography :global(hr) {
        @apply my-8;
      }
      .typography :global(blockquote) {
        @apply border-marp-light my-6 border-l-4 pl-5 text-gray-600;
      }
      .typography :global(blockquote blockquote) {
        border-left-width: 3px;
      }
      .typography :global(blockquote blockquote blockquote) {
        @apply border-l-2;
      }
      .typography :global(ul) {
        @apply my-6 ml-8 mr-3 list-disc;
      }
      .typography :global(ul ul) {
        list-style-type: circle;
      }
      .typography :global(ul ul ul) {
        list-style-type: square;
      }
      .typography :global(ol:not(.code-block)) {
        @apply my-6 ml-8 mr-3 list-decimal;
      }
      .typography :global(ul ul),
      .typography :global(ul ol:not(._)),
      .typography :global(ol:not(._) ul),
      .typography :global(ol:not(._) ol:not(._)) {
        @apply my-0 mr-0;
      }
      .typography :global(li:not(.code-block)) {
        @apply my-1;
      }
      .typography :global(code:not(.code-block)) {
        @apply rounded border border-gray-400 bg-gray-200;

        font-size: 0.9em;
        padding: 0.15em 0.35em;
      }
      .typography :global(pre) {
        @apply my-6;
      }
      .typography :global(img) {
        @apply inline;
      }
      .typography :global(figure) {
        @apply my-6;
      }
      .typography :global(figure img) {
        @apply mx-auto block;
        max-width: min(theme('screens.md'), 100%);
      }
      .typography :global(figcaption) {
        @apply mx-auto my-4 w-11/12 text-center text-sm text-gray-600;
      }
      .typography :global(table) {
        @apply mx-auto my-8 max-w-full;
      }
      .typography :global(td),
      .typography :global(th) {
        @apply border-b border-gray-400 p-2 text-sm;
      }
      .typography :global(thead tr:last-child td),
      .typography :global(thead tr:last-child th) {
        @apply border-b-2;
      }

      @screen sm {
        .typography :global(td),
        .typography :global(th) {
          @apply py-2 px-4;
        }
      }

      @screen md {
        .typography :global(td),
        .typography :global(th) {
          @apply text-base;
        }
      }

      .typography > :global(*:first-child),
      .typography > :global(*:first-child *:first-child) {
        @apply mt-0;
      }
      .typography > :global(*:last-child),
      .typography > :global(*:last-child *:last-child) {
        @apply mb-0;
      }
    `}</style>
  </div>
)

```

`/Users/nikola/dev/marp/website/components/docs/Breadcrumb.tsx`:

```tsx
import Link from 'next/link'

export type BreadcrumbProps = {
  breadcrumbs: {
    key: string
    link?: string
    title: string
  }[]
}

export const Breadcrumb = ({ breadcrumbs }: BreadcrumbProps) => (
  <ol>
    {breadcrumbs.map(({ key, title, link }) => (
      <li key={key}>{link ? <Link href={link}>{title}</Link> : title}</li>
    ))}
    <style jsx>{`
      ol {
        @apply inline-flex flex-1 flex-nowrap whitespace-nowrap;
      }
      li {
        @apply block;
      }
      li::after {
        @apply bg-no-repeat pl-6;

        background-image: url('https://icongr.am/octicons/triangle-right.svg?color=718096');
        background-position: 0.25rem center;
        background-size: 1rem 1rem;
        content: '';
      }
      li:last-child {
        @apply font-bold;
      }
      li:last-child::after {
        @apply hidden;
      }
    `}</style>
  </ol>
)

```

`/Users/nikola/dev/marp/website/components/docs/layouts/Desktop.tsx`:

```tsx
import {
  CSSProperties,
  useLayoutEffect,
  useRef,
  useState,
  useMemo,
} from 'react'
import { Breadcrumb } from 'components/docs/Breadcrumb'
import { LayoutProps } from 'components/docs/Layout'
import { Navigation } from 'components/docs/Navigation'

export const Desktop: React.FC<LayoutProps> = ({
  breadcrumbs,
  children,
  manifest,
  slug,
}) => {
  const sidebarRef = useRef<HTMLDivElement>(null)
  const sidebarContentRef = useRef<HTMLDivElement>(null)
  const headerHeightDetecterRef = useRef<HTMLDivElement>(null)

  const [stickyGap, setStickyGap] = useState(0)
  const [isScrollDown, setIsScrollDown] = useState(true)
  const [sidebarScrollable, setSidebarScrollable] = useState(false)

  useLayoutEffect(() => {
    let previousScrollY = window.scrollY

    const handleScroll = () => {
      // Get header height
      const headerHeight = headerHeightDetecterRef.current?.clientHeight || 80

      // Detect whether sidebar is scrollable
      const sidebarElm = sidebarRef.current
      const sidebarRect = sidebarElm?.getBoundingClientRect()
      const parentElm = sidebarElm?.parentElement
      const parentRect = parentElm?.getBoundingClientRect()

      if (sidebarContentRef.current && sidebarRect && parentRect) {
        const viewHeight = Math.max(
          0,
          Math.min(window.innerHeight, parentRect.bottom) - headerHeight
        )

        setSidebarScrollable(
          viewHeight < sidebarContentRef.current.clientHeight
        )
      }

      // Handle scroll
      const resetStickyGap = (base: 'top' | 'bottom') => {
        if (sidebarRect && parentRect) {
          setStickyGap(sidebarRect[base] - parentRect[base])
        }
      }

      const { scrollY } = window
      const scrollDelta = scrollY - previousScrollY

      if (scrollDelta < 0) {
        // Scroll up
        setIsScrollDown((prev) => {
          if (prev) resetStickyGap('bottom')
          return false
        })
      } else {
        // Scroll down
        setIsScrollDown((prev) => {
          if (!prev) resetStickyGap('top')
          return true
        })
      }
      previousScrollY = scrollY
    }

    window.addEventListener('scroll', handleScroll)
    window.addEventListener('resize', handleScroll)

    return () => {
      window.removeEventListener('scroll', handleScroll)
      window.removeEventListener('resize', handleScroll)
    }
  }, [])

  const sidebarStyle = useMemo<CSSProperties>(() => {
    if (!sidebarScrollable)
      return { alignSelf: 'start', top: 'var(--header-height)' }

    return {
      alignSelf: isScrollDown ? 'end' : 'start',
      top: !isScrollDown ? `var(--header-height)` : '',
      bottom: isScrollDown ? `0px` : '',
      marginBottom: stickyGap < 0 ? `${-stickyGap}px` : 0,
      marginTop: stickyGap >= 0 ? `${stickyGap}px` : 0,
    }
  }, [isScrollDown, sidebarScrollable, stickyGap])

  return (
    <>
      <div
        ref={headerHeightDetecterRef}
        className="fixed top-0 left-0 -z-10 h-[var(--header-height)] w-px opacity-0"
      />
      <div id="docs-container" className="text-sm xl:text-base">
        <div ref={sidebarRef} id="docs-sidebar" style={sidebarStyle}>
          <div ref={sidebarContentRef} className="sidebar-nav-content">
            <Navigation manifest={manifest} slug={slug} />
          </div>
        </div>
        <div className="my-6 w-px bg-gray-400" style={{ gridArea: 'border' }} />
        <div className="[grid-area:contents]">
          <div className="px-8 py-10">
            {breadcrumbs?.length && (
              <div className="mb-6 rounded bg-gray-300 p-2">
                <Breadcrumb breadcrumbs={breadcrumbs} />
              </div>
            )}
            <article id="docs-article" className="container">
              {children}
            </article>
          </div>
        </div>
      </div>
      {/* <div ref={docsClearfixRef} /> */}
      <style jsx>{`
        #docs-container {
          @apply grid;

          min-height: inherit;
          grid-template:
            'sidebar border contents' auto
            / minmax(16rem, 20%) 1px minmax(0, 1fr);
        }

        #docs-sidebar {
          @apply sticky [grid-area:sidebar];
        }

        #docs-article {
          @apply mx-auto px-6;

          --root-font-size: 0.9rem;
        }

        .sidebar-nav-content {
          @apply mx-auto w-64 px-8 py-10;

          min-width: 16rem;
        }

        @screen xl {
          #docs-container {
            grid-template:
              'sidebar border contents nav' auto
              / minmax(16rem, 20%) 1px minmax(0, 1fr) minmax(8rem, 15%);
          }

          #docs-article {
            --root-font-size: 1rem;
          }

          .sidebar-nav-content {
            @apply w-5/6;
          }
        }
      `}</style>
    </>
  )
}

```

`/Users/nikola/dev/marp/website/components/docs/layouts/Mobile.tsx`:

```tsx
import { ThreeBarsIcon, XIcon } from '@primer/octicons-react'
import { disableBodyScroll, enableBodyScroll } from 'body-scroll-lock'
import classNames from 'classnames'
import FocusTrap from 'focus-trap-react'
import { useRouter } from 'next/router'
import { useCallback, useEffect, useRef, useState } from 'react'
import { Breadcrumb } from 'components/docs/Breadcrumb'
import { LayoutProps } from 'components/docs/Layout'
import { Navigation } from 'components/docs/Navigation'

const useOnPageLoad = (callback: () => void, immediate = false) => {
  const router = useRouter()

  useEffect(() => {
    if (immediate) callback()
  }, [callback]) // eslint-disable-line react-hooks/exhaustive-deps

  useEffect(() => {
    router.events.on('routeChangeComplete', callback)
    return () => router.events.off('routeChangeComplete', callback)
  }, [callback, router.events])
}

const useDrawer = (drawer?: HTMLElement) => {
  const [open, setOpen] = useState(false)
  const [active, setActive] = useState(false)
  const activeTimer = useRef<number>()
  const lastFocusedElement = useRef<HTMLElement | undefined>(undefined)

  const handleOpen = useCallback((e?: React.SyntheticEvent<HTMLElement>) => {
    setActive(true)
    setOpen(true)

    lastFocusedElement.current = e?.currentTarget
  }, [])

  const handleClose = useCallback(() => {
    setActive(true)
    setOpen(false)
  }, [])

  const toggle = useCallback(
    (e?: React.SyntheticEvent<HTMLElement>) => {
      open ? handleClose() : handleOpen(e)
    },
    [open, handleOpen, handleClose]
  )

  useOnPageLoad(handleClose)

  useEffect(() => {
    if (drawer && open) {
      disableBodyScroll(drawer)
      return () => enableBodyScroll(drawer)
    }
  }, [drawer, open])

  useEffect(() => {
    if (open) {
      const escKeyListener = ({ key }: KeyboardEvent) => {
        if (key === 'Escape') handleClose()
      }

      document.addEventListener('keydown', escKeyListener)
      return () => document.removeEventListener('keydown', escKeyListener)
    }
  }, [handleClose, open])

  useEffect(() => {
    if (!open && lastFocusedElement.current) {
      lastFocusedElement.current.focus()
    }
  }, [open])

  useEffect(() => {
    if (active) {
      if (activeTimer.current !== undefined)
        window.clearTimeout(activeTimer.current)

      activeTimer.current = window.setTimeout(() => setActive(false), 300)
    }
  }, [active])

  return { active, handleClose, handleOpen, toggle, open }
}

export const Mobile: React.FC<LayoutProps> = ({
  children,
  breadcrumbs,
  manifest,
  slug,
}) => {
  const [drawer, setDrawer] = useState<HTMLElement | null>(null)
  const { active, handleClose, toggle, open } = useDrawer(drawer ?? undefined)

  const breadcrumbsContainer = useRef<HTMLDivElement | null>(null)

  useOnPageLoad(
    useCallback(() => {
      breadcrumbsContainer.current?.scrollTo({
        left: breadcrumbsContainer.current.scrollWidth,
        behavior: 'instant' as any,
      })
    }, []),
    true
  )

  return (
    <>
      <div
        className={classNames('docs-backdrop', { active, open })}
        onClick={handleClose}
        aria-hidden
      />
      <FocusTrap
        active={open}
        focusTrapOptions={{
          allowOutsideClick: () => true,
          escapeDeactivates: false,
          initialFocus: '#docs-nav',
          fallbackFocus: '#docs-nav-toggle',
        }}
      >
        <nav
          id="docs-nav"
          className={classNames({ active, open })}
          ref={setDrawer}
          tabIndex={-1}
          inert={open ? undefined : ''}
        >
          <div className="p-8">
            <p className="mb-6">
              <button
                className="docs-btn h-8 w-8"
                onClick={handleClose}
                aria-expanded={open}
              >
                <XIcon className="docs-btn-close-icon" />
                <span className="sr-only">Close navigation</span>
              </button>
            </p>
            <Navigation manifest={manifest} slug={slug} />
          </div>
        </nav>
      </FocusTrap>
      <nav className="docs-topbar">
        <button
          className="docs-btn relative z-20 m-1 h-8 w-8"
          id="docs-nav-toggle"
          type="button"
          onClick={toggle}
          aria-controls="docs-nav"
          aria-expanded={open}
        >
          <ThreeBarsIcon className="docs-btn-open-drawer-icon" />
          <span className="sr-only">Toggle navigation</span>
        </button>
        {breadcrumbs?.length && (
          <div ref={breadcrumbsContainer} className="docs-breadcrumb-container">
            <div className="docs-breadcrumb">
              <Breadcrumb breadcrumbs={breadcrumbs} />
            </div>
          </div>
        )}
      </nav>
      <article id="docs-article" className="container">
        {children}
      </article>
      <style jsx global>{`
        :root {
          --anchor-margin: calc(var(--header-height) + 2.5rem);
        }
      `}</style>
      <style jsx>{`
        .docs-backdrop {
          @apply pointer-events-none fixed inset-0 cursor-pointer opacity-0 transition-opacity;

          -webkit-tap-highlight-color: transparent;
          backdrop-filter: blur(2px);
          background: rgba(255, 255, 255, 0.75);
          z-index: 60;
        }
        .docs-backdrop.active {
          @apply duration-300;
        }
        .docs-backdrop.open {
          @apply pointer-events-auto opacity-100;
        }

        .docs-btn {
          @apply appearance-none rounded text-gray-700;
        }
        .docs-btn:hover,
        .docs-btn:focus {
          @apply bg-gray-200 outline-none;
        }
        .docs-btn:hover:active {
          @apply bg-gray-300 outline-none;
        }
        .docs-btn:focus-visible {
          @apply ring-1 ring-white ring-offset-2;
        }

        .docs-btn :global(.docs-btn-close-icon) {
          @apply h-8 w-8;
        }
        .docs-btn :glboal(.docs-btn-open-drawer-icon) {
          @apply h-8 w-8 p-1;
        }

        #docs-nav {
          @apply bg-background fixed inset-0 w-64 -translate-x-full transform overflow-hidden border-r outline-none;

          transition-property: box-shadow, transform;
          z-index: 60;
        }
        #docs-nav.active {
          @apply duration-300;
        }
        #docs-nav.open {
          @apply transform-none overflow-auto shadow-2xl;
        }

        .docs-topbar {
          @apply fixed inset-0 top-16 z-50 flex h-10 items-stretch bg-white shadow-sm;
        }
        .docs-breadcrumb-container {
          @apply flex flex-1 snap-x snap-proximity scroll-px-2 items-center overflow-x-auto;

          mask: linear-gradient(to right, transparent, #000 0.5rem, #000)
            no-repeat left top;
          -ms-overflow-style: none;
          scrollbar-width: none;
        }
        .docs-breadcrumb-container::-webkit-scrollbar {
          display: none;
        }
        .docs-breadcrumb {
          @apply relative mr-auto px-2;
          @apply after:pointer-events-none after:absolute after:inset-0 after:mx-2 after:snap-end;
        }
        .docs-breadcrumb :global(li) {
          @apply snap-start;
        }

        #docs-article {
          @apply mx-auto p-6 pt-16;

          --root-font-size: 0.9rem;
        }
      `}</style>
    </>
  )
}

```

`/Users/nikola/dev/marp/website/components/docs/Layout.tsx`:

```tsx
import { useMedia, useMediaLayout } from 'use-media'
import { BreadcrumbProps } from './Breadcrumb'
import { NavigationProps } from './Navigation'
import { Desktop } from './layouts/Desktop'
import { Mobile } from './layouts/Mobile'
import { Layout } from 'components/Layout'

export type LayoutProps = React.PropsWithChildren<
  BreadcrumbProps & NavigationProps
>

const useMediaIsomorphic =
  typeof window === 'undefined' ? useMedia : useMediaLayout

const DocsLayout: React.FC<LayoutProps> = (props) => {
  const isDesktop = useMediaIsomorphic({ minWidth: '768px' }, false)
  const Container = isDesktop ? Desktop : Mobile

  return (
    <Layout
      activeItem="docs"
      canonical={`/docs/${props.slug.join('/')}`}
      title={[props.breadcrumbs.map((b) => b.title).join(' > '), 'Docs']}
      noIndex={!process.env.NEXT_PUBLIC_DOCS}
    >
      <Container {...props} />
    </Layout>
  )
}

export { DocsLayout as Layout }

```

`/Users/nikola/dev/marp/website/components/docs/Navigation.tsx`:

```tsx
import classNames from 'classnames'
import Link from 'next/link'

export type NavigationProps = {
  manifest: Record<string, any>
  slug: string[]
}

export const Navigation = ({
  manifest,
  slug: currentSlug,
}: NavigationProps) => {
  const activePage = `/docs/${currentSlug.join('/')}`

  return (
    <div>
      {Object.entries<any>(manifest).map(([slug, meta]) => (
        <ul className="category" key={slug}>
          <li>
            {meta.title && <h3 className="category-title">{meta.title}</h3>}
            {meta.pages && (
              <ul>
                {Object.entries<any>(meta.pages).map(([pSlug, pMeta]) => {
                  const href = `/docs/${slug}/${pSlug}`

                  return (
                    <Link href={href} key={pSlug} legacyBehavior>
                      <a
                        className={classNames(
                          'page-link custom-anchor',
                          href === activePage && 'active'
                        )}
                      >
                        <li>{pMeta.title}</li>
                      </a>
                    </Link>
                  )
                })}
              </ul>
            )}
          </li>
        </ul>
      ))}
      <style jsx>{`
        .category {
          @apply mt-6;
        }
        .category:first-child {
          @apply mt-0;
        }
        .category-title {
          @apply font-rounded mb-2 text-xl font-bold uppercase text-gray-700;
        }

        .page-link {
          @apply text-marp-darken mt-1 block rounded py-1 px-2 outline-none;

          transition-property: background-color, border-color, fill, stroke;
        }
        .page-link:hover,
        .page-link:focus {
          @apply text-marp-dark bg-gray-200 duration-300;
        }
        .page-link:hover:active {
          @apply duration-0 bg-gray-300;
        }
        .page-link:focus-visible {
          @apply ring-1 ring-white ring-offset-2;
        }

        .page-link.active {
          @apply from-marp-brand to-marp-dark duration-0 bg-gradient-to-br font-bold text-white;
        }
        .page-link.active:hover:active {
          @apply bg-marp-dark from-marp-dark to-marp-darkest;
        }
      `}</style>
    </div>
  )
}

```

`/Users/nikola/dev/marp/website/components/blog/BlogHeader.tsx`:

```tsx
import Link from 'next/link'
import { formatDate, formatDateShort } from 'utils/date'

export type BlogHeaderProps = {
  author?: string
  date?: Date
  github?: string
  slug: string
  title: string
}

export const BlogHeader = ({
  author,
  date,
  github,
  slug,
  title,
}: BlogHeaderProps) => (
  <div className="text-center text-gray-600">
    <Link href={`/blog/${slug}`}>
      <h1 className="text-gradient text-3xl font-bold md:text-4xl">{title}</h1>
    </Link>
    {date && (
      <p className="mt-4">
        <time dateTime={formatDateShort(date)}>{formatDate(date)}</time>
      </p>
    )}
    <p className="author">
      {(author || github) && (
        <>
          {github && (
            <img
              src={`https://github.com/${github}.png`}
              alt={author || github}
              className="mr-4 h-16 w-16 rounded-full bg-white shadow-md"
              width={64}
              height={64}
            />
          )}
          <span className="leading-relaxed">
            by{' '}
            {author && (
              <>
                {author}
                {github && <br />}
              </>
            )}
            {github && (
              <a
                href={`https://github.com/${github}`}
                target="_blank"
                rel="noopener noreferrer"
              >
                @{github}
              </a>
            )}
          </span>
        </>
      )}
      <style jsx>{`
        .author {
          @apply -mx-6 mt-5 flex items-center text-left;
        }

        .author::before,
        .author::after {
          @apply mx-6 block h-px flex-1 bg-gray-400;

          content: '';
        }

        .author:empty {
          @apply mx-0 h-px;
        }

        .author:empty::before,
        .author:empty::after {
          @apply mx-0;
        }
      `}</style>
    </p>
  </div>
)

```

`/Users/nikola/dev/marp/website/components/Footer.tsx`:

```tsx
import { ScrollToTop } from 'components/ScrollToTop'

export const Footer = () => (
  <footer>
    <div className="container mx-auto table">
      <p className="mx-6 my-5 mr-20 leading-loose">
        Copyright © 2019-{process.env.BUILD_YEAR} Marp team.&emsp;
        <iframe
          className="inline-block align-text-top"
          src="https://ghbtns.com/github-btn.html?user=marp-team&amp;repo=marp&amp;type=star&amp;count=true"
          frameBorder={0}
          scrolling="0"
          width={150}
          height={20}
          title="GitHub"
          loading="lazy"
        ></iframe>
      </p>
      <ScrollToTop />
    </div>
    <style jsx>{`
      footer {
        @apply bg-gray-800 text-gray-500;

        min-height: 4.5rem;
        background-image: var(--noise-image);
      }
    `}</style>
  </footer>
)

```

`/Users/nikola/dev/marp/website/components/Layout.tsx`:

```tsx
import Head from 'next/head'
import { useRouter } from 'next/router'
import { Footer } from 'components/Footer'
import { Header, ItemSlug } from 'components/Header'
import { generateTitle } from 'utils/title'
import { absoluteUrl } from 'utils/url'

export type LayoutProps = React.PropsWithChildren<{
  activeItem?: ItemSlug
  canonical?: string
  description?: string
  image?: string
  noIndex?: boolean
  title?: string | string[]
  type?: string
}>

const defaultDescription =
  'Marp (also known as the Markdown Presentation Ecosystem) provides an intuitive experience for creating beautiful slide decks. You only have to focus on writing your story in a Markdown document.'

export const Layout: React.FC<LayoutProps> = ({
  activeItem,
  canonical: _canonical,
  children,
  description = defaultDescription,
  image: _image,
  noIndex,
  title: _title,
  type = 'article',
}) => {
  const router = useRouter()

  const canonical = absoluteUrl(_canonical || router.asPath).href
  const image = _image || '/assets/og-image.png'
  const title = typeof _title === 'string' ? _title : generateTitle(_title)

  return (
    <>
      <Head>
        <title key="title">{title}</title>
        {description && (
          <>
            <meta name="description" key="description" content={description} />
            <meta
              property="og:description"
              key="og:description"
              content={description}
            />
          </>
        )}
        {canonical && (
          <>
            <link rel="canonical" key="canonical" href={canonical} />
            <meta property="og:url" key="og:url" content={canonical} />
          </>
        )}
        <meta property="og:title" key="og:title" content={title} />
        <meta property="og:type" key="og:type" content={type} />
        <meta
          property="og:image"
          key="og:image"
          content={absoluteUrl(image).href}
        />
        <meta
          property="twitter:card"
          key="twitter:card"
          content={
            type === 'website' || _image ? 'summary_large_image' : 'summary'
          }
        />
        {noIndex && <meta name="robots" content="noindex,nofollow" />}
      </Head>
      <Header activeItem={activeItem} />
      <main className="relative mt-16 md:mt-20">
        {children}
        <style jsx>{`
          main {
            min-height: calc(100vh - 8.5rem);
          }

          @screen md {
            main {
              min-height: calc(100vh - 9.5rem);
            }
          }
        `}</style>
      </main>
      <Footer />
    </>
  )
}

```

`/Users/nikola/dev/marp/website/components/Header.tsx`:

```tsx
import classNames from 'classnames'
import Link from 'next/link'
import MarpLogo from 'public/assets/marp-logo.svg'

const handleMouseUp = (e: React.MouseEvent<HTMLElement>) =>
  e.currentTarget.blur()

export type ItemSlug = 'docs' | 'blog'

export const Header = ({ activeItem }: { activeItem?: ItemSlug }) => (
  <>
    <header className="header">
      <Link href="/" legacyBehavior>
        <a
          className="custom-anchor header-item"
          role="link"
          tabIndex={0}
          onMouseUp={handleMouseUp}
        >
          <MarpLogo className="block h-16 w-16 p-2 md:h-20 md:w-20 md:p-3" />
          <span className="sr-only">Marp</span>
        </a>
      </Link>
      <nav className="ml-2">
        <ul className="flex h-16 items-stretch md:h-20">
          {process.env.NEXT_PUBLIC_DOCS && (
            <li className="relative flex items-center justify-center">
              <Link href="/docs" legacyBehavior>
                <a
                  className={classNames('custom-anchor header-item nav-item', {
                    active: activeItem === 'docs',
                  })}
                  role="link"
                  tabIndex={0}
                  onMouseUp={handleMouseUp}
                >
                  <span>Docs</span>
                </a>
              </Link>
            </li>
          )}
          <li className="relative flex items-center justify-center">
            <Link href="/blog" legacyBehavior>
              <a
                className={classNames('custom-anchor header-item nav-item', {
                  active: activeItem === 'blog',
                })}
                role="link"
                tabIndex={0}
                onMouseUp={handleMouseUp}
              >
                <span>Blog</span>
              </a>
            </Link>
          </li>
          <li className="relative flex items-center justify-center">
            <a
              href="https://github.com/marp-team/marp"
              target="_blank"
              rel="noopener noreferrer"
              className="custom-anchor header-item nav-item"
              onMouseUp={handleMouseUp}
            >
              <span>GitHub</span>
            </a>
          </li>
        </ul>
      </nav>
      <style jsx>{`
        :global(:root) {
          @apply [--header-height:theme(spacing.16)] md:[--header-height:theme(spacing.20)];
        }

        .header {
          @apply fixed top-0 left-0 z-50 flex h-[var(--header-height)] w-full justify-center bg-white shadow-sm;
        }

        .header-item {
          @apply text-current no-underline outline-none;
        }

        .header-item > :global(svg) {
          @apply transition-transform duration-200;
        }

        .header-item:hover:active > :global(svg) {
          @apply duration-0 scale-125 transform shadow-none;
        }

        @media not all and (hover: none) {
          .header-item:hover:active > :global(svg) {
            @apply scale-110;
          }
        }

        .nav-item {
          @apply font-rounded mx-2 text-lg font-medium uppercase leading-none outline-none;
        }

        .nav-item::before {
          @apply absolute inset-0;

          content: '';
        }

        .header-item:focus-visible,
        .nav-item:focus-visible::before {
          @apply bg-gray-200;
        }

        .header-item:not(.nav-item) {
          -webkit-tap-highlight-color: transparent;
        }

        @screen md {
          .nav-item {
            @apply mx-3 tracking-wider;
          }
        }

        .nav-item > span {
          @apply relative z-10;
        }

        .nav-item > span::after {
          @apply absolute inset-x-0 mt-1 block h-1 transition-all duration-300;

          content: '';
          top: 100%;
        }

        .nav-item:hover > span::after,
        .nav-item:focus-within > span::after {
          box-shadow: inset 0 -0.25rem theme('colors.gray.400');
        }

        .nav-item.active > span::after {
          @apply duration-0;
          box-shadow: inset 0 -0.25rem theme('colors.marp.brand');
        }

        .nav-item:hover:active > span::after {
          @apply duration-0;
          box-shadow: inset 0 -0.25rem theme('colors.marp.dark');
        }
      `}</style>
    </header>
  </>
)

```

`/Users/nikola/dev/marp/website/components/Button.tsx`:

```tsx
import classNames from 'classnames'
import { ReactNode } from 'react'

export type ButtonProps = {
  children?: ReactNode
  color?: 'primary'
  href?: string
  outline?: boolean
  [key: string]: unknown
}

export const Button = ({
  children,
  className,
  color,
  href,
  outline,
  ...rest
}: ButtonProps) => {
  const Tag = href ? 'a' : 'button'
  const attrs = {
    ...rest,
    ...(Tag === 'a' ? { href, role: 'button', tabIndex: 0 } : {}),
  }

  return (
    <Tag
      {...attrs}
      className={classNames(
        Tag === 'a' && 'custom-anchor',
        'button',
        color,
        { btnOutline: outline },
        className as any
      )}
    >
      {children}
      <style jsx>{`
        .button {
          @apply relative inline-block select-none appearance-none rounded-full bg-white text-center font-bold no-underline shadow-md;

          padding: 0.625em 1.25em;
          transition: color, background-color, opacity;
        }

        @screen md {
          .button {
            @apply tracking-wider;
          }
        }

        .button:hover {
          @apply bg-background duration-150;
        }
        .button:hover:active {
          @apply duration-0 bg-gray-300 outline-none ring-1 ring-white ring-offset-2;
        }
        .button:focus {
          @apply outline-none ring-1 ring-white ring-offset-2;
        }

        /* Primary color */
        .button.primary {
          @apply bg-marp-brand text-white;

          background-image: linear-gradient(
            30deg,
            transparent,
            rgba(255, 255, 255, 0.3)
          );
        }
        .button.primary:hover {
          @apply bg-marp-darken;
        }
        .button.primary:hover:active {
          @apply bg-marp-dark;
        }

        /* Outline */
        .button.btnOutline {
          @apply text-foreground;
        }
        .button.btnOutline::after {
          @apply pointer-events-none absolute inset-0 block border-2 border-current;

          border-radius: inherit;
          content: '';
          transition: inherit;
        }

        .button.btnOutline.primary {
          @apply text-marp-darken bg-white;

          background-image: none;
        }
        .button.btnOutline.primary:hover {
          @apply bg-marp-darken text-white;
        }
        .button.btnOutline.primary:hover::after {
          @apply opacity-0;
        }
      `}</style>
    </Tag>
  )
}

```

`/Users/nikola/dev/marp/website/components/CodeBlock.tsx`:

```tsx
/* eslint-disable react/jsx-key */
import classNames from 'classnames'
import Highlight, {
  defaultProps,
  Language,
  PrismTheme,
} from 'prism-react-renderer'
import nightOwlLight from 'prism-react-renderer/themes/nightOwlLight'
import { useRef, useState, MouseEvent } from 'react'
import { Button } from 'components/Button'

const theme: PrismTheme = {
  plain: {
    ...nightOwlLight.plain,
    backgroundColor: '#f5f5f5',
  },
  styles: [
    ...nightOwlLight.styles,
    { types: ['italic'], style: { fontStyle: 'italic' } },
    { types: ['important', 'bold'], style: { fontWeight: 'bold' } },
  ],
}

export type CodeBlockProps = {
  children: string
  copyButton?: boolean
  language: Language
  lineNumber?: boolean
  [key: string]: unknown
}

export const CodeBlock = ({
  children,
  className,
  copyButton,
  language,
  lineNumber = false,
  ...rest
}: CodeBlockProps) => {
  const [copied, setCopied] = useState(false)
  const copiedTimer = useRef<number | undefined>(undefined)

  return (
    <>
      <Highlight
        {...defaultProps}
        code={children}
        language={language}
        theme={theme}
      >
        {({ className: cn, style, tokens, getLineProps, getTokenProps }) => (
          <div className={classNames('code-block-container', className as any)}>
            <pre
              className={classNames(lineNumber && 'line-number', cn)}
              style={style}
              {...rest}
            >
              <code className="code-block">
                <ol className="code-block">
                  {tokens.map((line, i) => {
                    const lineProps = getLineProps({ line, key: i })

                    return (
                      <li
                        {...lineProps}
                        className={classNames(
                          lineProps.className,
                          'code-block'
                        )}
                      >
                        {line.map((token, key) =>
                          token.empty ? (
                            <br key={key} />
                          ) : (
                            <span {...getTokenProps({ token, key })} />
                          )
                        )}
                      </li>
                    )
                  })}
                </ol>
              </code>
            </pre>
            {copyButton && (
              <div className="copy-btn-container">
                <Button
                  className={copied ? 'copied' : undefined}
                  onClick={(e: MouseEvent<HTMLButtonElement>) => {
                    const tmpTextarea = document.createElement('textarea')
                    tmpTextarea.value = children

                    tmpTextarea.style.position = 'absolute'
                    tmpTextarea.style.left = '0'
                    tmpTextarea.style.top = '0'
                    tmpTextarea.style.opacity = '0'
                    tmpTextarea.style.pointerEvents = 'none'

                    document.body.appendChild(tmpTextarea)
                    tmpTextarea.select()

                    document.execCommand('copy')
                    document.body.removeChild(tmpTextarea)
                    e.currentTarget.focus()

                    // Update React state
                    setCopied(true)

                    if (copiedTimer.current !== undefined) {
                      window.clearTimeout(copiedTimer.current)
                    }

                    copiedTimer.current = window.setTimeout(() => {
                      copiedTimer.current = undefined
                      setCopied(false)
                    }, 1000)
                  }}
                >
                  {copied ? 'Copied!' : 'Copy'}
                </Button>
              </div>
            )}
          </div>
        )}
      </Highlight>
      <style jsx>{`
        .code-block-container {
          @apply relative;
        }

        .prism-code {
          @apply overflow-x-auto overflow-y-hidden whitespace-pre break-words rounded-md border text-sm leading-5;

          font-family: inherit;
          background-image: var(--noise-image);
        }

        .prism-code code {
          @apply inline-block min-w-full p-4 font-mono;
        }

        .prism-code.line-number {
          @apply whitespace-pre-wrap;
        }

        .prism-code.line-number ol {
          counter-reset: line 0;
        }

        .prism-code.line-number li {
          @apply relative pl-12;

          counter-increment: line;
        }

        .prism-code.line-number li::before {
          @apply absolute inset-0 w-12 pr-3 text-right text-xs leading-5 text-gray-500;

          content: counter(line);
        }

        .copy-btn-container {
          @apply absolute top-0 right-0 m-3;
        }

        .copy-btn-container :global(button) {
          @apply w-24 py-1 text-xs opacity-0 transition-opacity duration-300;
        }

        .code-block-container:hover .copy-btn-container :global(button),
        .copy-btn-container :global(button):focus {
          @apply opacity-100;
        }
      `}</style>
    </>
  )
}

```

`/Users/nikola/dev/marp/website/public/assets/hero-background.svg`:

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2000 1200"><defs><linearGradient id="a" x1="284.13" y1="124.1" x2="877.7" y2="263.56" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#f3f3f3"/><stop offset="1" stop-color="#fdfdfd"/></linearGradient><linearGradient id="b" x1="855.49" y1="465.13" x2="1966.05" y2="232.05" gradientUnits="userSpaceOnUse"><stop offset=".53" stop-color="#f4f4f4"/><stop offset=".83" stop-color="#f2f2f2"/></linearGradient><linearGradient id="c" x1="118.65" y1="417.06" x2="593.1" y2="969.25" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#e4e4e4"/><stop offset=".43" stop-color="#f1f1f1"/></linearGradient></defs><path fill="url(#a)" d="m1571.5 0-.1.1L0 483.9 510.8 0h1060.7z"/><path fill="#fefefe" d="M1571.4.1 856.6 779.7 0 483.9 1571.4.1z"/><path fill="#fdfdfd" d="M2000 0v53.7L1571.7 0H2000z"/><path fill="#f1f1f1" d="M2000 53.7v471.1L1571.7 0 2000 53.7z"/><path fill="url(#b)" d="M2000 524.8 856.6 779.7 1571.4.1l.3-.1L2000 524.8z"/><path fill="#f8f8f8" d="M2000 524.8v543.4L858 780.1l-1.4-.4L2000 524.8z"/><path fill="url(#c)" d="m552.8 1200 303.8-420.3L0 483.9 364.9 1200h187.9z"/><path fill="#fafafa" d="M0 .1v483.8L510.8 0 0 .1z"/><path fill="#ededed" d="M2000 1200v-131.8L858 780.1l-1.4-.4L552.8 1200H2000z"/><path fill="#f1f1f1" d="M364.9 1200 0 483.9V1200h364.9z"/></svg>
```

`/Users/nikola/dev/marp/website/public/assets/marp.svg`:

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 522.5 160"><defs><style>.d{fill:none;stroke:#000;stroke-linecap:square;stroke-miterlimit:10;stroke-width:5px}</style></defs><path fill="#67b8e3" d="M250 0l-90 90v70h90V0z"/><path fill="#0288d1" d="M160 0L0 160h90l70-70V0z"/><path fill="#02669d" d="M90 160h70V90l-70 70z"/><path class="d" d="M300 110V50l30 30 30-30v60"/><circle class="d" cx="400" cy="90" r="20"/><path class="d" d="M440 90a20.1 20.1 0 0120-20M420 70v40"/><circle class="d" cx="500" cy="90" r="20"/><path class="d" d="M480 70v60M440 70v40"/></svg>
```

`/Users/nikola/dev/marp/website/public/assets/marpit.svg`:

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 60 40"><path d="M38.4 22.4V.8L0 39.2h60V.8zM2.9 38L37.2 3.7v19.9L22.8 38zm21.6 0l12.7-12.7V38zm34.3 0H38.4V24.1L58.8 3.7z" fill="#0288d1"/></svg>
```

`/Users/nikola/dev/marp/website/public/assets/marp-logo.svg`:

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 60 40"><path fill="#009bda" d="M40 0L0 40h20l20-20V0z"/><path fill="#78c5e9" d="M40 20v20h20V0L40 20z"/><path fill="#007aad" d="M20 40h20V20L20 40z"/></svg>

```

`/Users/nikola/dev/marp/website/public/assets/noise.svg`:

```svg
<svg xmlns="http://www.w3.org/2000/svg" width="300" height="300"><filter id="a"><feTurbulence type="fractalNoise" baseFrequency=".75" numOctaves="8" seed="60" stitchTiles="stitch"/><feComponentTransfer><feFuncG type="linear" slope="2" intercept="-.6"/></feComponentTransfer><feColorMatrix values="0 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 0 0 0 1"/></filter><path opacity=".025" filter="url(#a)" d="M0 0h300v300H0z"/></svg>

```

`/Users/nikola/dev/marp/website/babel.config.js`:

```js
const path = require('path')

module.exports = {
  presets: [
    [
      'next/babel',
      {
        'styled-jsx': {
          plugins: [
            [
              require.resolve('styled-jsx-plugin-postcss'),
              { path: path.resolve(__dirname, './postcss.config.js') },
            ],
          ],
        },
      },
    ],
  ],
}

```

`/Users/nikola/dev/marp/website/package.json`:

```json
{
  "name": "@marp-team/marp-website",
  "version": "0.0.0",
  "private": true,
  "scripts": {
    "check:ts": "tsc --noEmit",
    "export": "next build && next export",
    "dev": "next dev",
    "build": "next build",
    "start": "next start"
  },
  "dependencies": {
    "@primer/octicons-react": "^17.10.0",
    "body-scroll-lock": "^4.0.0-beta.0",
    "classnames": "^2.3.2",
    "focus-trap-react": "^10.0.2",
    "focus-visible": "^5.2.0",
    "hast-util-sanitize": "^4.0.0",
    "next": "^13.1.1",
    "nprogress": "^0.2.0",
    "prism-react-renderer": "^1.3.5",
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "remark-react": "^9.0.1",
    "swiper": "^8.4.5",
    "use-media": "^1.4.0",
    "wicg-inert": "^3.1.2"
  },
  "devDependencies": {
    "@marp-team/marp-core": "^3.6.0",
    "@next/bundle-analyzer": "^13.1.1",
    "@svgr/webpack": "^6.5.1",
    "@types/classnames": "^2.3.1",
    "@types/react": "^18.0.26",
    "@types/resize-observer-browser": "^0.1.7",
    "@types/webpack-env": "^1.18.0",
    "autoprefixer": "^10.4.13",
    "dot-prop": "^7.2.0",
    "eslint-config-next": "^13.1.1",
    "gray-matter": "^4.0.3",
    "hast-util-whitespace": "^2.0.0",
    "node-fetch": "^3.3.0",
    "null-loader": "^4.0.1",
    "postcss": "^8.4.20",
    "postcss-flexbugs-fixes": "^5.0.2",
    "postcss-import-url": "^7.2.0",
    "postcss-preset-env": "^7.8.3",
    "postcss-url": "^10.1.3",
    "prettier-plugin-tailwindcss": "^0.2.1",
    "remark-gfm": "^3.0.0",
    "remark-parse": "^10.0.0",
    "remark-slug": "^7.0.0",
    "styled-jsx-plugin-postcss": "^4.0.1",
    "tailwindcss": "^3.2.4",
    "unified": "^10.1.2",
    "unist-util-remove-position": "^4.0.1",
    "unist-util-visit": "^4.1.1",
    "yaml-loader": "^0.8.0"
  }
}

```

`/Users/nikola/dev/marp/website/global.d.ts`:

```ts
import {} from 'react'

declare module 'react' {
  interface HTMLAttributes {
    inert?: ''
  }
}

```

`/Users/nikola/dev/marp/website/tsconfig.json`:

```json
{
  "extends": "../tsconfig.json",
  "compilerOptions": {
    "allowJs": true,
    "baseUrl": ".",
    "downlevelIteration": true,
    "isolatedModules": true,
    "jsx": "preserve",
    "lib": ["dom", "dom.iterable", "esnext"],
    "module": "esnext",
    "moduleResolution": "node",
    "noEmit": true,
    "target": "es5",
    "incremental": true
  },
  "include": [
    "next-env.d.ts",
    "global.d.ts",
    "assets.d.ts",
    "**/*.ts",
    "**/*.tsx"
  ],
  "exclude": ["node_modules"]
}

```

`/Users/nikola/dev/marp/website/assets.d.ts`:

```ts
declare module '*.yaml' {
  const yaml: any
  export = yaml
}

```

`/Users/nikola/dev/marp/website/postcss.config.js`:

```js
const path = require('path')
const remoteInlineCache = new Map()

const encodeForInlining = (buffer) =>
  encodeURIComponent(buffer.toString('utf8').replace(/\n+/g, ''))
    .replace(/%20/g, ' ')
    .replace(/#/g, '%23')

module.exports = {
  plugins: {
    'postcss-flexbugs-fixes': {},
    tailwindcss: {},
    'postcss-preset-env': {
      autoprefixer: { flexbox: 'no-2009' },
      stage: 3,
      features: {
        'custom-properties': false,
        'focus-visible-pseudo-class': true,
      },
    },
    'postcss-url': [
      {
        filter: '**/assets/**/*.svg',
        basePath: path.resolve(__dirname, './public'),
        url: 'inline',
        maxSize: 1,
      },
      {
        filter: ({ url }) => url.startsWith('https://icongr.am/'),
        url: async ({ url }) => {
          if (remoteInlineCache.has(url)) return remoteInlineCache.get(url)

          const { default: fetch } = await import('node-fetch')
          const response = await fetch(url)

          if (!response.ok) {
            console.error(`Failed to make inline the remote URL: ${url}`)
            return url
          }

          const buffer = await response.buffer()
          const mimeType =
            response.headers.get('Content-Type') || 'application/octet-stream'

          const svg = [
            `data:${mimeType};base64,${buffer.toString('base64')}`,
            `data:${mimeType},${encodeForInlining(buffer)}`,
          ].sort((a, b) => a.length - b.length)[0]

          remoteInlineCache.set(url, svg)
          return svg
        },
      },
    ],
    [require.resolve('./css/plugin-rem')]: {},
  },
}

```

`/Users/nikola/dev/marp/website/pages/index.tsx`:

```tsx
import { InferGetStaticPropsType } from 'next'
import { Layout } from 'components/Layout'
import { generateRenderedMarp } from 'components/Marp'
import { Description } from 'components/top/Description'
import { Features } from 'components/top/Features'
import { GetStarted } from 'components/top/GetStarted'
import { Hero } from 'components/top/Hero'
import { absoluteUrl } from 'utils/url'

const exampleMarkdown = `
---
theme: gaia
_class: lead
paginate: true
backgroundColor: #fff
backgroundImage: url('${absoluteUrl('/assets/hero-background.svg')}')
---

![bg left:40% 80%](${absoluteUrl('/assets/marp.svg')})

# **Marp**

Markdown Presentation Ecosystem

https://marp.app/

---

# How to write slides

Split pages by horizontal ruler (\`---\`). It's very simple! :satisfied:

\`\`\`markdown
# Slide 1

foobar

---

# Slide 2

foobar
\`\`\`
`.trim()

export const getStaticProps = async () => ({
  props: { example: await generateRenderedMarp(exampleMarkdown) },
})

const Index = (props: InferGetStaticPropsType<typeof getStaticProps>) => (
  <Layout type="website">
    <Hero />
    <Description example={props.example} />
    <Features />
    <GetStarted />
  </Layout>
)

export default Index

```

`/Users/nikola/dev/marp/website/pages/404.tsx`:

```tsx
import { ArrowLeftIcon } from '@primer/octicons-react'
import { Button } from 'components/Button'
import { Layout } from 'components/Layout'

const error404 = () => (
  <Layout title={['404 Not Found']} noIndex>
    <section className="text-center">
      <div className="m-8 w-screen max-w-2xl sm:m-16">
        <h1 className="font-rounded text-4xl font-bold tracking-tighter text-gray-700">
          404 Not Found
        </h1>
        <hr className="my-6" />
        <p className="text-lg">Oops! The requested page could not be found.</p>
        <p className="mt-10">
          <Button
            className="w-full max-w-xs text-xs"
            onClick={() => window.history.back()}
            outline
            style={{ color: '#4a5568' }}
          >
            <span className="flex items-center justify-center text-lg">
              <ArrowLeftIcon className="mr-2 h-8 w-8" />
              Back to previous
            </span>
          </Button>
        </p>
      </div>
      <style jsx>{`
        section {
          @apply flex w-full items-center justify-center;

          background-image: url("data:image/svg+xml,%3csvg width='40' height='40' xmlns='http://www.w3.org/2000/svg'%3e%3cpath d='M0 40L40 0H20L0 20m40 20V20L20 40' fill='%23f0f0f0' fill-opacity='.2' fill-rule='evenodd'/%3e%3c/svg%3e");
          min-height: inherit;
        }
      `}</style>
    </section>
  </Layout>
)

export default error404

```

`/Users/nikola/dev/marp/website/pages/docs/[[...slug]].tsx`:

```tsx
import path from 'path'
import { getProperty } from 'dot-prop'
import {
  GetStaticPaths,
  GetStaticPropsContext,
  InferGetStaticPropsType,
} from 'next'
import { Typography } from 'components/Typography'
import { Layout } from 'components/docs/Layout'
import { parse, renderToReact } from 'utils/markdown'

const defaultSlug = ['introduction', 'whats-marp']
const docsCtx = () => require.context('docs', true, /\.md$/)

export const getStaticPaths: GetStaticPaths = async () => ({
  paths: [
    '/docs',
    ...docsCtx()
      .keys()
      .map((id) => path.join('/docs/', id).slice(0, -3)),
  ],
  fallback: false,
})

export const getStaticProps = async ({ params }: GetStaticPropsContext) => {
  // Manifest
  const { default: manifest } = await import('docs/manifest.yaml')

  // Page data
  const slug = ([] as string[]).concat(params?.slug ?? defaultSlug)
  if (slug[0] === 'docs') slug.splice(0, 1) // for webpack 5

  const { default: md } = await import(`docs/${path.join(...slug)}.md`)
  const { data, mdast } = await parse(md)

  // Breadcrumbs
  const breadcrumbs = slug.map((sl, i) => {
    const slugs = slug.slice(0, i + 1)
    const key = slugs.join('/')
    const data = getProperty(
      { pages: manifest },
      slugs.flatMap((s) => ['pages', s]).join('.'),
      undefined as Record<string, string> | undefined
    )
    const hasLink = docsCtx().keys().includes(`./${key}.md`)

    return {
      key,
      title: data?.title || sl,
      ...(hasLink ? { link: `/docs/${key}` } : {}),
    }
  })

  return { props: { breadcrumbs, data, manifest, mdast, slug } }
}

const Docs = ({
  breadcrumbs,
  manifest,
  mdast,
  slug,
}: InferGetStaticPropsType<typeof getStaticProps>) => (
  <Layout breadcrumbs={breadcrumbs} manifest={manifest} slug={slug}>
    {/* key is required to fix broken Google Translator built in Chrome */}
    <Typography key={slug.join('/')}>{renderToReact(mdast)}</Typography>
  </Layout>
)

export default Docs

```

`/Users/nikola/dev/marp/website/pages/_document.tsx`:

```tsx
import Document, { Html, Head, Main, NextScript } from 'next/document'

class MyDocument extends Document {
  render = () => (
    <Html lang="en">
      <Head>
        <link rel="icon" href="/favicon.png" type="image/png" />
        <link
          rel="apple-touch-icon"
          sizes="180x180"
          href="/apple-touch-icon-180x180.png"
        />
        <link
          href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&amp;family=Quicksand:wght@500;700&amp;display=swap"
          rel="stylesheet"
        />
      </Head>
      <body>
        <Main />
        <NextScript />
      </body>
    </Html>
  )
}

export default MyDocument

```

`/Users/nikola/dev/marp/website/pages/blog/[slug].tsx`:

```tsx
import { basename } from 'path'
import {
  GetStaticPaths,
  GetStaticPropsContext,
  InferGetStaticPropsType,
} from 'next'
import Link from 'next/link'
import { Layout } from 'components/Layout'
import { Title } from 'components/Title'
import { Typography } from 'components/Typography'
import { BlogHeader } from 'components/blog/BlogHeader'
import { parse, renderToReact } from 'utils/markdown'

export const getStaticPaths: GetStaticPaths = async () => ({
  paths: require
    .context('blog', false, /\.md$/)
    .keys()
    .map((id) => `/blog/${basename(id, '.md')}`),
  fallback: false,
})

export const getStaticProps = async ({ params }: GetStaticPropsContext) => {
  const slug = params?.slug as string
  const { default: md } = await import(`blog/${slug}.md`)
  const parsed = await parse(md)

  return {
    props: { markdown: { data: parsed.data, mdast: parsed.mdast }, slug },
  }
}

const Blog = ({
  markdown: { data, mdast },
  slug,
}: InferGetStaticPropsType<typeof getStaticProps>) => (
  <Layout
    activeItem="blog"
    description={data.description || ''}
    image={data.image}
    noIndex={!data.date}
    title={[data.title || slug, 'Blog']}
  >
    <Title>
      <Link href="/blog">Blog</Link>
    </Title>
    <div className="container mx-auto px-6 py-12">
      <BlogHeader
        title={data.title}
        date={data.date ? new Date(data.date) : undefined}
        author={data.author}
        github={data.github}
        slug={slug}
      />
      <article className="mx-auto mt-8 max-w-screen-lg">
        {data.image && (
          <figure className="my-12">
            <img
              src={data.image}
              alt={data.title}
              className="mx-auto block w-full max-w-screen-md bg-white shadow-xl"
            />
          </figure>
        )}
        <Typography>{renderToReact(mdast)}</Typography>
      </article>
    </div>
  </Layout>
)

export default Blog

```

`/Users/nikola/dev/marp/website/pages/blog.tsx`:

```tsx
import fs from 'fs'
import { basename } from 'path'
import { ArrowRightIcon } from '@primer/octicons-react'
import { InferGetStaticPropsType } from 'next'
import Head from 'next/head'
import Link from 'next/link'
import { Layout } from 'components/Layout'
import { Title } from 'components/Title'
import { Typography } from 'components/Typography'
import { formatDate, formatDateShort } from 'utils/date'
import { parse, parseMatter, renderToReact } from 'utils/markdown'
import { absoluteUrl } from 'utils/url'

const toJSON = (obj: any) => JSON.parse(JSON.stringify(obj))

const escapeEntities = (raw: string) =>
  raw.replace(/[&<>]/g, (matched) => `&#${matched.charCodeAt(0)};`)

export const getStaticProps = async () => {
  const ctx = require.context('blog', false, /^.[\\/][^\\/]*\.md$/)
  const mdMetas = await Promise.all(
    ctx.keys().map((id) => {
      const md = ctx(id)
      const { data, excerpt } = parseMatter(md)

      return (async () => ({
        data,
        excerpt: excerpt ? await parse(excerpt) : undefined,
        slug: basename(id, '.md'),
      }))()
    })
  )

  const articles = mdMetas.filter(({ data }) => data.date)
  articles.sort((a, b) => b.data.date.getTime() - a.data.date.getTime())

  // Generate RSS
  const rss = `
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <title>Blog | Marp</title>
    <link>${escapeEntities(absoluteUrl('/blog').toString())}</link>
    <description>Marp, Markdown Presentation Ecosystem, provides the great experience to create beautiful slide deck. You only have to focus writing your story in Markdown document.</description>
    <language>en</language>
    <lastBuildDate>${articles[0].data.date.toUTCString()}</lastBuildDate>
    <atom:link href="${absoluteUrl(
      '/blog/feed.xml'
    )}" rel="self" type="application/rss+xml"/>
    ${articles
      .map((article) =>
        `
      <item>
        <guid>${escapeEntities(
          absoluteUrl(`/blog/${article.slug}`).toString()
        )}</guid>
        <title>${escapeEntities(article.data.title)}</title>
        <link>${escapeEntities(
          absoluteUrl(`/blog/${article.slug}`).toString()
        )}</link>
        <description>${escapeEntities(article.data.description)}</description>
        <pubDate>${article.data.date.toUTCString()}</pubDate>
      </item>
    `.trim()
      )
      .join('')}
  </channel>
</rss>
  `.trim()

  await fs.promises.writeFile('./public/blog/feed.xml', rss)

  return {
    props: {
      articles: articles.map((article) =>
        toJSON({
          data: article.data,
          excerpt: article.excerpt?.mdast,
          slug: article.slug,
        })
      ),
    },
  }
}

const Blog = ({ articles }: InferGetStaticPropsType<typeof getStaticProps>) => (
  <Layout activeItem="blog" title={['Blog']}>
    <Title>
      <Link href="/blog">Blog</Link>
    </Title>
    <Head>
      <link
        rel="alternate"
        type="application/rss+xml"
        title="Blog | Marp"
        href={absoluteUrl(`/blog/feed.xml`).toString()}
      />
    </Head>
    <div className="container mx-auto max-w-screen-lg px-3 py-1">
      {articles.map((article) => {
        let summary: JSX.Element | string | undefined

        if (article.excerpt) {
          summary = (
            <Typography>
              {renderToReact(article.excerpt, { anchorLink: false })}
            </Typography>
          )
        } else if (article.data.description) {
          summary = article.data.description
        }

        const date = new Date(article.data.date)

        return (
          <div key={article.slug} className="article-container">
            <Link href={`/blog/${article.slug}`} legacyBehavior>
              <a className="article-container-link">
                <h1 className="sr-only">{article.data.title}</h1>
              </a>
            </Link>
            <div className="pointer-events-none relative">
              <h1 className="text-gradient text-3xl font-bold" aria-hidden>
                {article.data.title}
              </h1>
              <p className="mt-2 mb-4 border-b-2 pb-4 text-sm text-gray-600">
                <time dateTime={formatDateShort(date)}>{formatDate(date)}</time>
                {article.data.author && ` by ${article.data.author}`}
              </p>
              {summary && (
                <>
                  <div
                    className="article-summary flex flex-col lg:flex-row"
                    inert=""
                  >
                    {article.data.image && (
                      <figure className="mx-auto mb-6 lg:order-1 lg:mb-0 lg:ml-6 lg:w-full lg:max-w-[20rem]">
                        <img
                          src={article.data.image}
                          alt={article.data.title}
                          className="w-full max-w-[20rem] bg-white shadow-md lg:w-[100vw]"
                        />
                      </figure>
                    )}
                    <article className="flex-grow">{summary}</article>
                  </div>
                </>
              )}
              <p className="read-more">
                <ArrowRightIcon className="read-more-icon" />
                Read more...
              </p>
            </div>
          </div>
        )
      })}
      <style jsx>{`
        .article-container {
          @apply relative my-6 p-6;
        }
        .article-container-link {
          @apply absolute inset-0 rounded-lg transition-all duration-300;
        }

        @media not all and (hover: none) {
          .article-container-link:hover {
            @apply bg-white shadow-lg;
          }
          .article-container-link:hover:active {
            @apply duration-0 bg-white outline-none ring-1 ring-white ring-offset-2;
          }
          .article-container-link:hover + * .read-more {
            @apply text-marp-brand;
          }
        }

        .article-container-link:focus {
          @apply duration-0 bg-white outline-none ring-1 ring-white ring-offset-2;
        }

        .article-summary :global(a) {
          color: inherit;
        }

        .read-more {
          @apply mt-6 flex items-center justify-end text-right font-bold uppercase transition-colors duration-300;
        }

        .read-more :global(.read-more-icon) {
          @apply h-8 w-8;
        }

        @screen md {
          .article-container {
            @apply relative p-8;
          }
        }
      `}</style>
    </div>
  </Layout>
)

export default Blog

```

`/Users/nikola/dev/marp/website/pages/_app.tsx`:

```tsx
import { Router } from 'next/router'
import NProgress from 'nprogress'
import { FontFaceProvider, FontFaceRenderer } from 'utils/hooks/useFontFace'
import 'focus-visible'
import 'wicg-inert'
import 'nprogress/nprogress.css'
import 'swiper/css/bundle'
import 'css/index.css'

// NProgress
const translating = () => {
  NProgress.start()
  document.documentElement.classList.add('translating')
}

const translated = () => {
  NProgress.done()
  setTimeout(
    () => document.documentElement.classList.remove('translating'),
    250
  )
}

Router.events.on('routeChangeStart', translating)
Router.events.on('routeChangeComplete', translated)
Router.events.on('routeChangeError', translated)

NProgress.configure({ showSpinner: false, trickleSpeed: 350 })

// Make resilience from manipulating DOM by Google translator
// https://github.com/facebook/react/issues/11538
if (typeof Node === 'function' && Node.prototype) {
  const { removeChild, insertBefore } = Node.prototype

  Node.prototype.removeChild = function <T extends Node>(child: T): T {
    if (child.parentNode !== this) {
      if (console) {
        console.error(
          'Cannot remove a child from a different parent',
          child,
          this
        )
      }
      return child
    }
    return removeChild.call(this, child) as T
  }
  Node.prototype.insertBefore = function <T extends Node>(
    newNode: T,
    referenceNode: Node | null
  ): T {
    if (referenceNode && referenceNode.parentNode !== this) {
      if (console) {
        console.error(
          'Cannot insert before a reference node from a different parent',
          referenceNode,
          this
        )
      }
      return newNode
    }
    return insertBefore.call(this, newNode, referenceNode) as T
  }
}

const App = ({ Component, pageProps }) => (
  <FontFaceProvider>
    <FontFaceRenderer />
    <Component {...pageProps} />
  </FontFaceProvider>
)

export default App

```

`/Users/nikola/dev/marp/README.md`:

```md
<div align="center">
  <p>
    <img src="marp.png#gh-light-mode-only" alt="Marp" width="450" />
    <img src="marp-dark.png#gh-dark-mode-only" alt="Marp" width="450" />
  </p>
  <p>
    <strong>Marp</strong>: Markdown Presentation Ecosystem
  </p>
</div>

**Marp** is the ecosystem to write your presentation with plain Markdown.

<div align="center">

### [🌐 Website ▶︎](https://marp.app)&emsp;|&emsp;[💬 Discussion forum ▶︎](https://github.com/marp-team/marp/discussions)&emsp;|&emsp;[😎 Awesome list ▶︎](https://github.com/marp-team/awesome-marp)

</div>

## Marp family

Our project is spread over many repos in order to focus on a limited scope per repository.

This repo (**[marp-team/marp][marp]**) is an entrance to the Marp family, and places [our website](https://marp.app/) in `/website`.

### Framework / Core

|                       Name | Description                                                                                 | Release                                                   |
| -------------------------: | :------------------------------------------------------------------------------------------ | :-------------------------------------------------------- |
|               **[Marpit]** | The skinny framework for creating slide deck from Markdown. ([marpit.marp.app])             | [![@marp-team/marpit][badge-marpit]][marpit-npm]          |
| **[Marp Core][marp-core]** | The core of Marp converter with practical features and [built-in themes][marp-core-themes]. | [![@marp-team/marp-core][badge-marp-core]][marp-core-npm] |

### Apps

|                     Name | Description                                                                                      | Release                                                |
| -----------------------: | :----------------------------------------------------------------------------------------------- | :----------------------------------------------------- |
| **[Marp CLI][marp-cli]** | [Marp Core][marp-core] / [Marpit]'s CLI interface to convert into HTML, PDF, PPTX, and image(s). | [![@marp-team/marp-cli][badge-marp-cli]][marp-cli-npm] |

### Integrations

|                                Name | Description                                                                       | Release                                                     |
| ----------------------------------: | :-------------------------------------------------------------------------------- | :---------------------------------------------------------- |
| **[Marp for VS Code][marp-vscode]** | A [VS Code][vscode] extension to preview the slide deck written in Marp Markdown. | [![VS Marketplace][badge-marp-vscode]][marp-vscode-release] |

<details>
<summary>See outdated/inactive projects...</summary><br />

|                     Name | Description                                                      | Release                                                      |
| -----------------------: | :--------------------------------------------------------------- | :----------------------------------------------------------- |
|     [Marp Web][marp-web] | The Web interface of Marp based on [PWA] and [Preact] framework. | [![tech demo][badge-marp-web]][marp-web-site]                |
| [Marp React][marp-react] | Marp renderer component for [React].                             | [![@marp-team/marp-react][badge-marp-react]][marp-react-npm] |
|     [Marp Vue][marp-vue] | Marp renderer component for [Vue].                               | [![@marp-team/marp-vue][badge-marp-vue]][marp-vue-npm]       |

And there is a gravesite of classic Marp app in https://github.com/yhatt/marp. :ghost:

[marp-web]: https://github.com/marp-team/marp-web
[marp-react]: https://github.com/marp-team/marp-react
[marp-vue]: https://github.com/marp-team/marp-vue
[pwa]: https://en.wikipedia.org/wiki/Progressive_Web_Apps
[preact]: https://preactjs.com/
[react]: https://reactjs.org/
[vue]: https://vuejs.org/
[marp-web-site]: https://web.marp.app/
[marp-react-npm]: https://www.npmjs.com/package/@marp-team/marp-react
[marp-vue-npm]: https://www.npmjs.com/package/@marp-team/marp-vue
[badge-marp-web]: https://img.shields.io/badge/%E2%80%8B-tech%20demo-%230288d1.svg?style=flat-square&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA4AAAAOCAYAAAAfSC3RAAAAUUlEQVQokWNgGD6AqePif3Sx9B2PMcQwNKFrTN/x+D9ejTBNyBphmnBqRNYE04isCatGdE1MHRf/o2vC0IhNE1PaXPwacWnCqxGfJoI2Dn4AAN0ZrMM1VUFvAAAAAElFTkSuQmCC
[badge-marp-react]: https://img.shields.io/npm/v/@marp-team/marp-react.svg?style=flat-square&logo=npm
[badge-marp-vue]: https://img.shields.io/npm/v/@marp-team/marp-vue.svg?style=flat-square&logo=npm

</details>

[yhatt/marp]: https://github.com/yhatt/marp
[marp]: https://github.com/marp-team/marp
[marpit]: https://github.com/marp-team/marpit
[marp-core]: https://github.com/marp-team/marp-core
[marp-core-themes]: https://github.com/marp-team/marp-core/tree/main/themes
[marp-cli]: https://github.com/marp-team/marp-cli
[marp-vscode]: https://github.com/marp-team/marp-vscode
[vscode]: https://code.visualstudio.com/
[marpit.marp.app]: https://marpit.marp.app/
[marpit-npm]: https://www.npmjs.com/package/@marp-team/marpit
[marp-core-npm]: https://www.npmjs.com/package/@marp-team/marp-core
[marp-cli-npm]: https://www.npmjs.com/package/@marp-team/marp-cli
[marp-vscode-release]: https://marketplace.visualstudio.com/items?itemName=marp-team.marp-vscode
[badge-marpit]: https://img.shields.io/npm/v/@marp-team/marpit.svg?style=flat-square&logo=npm
[badge-marp-core]: https://img.shields.io/npm/v/@marp-team/marp-core.svg?style=flat-square&logo=npm
[badge-marp-cli]: https://img.shields.io/npm/v/@marp-team/marp-cli.svg?style=flat-square&logo=npm
[badge-marp-vscode]: https://img.shields.io/visual-studio-marketplace/v/marp-team.marp-vscode.svg?style=flat-square&logo=visual-studio-code&label=Marketplace

## Ecosystem

Marp ecosystem has a lot of cool stuffs for making awesome presentation. Check out **[the awesome list of Marp](https://github.com/marp-team/awesome-marp)**. 😎

## Contributing

Marp and sub-projects are following the [contributing guideline of marp-team][contributing]. Please read this before starting work in our projects.

[contributing]: https://github.com/marp-team/.github/blob/master/CONTRIBUTING.md

## Author

Managed by [@marp-team](https://github.com/marp-team).

- <img src="https://github.com/yhatt.png" width="16" height="16"/> Yuki Hattori ([@yhatt](https://github.com/yhatt))

## Sponsors

We are supported by them! Thanks for our sponsors! :heart:

<!-- [NOTE] Sort sponsors by name when modify. -->

### Organization sponsors

<!-- Logo and links for top-tier sponsors (The image should be up to 400px on a side) -->

<p align="center">
  <a href="https://github.com/markslides"><img src="https://github.com/markslides.png" width="64" height="64" alt="@markslides" valign="middle" hspace="4" /></a>
</p>

<!-- [TODO] For mid-tier sponsors: As the same format as personal sponsors, add small icons and links to GitHub organization. -->
<!--
<p>
  <a href="https://github.com/xxxxxx"><img src="https://github.com/xxxxxx.png" width="32" height="32" alt="xxxxxx" /></a>
</p>
-->

### Personal sponsors

<!-- [TODO] Currently shows maintainer's sponsors. We should show sponsors for all Marp team members in future. -->

<p align="center">
  <img alt="Personal sponsors" src="https://yhatt.github.io/yhatt/sponsors.svg" />
</p>

> Do you want to sponsor [the member of Marp team](https://github.com/orgs/marp-team/people)? See [GitHub Sponsors](https://github.com/sponsors) profile(s) from "♥︎ Sponsor" button [at the top of repository](https://github.com/marp-team/marp).

## License

[MIT License](LICENSE)

```

`/Users/nikola/dev/marp/yarn.lock`:

```lock
# THIS IS AN AUTOGENERATED FILE. DO NOT EDIT THIS FILE DIRECTLY.
# yarn lockfile v1


"@ampproject/remapping@^2.1.0":
  version "2.2.0"
  resolved "https://registry.yarnpkg.com/@ampproject/remapping/-/remapping-2.2.0.tgz#56c133824780de3174aed5ab6834f3026790154d"
  integrity sha512-qRmjj8nj9qmLTQXXmaR1cck3UXSRMPrbsLJAasZpF+t3riI71BXed5ebIOYwQntykeZuhjsdweEc9BxH5Jc26w==
  dependencies:
    "@jridgewell/gen-mapping" "^0.1.0"
    "@jridgewell/trace-mapping" "^0.3.9"

"@azure/abort-controller@^1.0.0":
  version "1.1.0"
  resolved "https://registry.yarnpkg.com/@azure/abort-controller/-/abort-controller-1.1.0.tgz#788ee78457a55af8a1ad342acb182383d2119249"
  integrity sha512-TrRLIoSQVzfAJX9H1JeFjzAoDGcoK1IYX1UImfceTZpsyYfWr09Ss1aHW1y5TrrR3iq6RZLBwJ3E24uwPhwahw==
  dependencies:
    tslib "^2.2.0"

"@azure/core-asynciterator-polyfill@^1.0.0":
  version "1.0.2"
  resolved "https://registry.yarnpkg.com/@azure/core-asynciterator-polyfill/-/core-asynciterator-polyfill-1.0.2.tgz#0dd3849fb8d97f062a39db0e5cadc9ffaf861fec"
  integrity sha512-3rkP4LnnlWawl0LZptJOdXNrT/fHp2eQMadoasa6afspXdpGrtPZuAQc2PD0cpgyuoXtUWyC3tv7xfntjGS5Dw==

"@azure/core-auth@^1.3.0":
  version "1.4.0"
  resolved "https://registry.yarnpkg.com/@azure/core-auth/-/core-auth-1.4.0.tgz#6fa9661c1705857820dbc216df5ba5665ac36a9e"
  integrity sha512-HFrcTgmuSuukRf/EdPmqBrc5l6Q5Uu+2TbuhaKbgaCpP2TfAeiNaQPAadxO+CYBRHGUzIDteMAjFspFLDLnKVQ==
  dependencies:
    "@azure/abort-controller" "^1.0.0"
    tslib "^2.2.0"

"@azure/core-http@^1.1.1", "@azure/core-http@^1.2.0":
  version "1.2.6"
  resolved "https://registry.yarnpkg.com/@azure/core-http/-/core-http-1.2.6.tgz#9cd508418572d2062fd3175274219438772bdb65"
  integrity sha512-odtH7UMKtekc5YQ86xg9GlVHNXR6pq2JgJ5FBo7/jbOjNGdBqcrIVrZx2bevXVJz/uUTSx6vUf62gzTXTfqYSQ==
  dependencies:
    "@azure/abort-controller" "^1.0.0"
    "@azure/core-asynciterator-polyfill" "^1.0.0"
    "@azure/core-auth" "^1.3.0"
    "@azure/core-tracing" "1.0.0-preview.11"
    "@azure/logger" "^1.0.0"
    "@types/node-fetch" "^2.5.0"
    "@types/tunnel" "^0.0.1"
    form-data "^3.0.0"
    node-fetch "^2.6.0"
    process "^0.11.10"
    tough-cookie "^4.0.0"
    tslib "^2.2.0"
    tunnel "^0.0.6"
    uuid "^8.3.0"
    xml2js "^0.4.19"

"@azure/core-lro@^1.0.2":
  version "1.0.5"
  resolved "https://registry.yarnpkg.com/@azure/core-lro/-/core-lro-1.0.5.tgz#856a2cb6a9bec739ee9cde33a27cc28f81ac0522"
  integrity sha512-0EFCFZxARrIoLWMIRt4vuqconRVIO2Iin7nFBfJiYCCbKp5eEmxutNk8uqudPmG0XFl5YqlVh68/al/vbE5OOg==
  dependencies:
    "@azure/abort-controller" "^1.0.0"
    "@azure/core-http" "^1.2.0"
    "@azure/core-tracing" "1.0.0-preview.11"
    events "^3.0.0"
    tslib "^2.0.0"

"@azure/core-paging@^1.1.1":
  version "1.4.0"
  resolved "https://registry.yarnpkg.com/@azure/core-paging/-/core-paging-1.4.0.tgz#b04a73ad18149733a848c3089a5e5ed144592338"
  integrity sha512-tabFtZTg8D9XqZKEfNUOGh63SuYeOxmvH4GDcOJN+R1bZWZ1FZskctgY9Pmuwzhn+0Xvq9rmimK9hsvtLkeBsw==
  dependencies:
    tslib "^2.2.0"

"@azure/core-tracing@1.0.0-preview.11":
  version "1.0.0-preview.11"
  resolved "https://registry.yarnpkg.com/@azure/core-tracing/-/core-tracing-1.0.0-preview.11.tgz#bdfb2ba73cd6c39b7d6c207b9522eb98e08b4ddd"
  integrity sha512-frF0pJc9HTmKncVokhBxCqipjbql02DThQ1ZJ9wLi7SDMLdPAFyDI5xZNzX5guLz+/DtPkY+SGK2li9FIXqshQ==
  dependencies:
    "@opencensus/web-types" "0.0.7"
    "@opentelemetry/api" "1.0.0-rc.0"
    tslib "^2.0.0"

"@azure/core-tracing@1.0.0-preview.8":
  version "1.0.0-preview.8"
  resolved "https://registry.yarnpkg.com/@azure/core-tracing/-/core-tracing-1.0.0-preview.8.tgz#1e0ff857e855edb774ffd33476003c27b5bb2705"
  integrity sha512-ZKUpCd7Dlyfn7bdc+/zC/sf0aRIaNQMDuSj2RhYRFe3p70hVAnYGp3TX4cnG2yoEALp/LTj/XnZGQ8Xzf6Ja/Q==
  dependencies:
    "@opencensus/web-types" "0.0.7"
    "@opentelemetry/api" "^0.6.1"
    tslib "^1.10.0"

"@azure/logger@^1.0.0":
  version "1.0.3"
  resolved "https://registry.yarnpkg.com/@azure/logger/-/logger-1.0.3.tgz#6e36704aa51be7d4a1bae24731ea580836293c96"
  integrity sha512-aK4s3Xxjrx3daZr3VylxejK3vG5ExXck5WOHDJ8in/k9AqlfIyFMMT1uG7u8mNjX+QRILTIn0/Xgschfh/dQ9g==
  dependencies:
    tslib "^2.2.0"

"@azure/storage-blob@12.1.2":
  version "12.1.2"
  resolved "https://registry.yarnpkg.com/@azure/storage-blob/-/storage-blob-12.1.2.tgz#046d146a3bd2622b61d6bdc5708955893a5b4f04"
  integrity sha512-PCHgG4r3xLt5FaFj+uiMqrRpuzD3TD17cvxCeA1JKK2bJEf8b07H3QRLQVf0DM1MmvYY8FgQagkWZTp+jr9yew==
  dependencies:
    "@azure/abort-controller" "^1.0.0"
    "@azure/core-http" "^1.1.1"
    "@azure/core-lro" "^1.0.2"
    "@azure/core-paging" "^1.1.1"
    "@azure/core-tracing" "1.0.0-preview.8"
    "@azure/logger" "^1.0.0"
    "@opentelemetry/api" "^0.6.1"
    events "^3.0.0"
    tslib "^1.10.0"

"@babel/code-frame@^7.0.0", "@babel/code-frame@^7.18.6":
  version "7.18.6"
  resolved "https://registry.yarnpkg.com/@babel/code-frame/-/code-frame-7.18.6.tgz#3b25d38c89600baa2dcc219edfa88a74eb2c427a"
  integrity sha512-TDCmlK5eOvH+eH7cdAFlNXeVJqWIQ7gW9tY1GJIpUtFb6CmjVyq2VM3u71bOyR8CRihcCgMUYoDNyLXao3+70Q==
  dependencies:
    "@babel/highlight" "^7.18.6"

"@babel/compat-data@^7.17.7", "@babel/compat-data@^7.20.1", "@babel/compat-data@^7.20.5":
  version "7.20.10"
  resolved "https://registry.yarnpkg.com/@babel/compat-data/-/compat-data-7.20.10.tgz#9d92fa81b87542fff50e848ed585b4212c1d34ec"
  integrity sha512-sEnuDPpOJR/fcafHMjpcpGN5M2jbUGUHwmuWKM/YdPzeEDJg8bgmbcWQFUfE32MQjti1koACvoPVsDe8Uq+idg==

"@babel/core@^7.19.6":
  version "7.20.7"
  resolved "https://registry.yarnpkg.com/@babel/core/-/core-7.20.7.tgz#37072f951bd4d28315445f66e0ec9f6ae0c8c35f"
  integrity sha512-t1ZjCluspe5DW24bn2Rr1CDb2v9rn/hROtg9a2tmd0+QYf4bsloYfLQzjG4qHPNMhWtKdGC33R5AxGR2Af2cBw==
  dependencies:
    "@ampproject/remapping" "^2.1.0"
    "@babel/code-frame" "^7.18.6"
    "@babel/generator" "^7.20.7"
    "@babel/helper-compilation-targets" "^7.20.7"
    "@babel/helper-module-transforms" "^7.20.7"
    "@babel/helpers" "^7.20.7"
    "@babel/parser" "^7.20.7"
    "@babel/template" "^7.20.7"
    "@babel/traverse" "^7.20.7"
    "@babel/types" "^7.20.7"
    convert-source-map "^1.7.0"
    debug "^4.1.0"
    gensync "^1.0.0-beta.2"
    json5 "^2.2.1"
    semver "^6.3.0"

"@babel/generator@^7.20.7":
  version "7.20.7"
  resolved "https://registry.yarnpkg.com/@babel/generator/-/generator-7.20.7.tgz#f8ef57c8242665c5929fe2e8d82ba75460187b4a"
  integrity sha512-7wqMOJq8doJMZmP4ApXTzLxSr7+oO2jroJURrVEp6XShrQUObV8Tq/D0NCcoYg2uHqUrjzO0zwBjoYzelxK+sw==
  dependencies:
    "@babel/types" "^7.20.7"
    "@jridgewell/gen-mapping" "^0.3.2"
    jsesc "^2.5.1"

"@babel/helper-annotate-as-pure@^7.18.6":
  version "7.18.6"
  resolved "https://registry.yarnpkg.com/@babel/helper-annotate-as-pure/-/helper-annotate-as-pure-7.18.6.tgz#eaa49f6f80d5a33f9a5dd2276e6d6e451be0a6bb"
  integrity sha512-duORpUiYrEpzKIop6iNbjnwKLAKnJ47csTyRACyEmWj0QdUrm5aqNJGHSSEQSUAvNW0ojX0dOmK9dZduvkfeXA==
  dependencies:
    "@babel/types" "^7.18.6"

"@babel/helper-builder-binary-assignment-operator-visitor@^7.18.6":
  version "7.18.9"
  resolved "https://registry.yarnpkg.com/@babel/helper-builder-binary-assignment-operator-visitor/-/helper-builder-binary-assignment-operator-visitor-7.18.9.tgz#acd4edfd7a566d1d51ea975dff38fd52906981bb"
  integrity sha512-yFQ0YCHoIqarl8BCRwBL8ulYUaZpz3bNsA7oFepAzee+8/+ImtADXNOmO5vJvsPff3qi+hvpkY/NYBTrBQgdNw==
  dependencies:
    "@babel/helper-explode-assignable-expression" "^7.18.6"
    "@babel/types" "^7.18.9"

"@babel/helper-compilation-targets@^7.17.7", "@babel/helper-compilation-targets@^7.18.9", "@babel/helper-compilation-targets@^7.20.0", "@babel/helper-compilation-targets@^7.20.7":
  version "7.20.7"
  resolved "https://registry.yarnpkg.com/@babel/helper-compilation-targets/-/helper-compilation-targets-7.20.7.tgz#a6cd33e93629f5eb473b021aac05df62c4cd09bb"
  integrity sha512-4tGORmfQcrc+bvrjb5y3dG9Mx1IOZjsHqQVUz7XCNHO+iTmqxWnVg3KRygjGmpRLJGdQSKuvFinbIb0CnZwHAQ==
  dependencies:
    "@babel/compat-data" "^7.20.5"
    "@babel/helper-validator-option" "^7.18.6"
    browserslist "^4.21.3"
    lru-cache "^5.1.1"
    semver "^6.3.0"

"@babel/helper-create-class-features-plugin@^7.18.6", "@babel/helper-create-class-features-plugin@^7.20.5", "@babel/helper-create-class-features-plugin@^7.20.7":
  version "7.20.7"
  resolved "https://registry.yarnpkg.com/@babel/helper-create-class-features-plugin/-/helper-create-class-features-plugin-7.20.7.tgz#d0e1f8d7e4ed5dac0389364d9c0c191d948ade6f"
  integrity sha512-LtoWbDXOaidEf50hmdDqn9g8VEzsorMexoWMQdQODbvmqYmaF23pBP5VNPAGIFHsFQCIeKokDiz3CH5Y2jlY6w==
  dependencies:
    "@babel/helper-annotate-as-pure" "^7.18.6"
    "@babel/helper-environment-visitor" "^7.18.9"
    "@babel/helper-function-name" "^7.19.0"
    "@babel/helper-member-expression-to-functions" "^7.20.7"
    "@babel/helper-optimise-call-expression" "^7.18.6"
    "@babel/helper-replace-supers" "^7.20.7"
    "@babel/helper-split-export-declaration" "^7.18.6"

"@babel/helper-create-regexp-features-plugin@^7.18.6", "@babel/helper-create-regexp-features-plugin@^7.20.5":
  version "7.20.5"
  resolved "https://registry.yarnpkg.com/@babel/helper-create-regexp-features-plugin/-/helper-create-regexp-features-plugin-7.20.5.tgz#5ea79b59962a09ec2acf20a963a01ab4d076ccca"
  integrity sha512-m68B1lkg3XDGX5yCvGO0kPx3v9WIYLnzjKfPcQiwntEQa5ZeRkPmo2X/ISJc8qxWGfwUr+kvZAeEzAwLec2r2w==
  dependencies:
    "@babel/helper-annotate-as-pure" "^7.18.6"
    regexpu-core "^5.2.1"

"@babel/helper-define-polyfill-provider@^0.3.3":
  version "0.3.3"
  resolved "https://registry.yarnpkg.com/@babel/helper-define-polyfill-provider/-/helper-define-polyfill-provider-0.3.3.tgz#8612e55be5d51f0cd1f36b4a5a83924e89884b7a"
  integrity sha512-z5aQKU4IzbqCC1XH0nAqfsFLMVSo22SBKUc0BxGrLkolTdPTructy0ToNnlO2zA4j9Q/7pjMZf0DSY+DSTYzww==
  dependencies:
    "@babel/helper-compilation-targets" "^7.17.7"
    "@babel/helper-plugin-utils" "^7.16.7"
    debug "^4.1.1"
    lodash.debounce "^4.0.8"
    resolve "^1.14.2"
    semver "^6.1.2"

"@babel/helper-environment-visitor@^7.18.9":
  version "7.18.9"
  resolved "https://registry.yarnpkg.com/@babel/helper-environment-visitor/-/helper-environment-visitor-7.18.9.tgz#0c0cee9b35d2ca190478756865bb3528422f51be"
  integrity sha512-3r/aACDJ3fhQ/EVgFy0hpj8oHyHpQc+LPtJoY9SzTThAsStm4Ptegq92vqKoE3vD706ZVFWITnMnxucw+S9Ipg==

"@babel/helper-explode-assignable-expression@^7.18.6":
  version "7.18.6"
  resolved "https://registry.yarnpkg.com/@babel/helper-explode-assignable-expression/-/helper-explode-assignable-expression-7.18.6.tgz#41f8228ef0a6f1a036b8dfdfec7ce94f9a6bc096"
  integrity sha512-eyAYAsQmB80jNfg4baAtLeWAQHfHFiR483rzFK+BhETlGZaQC9bsfrugfXDCbRHLQbIA7U5NxhhOxN7p/dWIcg==
  dependencies:
    "@babel/types" "^7.18.6"

"@babel/helper-function-name@^7.18.9", "@babel/helper-function-name@^7.19.0":
  version "7.19.0"
  resolved "https://registry.yarnpkg.com/@babel/helper-function-name/-/helper-function-name-7.19.0.tgz#941574ed5390682e872e52d3f38ce9d1bef4648c"
  integrity sha512-WAwHBINyrpqywkUH0nTnNgI5ina5TFn85HKS0pbPDfxFfhyR/aNQEn4hGi1P1JyT//I0t4OgXUlofzWILRvS5w==
  dependencies:
    "@babel/template" "^7.18.10"
    "@babel/types" "^7.19.0"

"@babel/helper-hoist-variables@^7.18.6":
  version "7.18.6"
  resolved "https://registry.yarnpkg.com/@babel/helper-hoist-variables/-/helper-hoist-variables-7.18.6.tgz#d4d2c8fb4baeaa5c68b99cc8245c56554f926678"
  integrity sha512-UlJQPkFqFULIcyW5sbzgbkxn2FKRgwWiRexcuaR8RNJRy8+LLveqPjwZV/bwrLZCN0eUHD/x8D0heK1ozuoo6Q==
  dependencies:
    "@babel/types" "^7.18.6"

"@babel/helper-member-expression-to-functions@^7.20.7":
  version "7.20.7"
  resolved "https://registry.yarnpkg.com/@babel/helper-member-expression-to-functions/-/helper-member-expression-to-functions-7.20.7.tgz#a6f26e919582275a93c3aa6594756d71b0bb7f05"
  integrity sha512-9J0CxJLq315fEdi4s7xK5TQaNYjZw+nDVpVqr1axNGKzdrdwYBD5b4uKv3n75aABG0rCCTK8Im8Ww7eYfMrZgw==
  dependencies:
    "@babel/types" "^7.20.7"

"@babel/helper-module-imports@^7.18.6":
  version "7.18.6"
  resolved "https://registry.yarnpkg.com/@babel/helper-module-imports/-/helper-module-imports-7.18.6.tgz#1e3ebdbbd08aad1437b428c50204db13c5a3ca6e"
  integrity sha512-0NFvs3VkuSYbFi1x2Vd6tKrywq+z/cLeYC/RJNFrIX/30Bf5aiGYbtvGXolEktzJH8o5E5KJ3tT+nkxuuZFVlA==
  dependencies:
    "@babel/types" "^7.18.6"

"@babel/helper-module-transforms@^7.18.6", "@babel/helper-module-transforms@^7.20.11", "@babel/helper-module-transforms@^7.20.7":
  version "7.20.11"
  resolved "https://registry.yarnpkg.com/@babel/helper-module-transforms/-/helper-module-transforms-7.20.11.tgz#df4c7af713c557938c50ea3ad0117a7944b2f1b0"
  integrity sha512-uRy78kN4psmji1s2QtbtcCSaj/LILFDp0f/ymhpQH5QY3nljUZCaNWz9X1dEj/8MBdBEFECs7yRhKn8i7NjZgg==
  dependencies:
    "@babel/helper-environment-visitor" "^7.18.9"
    "@babel/helper-module-imports" "^7.18.6"
    "@babel/helper-simple-access" "^7.20.2"
    "@babel/helper-split-export-declaration" "^7.18.6"
    "@babel/helper-validator-identifier" "^7.19.1"
    "@babel/template" "^7.20.7"
    "@babel/traverse" "^7.20.10"
    "@babel/types" "^7.20.7"

"@babel/helper-optimise-call-expression@^7.18.6":
  version "7.18.6"
  resolved "https://registry.yarnpkg.com/@babel/helper-optimise-call-expression/-/helper-optimise-call-expression-7.18.6.tgz#9369aa943ee7da47edab2cb4e838acf09d290ffe"
  integrity sha512-HP59oD9/fEHQkdcbgFCnbmgH5vIQTJbxh2yf+CdM89/glUNnuzr87Q8GIjGEnOktTROemO0Pe0iPAYbqZuOUiA==
  dependencies:
    "@babel/types" "^7.18.6"

"@babel/helper-plugin-utils@^7.0.0", "@babel/helper-plugin-utils@^7.10.4", "@babel/helper-plugin-utils@^7.12.13", "@babel/helper-plugin-utils@^7.14.5", "@babel/helper-plugin-utils@^7.16.7", "@babel/helper-plugin-utils@^7.18.6", "@babel/helper-plugin-utils@^7.18.9", "@babel/helper-plugin-utils@^7.19.0", "@babel/helper-plugin-utils@^7.20.2", "@babel/helper-plugin-utils@^7.8.0", "@babel/helper-plugin-utils@^7.8.3":
  version "7.20.2"
  resolved "https://registry.yarnpkg.com/@babel/helper-plugin-utils/-/helper-plugin-utils-7.20.2.tgz#d1b9000752b18d0877cff85a5c376ce5c3121629"
  integrity sha512-8RvlJG2mj4huQ4pZ+rU9lqKi9ZKiRmuvGuM2HlWmkmgOhbs6zEAw6IEiJ5cQqGbDzGZOhwuOQNtZMi/ENLjZoQ==

"@babel/helper-remap-async-to-generator@^7.18.9":
  version "7.18.9"
  resolved "https://registry.yarnpkg.com/@babel/helper-remap-async-to-generator/-/helper-remap-async-to-generator-7.18.9.tgz#997458a0e3357080e54e1d79ec347f8a8cd28519"
  integrity sha512-dI7q50YKd8BAv3VEfgg7PS7yD3Rtbi2J1XMXaalXO0W0164hYLnh8zpjRS0mte9MfVp/tltvr/cfdXPvJr1opA==
  dependencies:
    "@babel/helper-annotate-as-pure" "^7.18.6"
    "@babel/helper-environment-visitor" "^7.18.9"
    "@babel/helper-wrap-function" "^7.18.9"
    "@babel/types" "^7.18.9"

"@babel/helper-replace-supers@^7.18.6", "@babel/helper-replace-supers@^7.20.7":
  version "7.20.7"
  resolved "https://registry.yarnpkg.com/@babel/helper-replace-supers/-/helper-replace-supers-7.20.7.tgz#243ecd2724d2071532b2c8ad2f0f9f083bcae331"
  integrity sha512-vujDMtB6LVfNW13jhlCrp48QNslK6JXi7lQG736HVbHz/mbf4Dc7tIRh1Xf5C0rF7BP8iiSxGMCmY6Ci1ven3A==
  dependencies:
    "@babel/helper-environment-visitor" "^7.18.9"
    "@babel/helper-member-expression-to-functions" "^7.20.7"
    "@babel/helper-optimise-call-expression" "^7.18.6"
    "@babel/template" "^7.20.7"
    "@babel/traverse" "^7.20.7"
    "@babel/types" "^7.20.7"

"@babel/helper-simple-access@^7.20.2":
  version "7.20.2"
  resolved "https://registry.yarnpkg.com/@babel/helper-simple-access/-/helper-simple-access-7.20.2.tgz#0ab452687fe0c2cfb1e2b9e0015de07fc2d62dd9"
  integrity sha512-+0woI/WPq59IrqDYbVGfshjT5Dmk/nnbdpcF8SnMhhXObpTq2KNBdLFRFrkVdbDOyUmHBCxzm5FHV1rACIkIbA==
  dependencies:
    "@babel/types" "^7.20.2"

"@babel/helper-skip-transparent-expression-wrappers@^7.20.0":
  version "7.20.0"
  resolved "https://registry.yarnpkg.com/@babel/helper-skip-transparent-expression-wrappers/-/helper-skip-transparent-expression-wrappers-7.20.0.tgz#fbe4c52f60518cab8140d77101f0e63a8a230684"
  integrity sha512-5y1JYeNKfvnT8sZcK9DVRtpTbGiomYIHviSP3OQWmDPU3DeH4a1ZlT/N2lyQ5P8egjcRaT/Y9aNqUxK0WsnIIg==
  dependencies:
    "@babel/types" "^7.20.0"

"@babel/helper-split-export-declaration@^7.18.6":
  version "7.18.6"
  resolved "https://registry.yarnpkg.com/@babel/helper-split-export-declaration/-/helper-split-export-declaration-7.18.6.tgz#7367949bc75b20c6d5a5d4a97bba2824ae8ef075"
  integrity sha512-bde1etTx6ZyTmobl9LLMMQsaizFVZrquTEHOqKeQESMKo4PlObf+8+JA25ZsIpZhT/WEd39+vOdLXAFG/nELpA==
  dependencies:
    "@babel/types" "^7.18.6"

"@babel/helper-string-parser@^7.19.4":
  version "7.19.4"
  resolved "https://registry.yarnpkg.com/@babel/helper-string-parser/-/helper-string-parser-7.19.4.tgz#38d3acb654b4701a9b77fb0615a96f775c3a9e63"
  integrity sha512-nHtDoQcuqFmwYNYPz3Rah5ph2p8PFeFCsZk9A/48dPc/rGocJ5J3hAAZ7pb76VWX3fZKu+uEr/FhH5jLx7umrw==

"@babel/helper-validator-identifier@^7.18.6", "@babel/helper-validator-identifier@^7.19.1":
  version "7.19.1"
  resolved "https://registry.yarnpkg.com/@babel/helper-validator-identifier/-/helper-validator-identifier-7.19.1.tgz#7eea834cf32901ffdc1a7ee555e2f9c27e249ca2"
  integrity sha512-awrNfaMtnHUr653GgGEs++LlAvW6w+DcPrOliSMXWCKo597CwL5Acf/wWdNkf/tfEQE3mjkeD1YOVZOUV/od1w==

"@babel/helper-validator-option@^7.18.6":
  version "7.18.6"
  resolved "https://registry.yarnpkg.com/@babel/helper-validator-option/-/helper-validator-option-7.18.6.tgz#bf0d2b5a509b1f336099e4ff36e1a63aa5db4db8"
  integrity sha512-XO7gESt5ouv/LRJdrVjkShckw6STTaB7l9BrpBaAHDeF5YZT+01PCwmR0SJHnkW6i8OwW/EVWRShfi4j2x+KQw==

"@babel/helper-wrap-function@^7.18.9":
  version "7.20.5"
  resolved "https://registry.yarnpkg.com/@babel/helper-wrap-function/-/helper-wrap-function-7.20.5.tgz#75e2d84d499a0ab3b31c33bcfe59d6b8a45f62e3"
  integrity sha512-bYMxIWK5mh+TgXGVqAtnu5Yn1un+v8DDZtqyzKRLUzrh70Eal2O3aZ7aPYiMADO4uKlkzOiRiZ6GX5q3qxvW9Q==
  dependencies:
    "@babel/helper-function-name" "^7.19.0"
    "@babel/template" "^7.18.10"
    "@babel/traverse" "^7.20.5"
    "@babel/types" "^7.20.5"

"@babel/helpers@^7.20.7":
  version "7.20.7"
  resolved "https://registry.yarnpkg.com/@babel/helpers/-/helpers-7.20.7.tgz#04502ff0feecc9f20ecfaad120a18f011a8e6dce"
  integrity sha512-PBPjs5BppzsGaxHQCDKnZ6Gd9s6xl8bBCluz3vEInLGRJmnZan4F6BYCeqtyXqkk4W5IlPmjK4JlOuZkpJ3xZA==
  dependencies:
    "@babel/template" "^7.20.7"
    "@babel/traverse" "^7.20.7"
    "@babel/types" "^7.20.7"

"@babel/highlight@^7.18.6":
  version "7.18.6"
  resolved "https://registry.yarnpkg.com/@babel/highlight/-/highlight-7.18.6.tgz#81158601e93e2563795adcbfbdf5d64be3f2ecdf"
  integrity sha512-u7stbOuYjaPezCuLj29hNW1v64M2Md2qupEKP1fHc7WdOA3DgLh37suiSrZYY7haUB7iBeQZ9P1uiRF359do3g==
  dependencies:
    "@babel/helper-validator-identifier" "^7.18.6"
    chalk "^2.0.0"
    js-tokens "^4.0.0"

"@babel/parser@^7.20.7":
  version "7.20.7"
  resolved "https://registry.yarnpkg.com/@babel/parser/-/parser-7.20.7.tgz#66fe23b3c8569220817d5feb8b9dcdc95bb4f71b"
  integrity sha512-T3Z9oHybU+0vZlY9CiDSJQTD5ZapcW18ZctFMi0MOAl/4BjFF4ul7NVSARLdbGO5vDqy9eQiGTV0LtKfvCYvcg==

"@babel/plugin-bugfix-safari-id-destructuring-collision-in-function-expression@^7.18.6":
  version "7.18.6"
  resolved "https://registry.yarnpkg.com/@babel/plugin-bugfix-safari-id-destructuring-collision-in-function-expression/-/plugin-bugfix-safari-id-destructuring-collision-in-function-expression-7.18.6.tgz#da5b8f9a580acdfbe53494dba45ea389fb09a4d2"
  integrity sha512-Dgxsyg54Fx1d4Nge8UnvTrED63vrwOdPmyvPzlNN/boaliRP54pm3pGzZD1SJUwrBA+Cs/xdG8kXX6Mn/RfISQ==
  dependencies:
    "@babel/helper-plugin-utils" "^7.18.6"

"@babel/plugin-bugfix-v8-spread-parameters-in-optional-chaining@^7.18.9":
  version "7.20.7"
  resolved "https://registry.yarnpkg.com/@babel/plugin-bugfix-v8-spread-parameters-in-optional-chaining/-/plugin-bugfix-v8-spread-parameters-in-optional-chaining-7.20.7.tgz#d9c85589258539a22a901033853101a6198d4ef1"
  integrity sha512-sbr9+wNE5aXMBBFBICk01tt7sBf2Oc9ikRFEcem/ZORup9IMUdNhW7/wVLEbbtlWOsEubJet46mHAL2C8+2jKQ==
  dependencies:
    "@babel/helper-plugin-utils" "^7.20.2"
    "@babel/helper-skip-transparent-expression-wrappers" "^7.20.0"
    "@babel/plugin-proposal-optional-chaining" "^7.20.7"

"@babel/plugin-proposal-async-generator-functions@^7.20.1":
  version "7.20.7"
  resolved "https://registry.yarnpkg.com/@babel/plugin-proposal-async-generator-functions/-/plugin-proposal-async-generator-functions-7.20.7.tgz#bfb7276d2d573cb67ba379984a2334e262ba5326"
  integrity sha512-xMbiLsn/8RK7Wq7VeVytytS2L6qE69bXPB10YCmMdDZbKF4okCqY74pI/jJQ/8U0b/F6NrT2+14b8/P9/3AMGA==
  dependencies:
    "@babel/helper-environment-visitor" "^7.18.9"
    "@babel/helper-plugin-utils" "^7.20.2"
    "@babel/helper-remap-async-to-generator" "^7.18.9"
    "@babel/plugin-syntax-async-generators" "^7.8.4"

"@babel/plugin-proposal-class-properties@^7.18.6":
  version "7.18.6"
  resolved "https://registry.yarnpkg.com/@babel/plugin-proposal-class-properties/-/plugin-proposal-class-properties-7.18.6.tgz#b110f59741895f7ec21a6fff696ec46265c446a3"
  integrity sha512-cumfXOF0+nzZrrN8Rf0t7M+tF6sZc7vhQwYQck9q1/5w2OExlD+b4v4RpMJFaV1Z7WcDRgO6FqvxqxGlwo+RHQ==
  dependencies:
    "@babel/helper-create-class-features-plugin" "^7.18.6"
    "@babel/helper-plugin-utils" "^7.18.6"

"@babel/plugin-proposal-class-static-block@^7.18.6":
  version "7.20.7"
  resolved "https://registry.yarnpkg.com/@babel/plugin-proposal-class-static-block/-/plugin-proposal-class-static-block-7.20.7.tgz#92592e9029b13b15be0f7ce6a7aedc2879ca45a7"
  integrity sha512-AveGOoi9DAjUYYuUAG//Ig69GlazLnoyzMw68VCDux+c1tsnnH/OkYcpz/5xzMkEFC6UxjR5Gw1c+iY2wOGVeQ==
  dependencies:
    "@babel/helper-create-class-features-plugin" "^7.20.7"
    "@babel/helper-plugin-utils" "^7.20.2"
    "@babel/plugin-syntax-class-static-block" "^7.14.5"

"@babel/plugin-proposal-dynamic-import@^7.18.6":
  version "7.18.6"
  resolved "https://registry.yarnpkg.com/@babel/plugin-proposal-dynamic-import/-/plugin-proposal-dynamic-import-7.18.6.tgz#72bcf8d408799f547d759298c3c27c7e7faa4d94"
  integrity sha512-1auuwmK+Rz13SJj36R+jqFPMJWyKEDd7lLSdOj4oJK0UTgGueSAtkrCvz9ewmgyU/P941Rv2fQwZJN8s6QruXw==
  dependencies:
    "@babel/helper-plugin-utils" "^7.18.6"
    "@babel/plugin-syntax-dynamic-import" "^7.8.3"

"@babel/plugin-proposal-export-namespace-from@^7.18.9":
  version "7.18.9"
  resolved "https://registry.yarnpkg.com/@babel/plugin-proposal-export-namespace-from/-/plugin-proposal-export-namespace-from-7.18.9.tgz#5f7313ab348cdb19d590145f9247540e94761203"
  integrity sha512-k1NtHyOMvlDDFeb9G5PhUXuGj8m/wiwojgQVEhJ/fsVsMCpLyOP4h0uGEjYJKrRI+EVPlb5Jk+Gt9P97lOGwtA==
  dependencies:
    "@babel/helper-plugin-utils" "^7.18.9"
    "@babel/plugin-syntax-export-namespace-from" "^7.8.3"

"@babel/plugin-proposal-json-strings@^7.18.6":
  version "7.18.6"
  resolved "https://registry.yarnpkg.com/@babel/plugin-proposal-json-strings/-/plugin-proposal-json-strings-7.18.6.tgz#7e8788c1811c393aff762817e7dbf1ebd0c05f0b"
  integrity sha512-lr1peyn9kOdbYc0xr0OdHTZ5FMqS6Di+H0Fz2I/JwMzGmzJETNeOFq2pBySw6X/KFL5EWDjlJuMsUGRFb8fQgQ==
  dependencies:
    "@babel/helper-plugin-utils" "^7.18.6"
    "@babel/plugin-syntax-json-strings" "^7.8.3"

"@babel/plugin-proposal-logical-assignment-operators@^7.18.9":
  version "7.20.7"
  resolved "https://registry.yarnpkg.com/@babel/plugin-proposal-logical-assignment-operators/-/plugin-proposal-logical-assignment-operators-7.20.7.tgz#dfbcaa8f7b4d37b51e8bfb46d94a5aea2bb89d83"
  integrity sha512-y7C7cZgpMIjWlKE5T7eJwp+tnRYM89HmRvWM5EQuB5BoHEONjmQ8lSNmBUwOyy/GFRsohJED51YBF79hE1djug==
  dependencies:
    "@babel/helper-plugin-utils" "^7.20.2"
    "@babel/plugin-syntax-logical-assignment-operators" "^7.10.4"

"@babel/plugin-proposal-nullish-coalescing-operator@^7.18.6":
  version "7.18.6"
  resolved "https://registry.yarnpkg.com/@babel/plugin-proposal-nullish-coalescing-operator/-/plugin-proposal-nullish-coalescing-operator-7.18.6.tgz#fdd940a99a740e577d6c753ab6fbb43fdb9467e1"
  integrity sha512-wQxQzxYeJqHcfppzBDnm1yAY0jSRkUXR2z8RePZYrKwMKgMlE8+Z6LUno+bd6LvbGh8Gltvy74+9pIYkr+XkKA==
  dependencies:
    "@babel/helper-plugin-utils" "^7.18.6"
    "@babel/plugin-syntax-nullish-coalescing-operator" "^7.8.3"

"@babel/plugin-proposal-numeric-separator@^7.18.6":
  version "7.18.6"
  resolved "https://registry.yarnpkg.com/@babel/plugin-proposal-numeric-separator/-/plugin-proposal-numeric-separator-7.18.6.tgz#899b14fbafe87f053d2c5ff05b36029c62e13c75"
  integrity sha512-ozlZFogPqoLm8WBr5Z8UckIoE4YQ5KESVcNudyXOR8uqIkliTEgJ3RoketfG6pmzLdeZF0H/wjE9/cCEitBl7Q==
  dependencies:
    "@babel/helper-plugin-utils" "^7.18.6"
    "@babel/plugin-syntax-numeric-separator" "^7.10.4"

"@babel/plugin-proposal-object-rest-spread@^7.20.2":
  version "7.20.7"
  resolved "https://registry.yarnpkg.com/@babel/plugin-proposal-object-rest-spread/-/plugin-proposal-object-rest-spread-7.20.7.tgz#aa662940ef425779c75534a5c41e9d936edc390a"
  integrity sha512-d2S98yCiLxDVmBmE8UjGcfPvNEUbA1U5q5WxaWFUGRzJSVAZqm5W6MbPct0jxnegUZ0niLeNX+IOzEs7wYg9Dg==
  dependencies:
    "@babel/compat-data" "^7.20.5"
    "@babel/helper-compilation-targets" "^7.20.7"
    "@babel/helper-plugin-utils" "^7.20.2"
    "@babel/plugin-syntax-object-rest-spread" "^7.8.3"
    "@babel/plugin-transform-parameters" "^7.20.7"

"@babel/plugin-proposal-optional-catch-binding@^7.18.6":
  version "7.18.6"
  resolved "https://registry.yarnpkg.com/@babel/plugin-proposal-optional-catch-binding/-/plugin-proposal-optional-catch-binding-7.18.6.tgz#f9400d0e6a3ea93ba9ef70b09e72dd6da638a2cb"
  integrity sha512-Q40HEhs9DJQyaZfUjjn6vE8Cv4GmMHCYuMGIWUnlxH6400VGxOuwWsPt4FxXxJkC/5eOzgn0z21M9gMT4MOhbw==
  dependencies:
    "@babel/helper-plugin-utils" "^7.18.6"
    "@babel/plugin-syntax-optional-catch-binding" "^7.8.3"

"@babel/plugin-proposal-optional-chaining@^7.18.9", "@babel/plugin-proposal-optional-chaining@^7.20.7":
  version "7.20.7"
  resolved "https://registry.yarnpkg.com/@babel/plugin-proposal-optional-chaining/-/plugin-proposal-optional-chaining-7.20.7.tgz#49f2b372519ab31728cc14115bb0998b15bfda55"
  integrity sha512-T+A7b1kfjtRM51ssoOfS1+wbyCVqorfyZhT99TvxxLMirPShD8CzKMRepMlCBGM5RpHMbn8s+5MMHnPstJH6mQ==
  dependencies:
    "@babel/helper-plugin-utils" "^7.20.2"
    "@babel/helper-skip-transparent-expression-wrappers" "^7.20.0"
    "@babel/plugin-syntax-optional-chaining" "^7.8.3"

"@babel/plugin-proposal-private-methods@^7.18.6":
  version "7.18.6"
  resolved "https://registry.yarnpkg.com/@babel/plugin-proposal-private-methods/-/plugin-proposal-private-methods-7.18.6.tgz#5209de7d213457548a98436fa2882f52f4be6bea"
  integrity sha512-nutsvktDItsNn4rpGItSNV2sz1XwS+nfU0Rg8aCx3W3NOKVzdMjJRu0O5OkgDp3ZGICSTbgRpxZoWsxoKRvbeA==
  dependencies:
    "@babel/helper-create-class-features-plugin" "^7.18.6"
    "@babel/helper-plugin-utils" "^7.18.6"

"@babel/plugin-proposal-private-property-in-object@^7.18.6":
  version "7.20.5"
  resolved "https://registry.yarnpkg.com/@babel/plugin-proposal-private-property-in-object/-/plugin-proposal-private-property-in-object-7.20.5.tgz#309c7668f2263f1c711aa399b5a9a6291eef6135"
  integrity sha512-Vq7b9dUA12ByzB4EjQTPo25sFhY+08pQDBSZRtUAkj7lb7jahaHR5igera16QZ+3my1nYR4dKsNdYj5IjPHilQ==
  dependencies:
    "@babel/helper-annotate-as-pure" "^7.18.6"
    "@babel/helper-create-class-features-plugin" "^7.20.5"
    "@babel/helper-plugin-utils" "^7.20.2"
    "@babel/plugin-syntax-private-property-in-object" "^7.14.5"

"@babel/plugin-proposal-unicode-property-regex@^7.18.6", "@babel/plugin-proposal-unicode-property-regex@^7.4.4":
  version "7.18.6"
  resolved "https://registry.yarnpkg.com/@babel/plugin-proposal-unicode-property-regex/-/plugin-proposal-unicode-property-regex-7.18.6.tgz#af613d2cd5e643643b65cded64207b15c85cb78e"
  integrity sha512-2BShG/d5yoZyXZfVePH91urL5wTG6ASZU9M4o03lKK8u8UW1y08OMttBSOADTcJrnPMpvDXRG3G8fyLh4ovs8w==
  dependencies:
    "@babel/helper-create-regexp-features-plugin" "^7.18.6"
    "@babel/helper-plugin-utils" "^7.18.6"

"@babel/plugin-syntax-async-generators@^7.8.4":
  version "7.8.4"
  resolved "https://registry.yarnpkg.com/@babel/plugin-syntax-async-generators/-/plugin-syntax-async-generators-7.8.4.tgz#a983fb1aeb2ec3f6ed042a210f640e90e786fe0d"
  integrity sha512-tycmZxkGfZaxhMRbXlPXuVFpdWlXpir2W4AMhSJgRKzk/eDlIXOhb2LHWoLpDF7TEHylV5zNhykX6KAgHJmTNw==
  dependencies:
    "@babel/helper-plugin-utils" "^7.8.0"

"@babel/plugin-syntax-class-properties@^7.12.13":
  version "7.12.13"
  resolved "https://registry.yarnpkg.com/@babel/plugin-syntax-class-properties/-/plugin-syntax-class-properties-7.12.13.tgz#b5c987274c4a3a82b89714796931a6b53544ae10"
  integrity sha512-fm4idjKla0YahUNgFNLCB0qySdsoPiZP3iQE3rky0mBUtMZ23yDJ9SJdg6dXTSDnulOVqiF3Hgr9nbXvXTQZYA==
  dependencies:
    "@babel/helper-plugin-utils" "^7.12.13"

"@babel/plugin-syntax-class-static-block@^7.14.5":
  version "7.14.5"
  resolved "https://registry.yarnpkg.com/@babel/plugin-syntax-class-static-block/-/plugin-syntax-class-static-block-7.14.5.tgz#195df89b146b4b78b3bf897fd7a257c84659d406"
  integrity sha512-b+YyPmr6ldyNnM6sqYeMWE+bgJcJpO6yS4QD7ymxgH34GBPNDM/THBh8iunyvKIZztiwLH4CJZ0RxTk9emgpjw==
  dependencies:
    "@babel/helper-plugin-utils" "^7.14.5"

"@babel/plugin-syntax-dynamic-import@^7.8.3":
  version "7.8.3"
  resolved "https://registry.yarnpkg.com/@babel/plugin-syntax-dynamic-import/-/plugin-syntax-dynamic-import-7.8.3.tgz#62bf98b2da3cd21d626154fc96ee5b3cb68eacb3"
  integrity sha512-5gdGbFon+PszYzqs83S3E5mpi7/y/8M9eC90MRTZfduQOYW76ig6SOSPNe41IG5LoP3FGBn2N0RjVDSQiS94kQ==
  dependencies:
    "@babel/helper-plugin-utils" "^7.8.0"

"@babel/plugin-syntax-export-namespace-from@^7.8.3":
  version "7.8.3"
  resolved "https://registry.yarnpkg.com/@babel/plugin-syntax-export-namespace-from/-/plugin-syntax-export-namespace-from-7.8.3.tgz#028964a9ba80dbc094c915c487ad7c4e7a66465a"
  integrity sha512-MXf5laXo6c1IbEbegDmzGPwGNTsHZmEy6QGznu5Sh2UCWvueywb2ee+CCE4zQiZstxU9BMoQO9i6zUFSY0Kj0Q==
  dependencies:
    "@babel/helper-plugin-utils" "^7.8.3"

"@babel/plugin-syntax-import-assertions@^7.20.0":
  version "7.20.0"
  resolved "https://registry.yarnpkg.com/@babel/plugin-syntax-import-assertions/-/plugin-syntax-import-assertions-7.20.0.tgz#bb50e0d4bea0957235390641209394e87bdb9cc4"
  integrity sha512-IUh1vakzNoWalR8ch/areW7qFopR2AEw03JlG7BbrDqmQ4X3q9uuipQwSGrUn7oGiemKjtSLDhNtQHzMHr1JdQ==
  dependencies:
    "@babel/helper-plugin-utils" "^7.19.0"

"@babel/plugin-syntax-json-strings@^7.8.3":
  version "7.8.3"
  resolved "https://registry.yarnpkg.com/@babel/plugin-syntax-json-strings/-/plugin-syntax-json-strings-7.8.3.tgz#01ca21b668cd8218c9e640cb6dd88c5412b2c96a"
  integrity sha512-lY6kdGpWHvjoe2vk4WrAapEuBR69EMxZl+RoGRhrFGNYVK8mOPAW8VfbT/ZgrFbXlDNiiaxQnAtgVCZ6jv30EA==
  dependencies:
    "@babel/helper-plugin-utils" "^7.8.0"

"@babel/plugin-syntax-jsx@^7.18.6":
  version "7.18.6"
  resolved "https://registry.yarnpkg.com/@babel/plugin-syntax-jsx/-/plugin-syntax-jsx-7.18.6.tgz#a8feef63b010150abd97f1649ec296e849943ca0"
  integrity sha512-6mmljtAedFGTWu2p/8WIORGwy+61PLgOMPOdazc7YoJ9ZCWUyFy3A6CpPkRKLKD1ToAesxX8KGEViAiLo9N+7Q==
  dependencies:
    "@babel/helper-plugin-utils" "^7.18.6"

"@babel/plugin-syntax-logical-assignment-operators@^7.10.4":
  version "7.10.4"
  resolved "https://registry.yarnpkg.com/@babel/plugin-syntax-logical-assignment-operators/-/plugin-syntax-logical-assignment-operators-7.10.4.tgz#ca91ef46303530448b906652bac2e9fe9941f699"
  integrity sha512-d8waShlpFDinQ5MtvGU9xDAOzKH47+FFoney2baFIoMr952hKOLp1HR7VszoZvOsV/4+RRszNY7D17ba0te0ig==
  dependencies:
    "@babel/helper-plugin-utils" "^7.10.4"

"@babel/plugin-syntax-nullish-coalescing-operator@^7.8.3":
  version "7.8.3"
  resolved "https://registry.yarnpkg.com/@babel/plugin-syntax-nullish-coalescing-operator/-/plugin-syntax-nullish-coalescing-operator-7.8.3.tgz#167ed70368886081f74b5c36c65a88c03b66d1a9"
  integrity sha512-aSff4zPII1u2QD7y+F8oDsz19ew4IGEJg9SVW+bqwpwtfFleiQDMdzA/R+UlWDzfnHFCxxleFT0PMIrR36XLNQ==
  dependencies:
    "@babel/helper-plugin-utils" "^7.8.0"

"@babel/plugin-syntax-numeric-separator@^7.10.4":
  version "7.10.4"
  resolved "https://registry.yarnpkg.com/@babel/plugin-syntax-numeric-separator/-/plugin-syntax-numeric-separator-7.10.4.tgz#b9b070b3e33570cd9fd07ba7fa91c0dd37b9af97"
  integrity sha512-9H6YdfkcK/uOnY/K7/aA2xpzaAgkQn37yzWUMRK7OaPOqOpGS1+n0H5hxT9AUw9EsSjPW8SVyMJwYRtWs3X3ug==
  dependencies:
    "@babel/helper-plugin-utils" "^7.10.4"

"@babel/plugin-syntax-object-rest-spread@^7.8.3":
  version "7.8.3"
  resolved "https://registry.yarnpkg.com/@babel/plugin-syntax-object-rest-spread/-/plugin-syntax-object-rest-spread-7.8.3.tgz#60e225edcbd98a640332a2e72dd3e66f1af55871"
  integrity sha512-XoqMijGZb9y3y2XskN+P1wUGiVwWZ5JmoDRwx5+3GmEplNyVM2s2Dg8ILFQm8rWM48orGy5YpI5Bl8U1y7ydlA==
  dependencies:
    "@babel/helper-plugin-utils" "^7.8.0"

"@babel/plugin-syntax-optional-catch-binding@^7.8.3":
  version "7.8.3"
  resolved "https://registry.yarnpkg.com/@babel/plugin-syntax-optional-catch-binding/-/plugin-syntax-optional-catch-binding-7.8.3.tgz#6111a265bcfb020eb9efd0fdfd7d26402b9ed6c1"
  integrity sha512-6VPD0Pc1lpTqw0aKoeRTMiB+kWhAoT24PA+ksWSBrFtl5SIRVpZlwN3NNPQjehA2E/91FV3RjLWoVTglWcSV3Q==
  dependencies:
    "@babel/helper-plugin-utils" "^7.8.0"

"@babel/plugin-syntax-optional-chaining@^7.8.3":
  version "7.8.3"
  resolved "https://registry.yarnpkg.com/@babel/plugin-syntax-optional-chaining/-/plugin-syntax-optional-chaining-7.8.3.tgz#4f69c2ab95167e0180cd5336613f8c5788f7d48a"
  integrity sha512-KoK9ErH1MBlCPxV0VANkXW2/dw4vlbGDrFgz8bmUsBGYkFRcbRwMh6cIJubdPrkxRwuGdtCk0v/wPTKbQgBjkg==
  dependencies:
    "@babel/helper-plugin-utils" "^7.8.0"

"@babel/plugin-syntax-private-property-in-object@^7.14.5":
  version "7.14.5"
  resolved "https://registry.yarnpkg.com/@babel/plugin-syntax-private-property-in-object/-/plugin-syntax-private-property-in-object-7.14.5.tgz#0dc6671ec0ea22b6e94a1114f857970cd39de1ad"
  integrity sha512-0wVnp9dxJ72ZUJDV27ZfbSj6iHLoytYZmh3rFcxNnvsJF3ktkzLDZPy/mA17HGsaQT3/DQsWYX1f1QGWkCoVUg==
  dependencies:
    "@babel/helper-plugin-utils" "^7.14.5"

"@babel/plugin-syntax-top-level-await@^7.14.5":
  version "7.14.5"
  resolved "https://registry.yarnpkg.com/@babel/plugin-syntax-top-level-await/-/plugin-syntax-top-level-await-7.14.5.tgz#c1cfdadc35a646240001f06138247b741c34d94c"
  integrity sha512-hx++upLv5U1rgYfwe1xBQUhRmU41NEvpUvrp8jkrSCdvGSnM5/qdRMtylJ6PG5OFkBaHkbTAKTnd3/YyESRHFw==
  dependencies:
    "@babel/helper-plugin-utils" "^7.14.5"

"@babel/plugin-syntax-typescript@^7.20.0":
  version "7.20.0"
  resolved "https://registry.yarnpkg.com/@babel/plugin-syntax-typescript/-/plugin-syntax-typescript-7.20.0.tgz#4e9a0cfc769c85689b77a2e642d24e9f697fc8c7"
  integrity sha512-rd9TkG+u1CExzS4SM1BlMEhMXwFLKVjOAFFCDx9PbX5ycJWDoWMcwdJH9RhkPu1dOgn5TrxLot/Gx6lWFuAUNQ==
  dependencies:
    "@babel/helper-plugin-utils" "^7.19.0"

"@babel/plugin-transform-arrow-functions@^7.18.6":
  version "7.20.7"
  resolved "https://registry.yarnpkg.com/@babel/plugin-transform-arrow-functions/-/plugin-transform-arrow-functions-7.20.7.tgz#bea332b0e8b2dab3dafe55a163d8227531ab0551"
  integrity sha512-3poA5E7dzDomxj9WXWwuD6A5F3kc7VXwIJO+E+J8qtDtS+pXPAhrgEyh+9GBwBgPq1Z+bB+/JD60lp5jsN7JPQ==
  dependencies:
    "@babel/helper-plugin-utils" "^7.20.2"

"@babel/plugin-transform-async-to-generator@^7.18.6":
  version "7.20.7"
  resolved "https://registry.yarnpkg.com/@babel/plugin-transform-async-to-generator/-/plugin-transform-async-to-generator-7.20.7.tgz#dfee18623c8cb31deb796aa3ca84dda9cea94354"
  integrity sha512-Uo5gwHPT9vgnSXQxqGtpdufUiWp96gk7yiP4Mp5bm1QMkEmLXBO7PAGYbKoJ6DhAwiNkcHFBol/x5zZZkL/t0Q==
  dependencies:
    "@babel/helper-module-imports" "^7.18.6"
    "@babel/helper-plugin-utils" "^7.20.2"
    "@babel/helper-remap-async-to-generator" "^7.18.9"

"@babel/plugin-transform-block-scoped-functions@^7.18.6":
  version "7.18.6"
  resolved "https://registry.yarnpkg.com/@babel/plugin-transform-block-scoped-functions/-/plugin-transform-block-scoped-functions-7.18.6.tgz#9187bf4ba302635b9d70d986ad70f038726216a8"
  integrity sha512-ExUcOqpPWnliRcPqves5HJcJOvHvIIWfuS4sroBUenPuMdmW+SMHDakmtS7qOo13sVppmUijqeTv7qqGsvURpQ==
  dependencies:
    "@babel/helper-plugin-utils" "^7.18.6"

"@babel/plugin-transform-block-scoping@^7.20.2":
  version "7.20.11"
  resolved "https://registry.yarnpkg.com/@babel/plugin-transform-block-scoping/-/plugin-transform-block-scoping-7.20.11.tgz#9f5a3424bd112a3f32fe0cf9364fbb155cff262a"
  integrity sha512-tA4N427a7fjf1P0/2I4ScsHGc5jcHPbb30xMbaTke2gxDuWpUfXDuX1FEymJwKk4tuGUvGcejAR6HdZVqmmPyw==
  dependencies:
    "@babel/helper-plugin-utils" "^7.20.2"

"@babel/plugin-transform-classes@^7.20.2":
  version "7.20.7"
  resolved "https://registry.yarnpkg.com/@babel/plugin-transform-classes/-/plugin-transform-classes-7.20.7.tgz#f438216f094f6bb31dc266ebfab8ff05aecad073"
  integrity sha512-LWYbsiXTPKl+oBlXUGlwNlJZetXD5Am+CyBdqhPsDVjM9Jc8jwBJFrKhHf900Kfk2eZG1y9MAG3UNajol7A4VQ==
  dependencies:
    "@babel/helper-annotate-as-pure" "^7.18.6"
    "@babel/helper-compilation-targets" "^7.20.7"
    "@babel/helper-environment-visitor" "^7.18.9"
    "@babel/helper-function-name" "^7.19.0"
    "@babel/helper-optimise-call-expression" "^7.18.6"
    "@babel/helper-plugin-utils" "^7.20.2"
    "@babel/helper-replace-supers" "^7.20.7"
    "@babel/helper-split-export-declaration" "^7.18.6"
    globals "^11.1.0"

"@babel/plugin-transform-computed-properties@^7.18.9":
  version "7.20.7"
  resolved "https://registry.yarnpkg.com/@babel/plugin-transform-computed-properties/-/plugin-transform-computed-properties-7.20.7.tgz#704cc2fd155d1c996551db8276d55b9d46e4d0aa"
  integrity sha512-Lz7MvBK6DTjElHAmfu6bfANzKcxpyNPeYBGEafyA6E5HtRpjpZwU+u7Qrgz/2OR0z+5TvKYbPdphfSaAcZBrYQ==
  dependencies:
    "@babel/helper-plugin-utils" "^7.20.2"
    "@babel/template" "^7.20.7"

"@babel/plugin-transform-destructuring@^7.20.2":
  version "7.20.7"
  resolved "https://registry.yarnpkg.com/@babel/plugin-transform-destructuring/-/plugin-transform-destructuring-7.20.7.tgz#8bda578f71620c7de7c93af590154ba331415454"
  integrity sha512-Xwg403sRrZb81IVB79ZPqNQME23yhugYVqgTxAhT99h485F4f+GMELFhhOsscDUB7HCswepKeCKLn/GZvUKoBA==
  dependencies:
    "@babel/helper-plugin-utils" "^7.20.2"

"@babel/plugin-transform-dotall-regex@^7.18.6", "@babel/plugin-transform-dotall-regex@^7.4.4":
  version "7.18.6"
  resolved "https://registry.yarnpkg.com/@babel/plugin-transform-dotall-regex/-/plugin-transform-dotall-regex-7.18.6.tgz#b286b3e7aae6c7b861e45bed0a2fafd6b1a4fef8"
  integrity sha512-6S3jpun1eEbAxq7TdjLotAsl4WpQI9DxfkycRcKrjhQYzU87qpXdknpBg/e+TdcMehqGnLFi7tnFUBR02Vq6wg==
  dependencies:
    "@babel/helper-create-regexp-features-plugin" "^7.18.6"
    "@babel/helper-plugin-utils" "^7.18.6"

"@babel/plugin-transform-duplicate-keys@^7.18.9":
  version "7.18.9"
  resolved "https://registry.yarnpkg.com/@babel/plugin-transform-duplicate-keys/-/plugin-transform-duplicate-keys-7.18.9.tgz#687f15ee3cdad6d85191eb2a372c4528eaa0ae0e"
  integrity sha512-d2bmXCtZXYc59/0SanQKbiWINadaJXqtvIQIzd4+hNwkWBgyCd5F/2t1kXoUdvPMrxzPvhK6EMQRROxsue+mfw==
  dependencies:
    "@babel/helper-plugin-utils" "^7.18.9"

"@babel/plugin-transform-exponentiation-operator@^7.18.6":
  version "7.18.6"
  resolved "https://registry.yarnpkg.com/@babel/plugin-transform-exponentiation-operator/-/plugin-transform-exponentiation-operator-7.18.6.tgz#421c705f4521888c65e91fdd1af951bfefd4dacd"
  integrity sha512-wzEtc0+2c88FVR34aQmiz56dxEkxr2g8DQb/KfaFa1JYXOFVsbhvAonFN6PwVWj++fKmku8NP80plJ5Et4wqHw==
  dependencies:
    "@babel/helper-builder-binary-assignment-operator-visitor" "^7.18.6"
    "@babel/helper-plugin-utils" "^7.18.6"

"@babel/plugin-transform-for-of@^7.18.8":
  version "7.18.8"
  resolved "https://registry.yarnpkg.com/@babel/plugin-transform-for-of/-/plugin-transform-for-of-7.18.8.tgz#6ef8a50b244eb6a0bdbad0c7c61877e4e30097c1"
  integrity sha512-yEfTRnjuskWYo0k1mHUqrVWaZwrdq8AYbfrpqULOJOaucGSp4mNMVps+YtA8byoevxS/urwU75vyhQIxcCgiBQ==
  dependencies:
    "@babel/helper-plugin-utils" "^7.18.6"

"@babel/plugin-transform-function-name@^7.18.9":
  version "7.18.9"
  resolved "https://registry.yarnpkg.com/@babel/plugin-transform-function-name/-/plugin-transform-function-name-7.18.9.tgz#cc354f8234e62968946c61a46d6365440fc764e0"
  integrity sha512-WvIBoRPaJQ5yVHzcnJFor7oS5Ls0PYixlTYE63lCj2RtdQEl15M68FXQlxnG6wdraJIXRdR7KI+hQ7q/9QjrCQ==
  dependencies:
    "@babel/helper-compilation-targets" "^7.18.9"
    "@babel/helper-function-name" "^7.18.9"
    "@babel/helper-plugin-utils" "^7.18.9"

"@babel/plugin-transform-literals@^7.18.9":
  version "7.18.9"
  resolved "https://registry.yarnpkg.com/@babel/plugin-transform-literals/-/plugin-transform-literals-7.18.9.tgz#72796fdbef80e56fba3c6a699d54f0de557444bc"
  integrity sha512-IFQDSRoTPnrAIrI5zoZv73IFeZu2dhu6irxQjY9rNjTT53VmKg9fenjvoiOWOkJ6mm4jKVPtdMzBY98Fp4Z4cg==
  dependencies:
    "@babel/helper-plugin-utils" "^7.18.9"

"@babel/plugin-transform-member-expression-literals@^7.18.6":
  version "7.18.6"
  resolved "https://registry.yarnpkg.com/@babel/plugin-transform-member-expression-literals/-/plugin-transform-member-expression-literals-7.18.6.tgz#ac9fdc1a118620ac49b7e7a5d2dc177a1bfee88e"
  integrity sha512-qSF1ihLGO3q+/g48k85tUjD033C29TNTVB2paCwZPVmOsjn9pClvYYrM2VeJpBY2bcNkuny0YUyTNRyRxJ54KA==
  dependencies:
    "@babel/helper-plugin-utils" "^7.18.6"

"@babel/plugin-transform-modules-amd@^7.19.6":
  version "7.20.11"
  resolved "https://registry.yarnpkg.com/@babel/plugin-transform-modules-amd/-/plugin-transform-modules-amd-7.20.11.tgz#3daccca8e4cc309f03c3a0c4b41dc4b26f55214a"
  integrity sha512-NuzCt5IIYOW0O30UvqktzHYR2ud5bOWbY0yaxWZ6G+aFzOMJvrs5YHNikrbdaT15+KNO31nPOy5Fim3ku6Zb5g==
  dependencies:
    "@babel/helper-module-transforms" "^7.20.11"
    "@babel/helper-plugin-utils" "^7.20.2"

"@babel/plugin-transform-modules-commonjs@^7.19.6":
  version "7.20.11"
  resolved "https://registry.yarnpkg.com/@babel/plugin-transform-modules-commonjs/-/plugin-transform-modules-commonjs-7.20.11.tgz#8cb23010869bf7669fd4b3098598b6b2be6dc607"
  integrity sha512-S8e1f7WQ7cimJQ51JkAaDrEtohVEitXjgCGAS2N8S31Y42E+kWwfSz83LYz57QdBm7q9diARVqanIaH2oVgQnw==
  dependencies:
    "@babel/helper-module-transforms" "^7.20.11"
    "@babel/helper-plugin-utils" "^7.20.2"
    "@babel/helper-simple-access" "^7.20.2"

"@babel/plugin-transform-modules-systemjs@^7.19.6":
  version "7.20.11"
  resolved "https://registry.yarnpkg.com/@babel/plugin-transform-modules-systemjs/-/plugin-transform-modules-systemjs-7.20.11.tgz#467ec6bba6b6a50634eea61c9c232654d8a4696e"
  integrity sha512-vVu5g9BPQKSFEmvt2TA4Da5N+QVS66EX21d8uoOihC+OCpUoGvzVsXeqFdtAEfVa5BILAeFt+U7yVmLbQnAJmw==
  dependencies:
    "@babel/helper-hoist-variables" "^7.18.6"
    "@babel/helper-module-transforms" "^7.20.11"
    "@babel/helper-plugin-utils" "^7.20.2"
    "@babel/helper-validator-identifier" "^7.19.1"

"@babel/plugin-transform-modules-umd@^7.18.6":
  version "7.18.6"
  resolved "https://registry.yarnpkg.com/@babel/plugin-transform-modules-umd/-/plugin-transform-modules-umd-7.18.6.tgz#81d3832d6034b75b54e62821ba58f28ed0aab4b9"
  integrity sha512-dcegErExVeXcRqNtkRU/z8WlBLnvD4MRnHgNs3MytRO1Mn1sHRyhbcpYbVMGclAqOjdW+9cfkdZno9dFdfKLfQ==
  dependencies:
    "@babel/helper-module-transforms" "^7.18.6"
    "@babel/helper-plugin-utils" "^7.18.6"

"@babel/plugin-transform-named-capturing-groups-regex@^7.19.1":
  version "7.20.5"
  resolved "https://registry.yarnpkg.com/@babel/plugin-transform-named-capturing-groups-regex/-/plugin-transform-named-capturing-groups-regex-7.20.5.tgz#626298dd62ea51d452c3be58b285d23195ba69a8"
  integrity sha512-mOW4tTzi5iTLnw+78iEq3gr8Aoq4WNRGpmSlrogqaiCBoR1HFhpU4JkpQFOHfeYx3ReVIFWOQJS4aZBRvuZ6mA==
  dependencies:
    "@babel/helper-create-regexp-features-plugin" "^7.20.5"
    "@babel/helper-plugin-utils" "^7.20.2"

"@babel/plugin-transform-new-target@^7.18.6":
  version "7.18.6"
  resolved "https://registry.yarnpkg.com/@babel/plugin-transform-new-target/-/plugin-transform-new-target-7.18.6.tgz#d128f376ae200477f37c4ddfcc722a8a1b3246a8"
  integrity sha512-DjwFA/9Iu3Z+vrAn+8pBUGcjhxKguSMlsFqeCKbhb9BAV756v0krzVK04CRDi/4aqmk8BsHb4a/gFcaA5joXRw==
  dependencies:
    "@babel/helper-plugin-utils" "^7.18.6"

"@babel/plugin-transform-object-super@^7.18.6":
  version "7.18.6"
  resolved "https://registry.yarnpkg.com/@babel/plugin-transform-object-super/-/plugin-transform-object-super-7.18.6.tgz#fb3c6ccdd15939b6ff7939944b51971ddc35912c"
  integrity sha512-uvGz6zk+pZoS1aTZrOvrbj6Pp/kK2mp45t2B+bTDre2UgsZZ8EZLSJtUg7m/no0zOJUWgFONpB7Zv9W2tSaFlA==
  dependencies:
    "@babel/helper-plugin-utils" "^7.18.6"
    "@babel/helper-replace-supers" "^7.18.6"

"@babel/plugin-transform-parameters@^7.20.1", "@babel/plugin-transform-parameters@^7.20.7":
  version "7.20.7"
  resolved "https://registry.yarnpkg.com/@babel/plugin-transform-parameters/-/plugin-transform-parameters-7.20.7.tgz#0ee349e9d1bc96e78e3b37a7af423a4078a7083f"
  integrity sha512-WiWBIkeHKVOSYPO0pWkxGPfKeWrCJyD3NJ53+Lrp/QMSZbsVPovrVl2aWZ19D/LTVnaDv5Ap7GJ/B2CTOZdrfA==
  dependencies:
    "@babel/helper-plugin-utils" "^7.20.2"

"@babel/plugin-transform-property-literals@^7.18.6":
  version "7.18.6"
  resolved "https://registry.yarnpkg.com/@babel/plugin-transform-property-literals/-/plugin-transform-property-literals-7.18.6.tgz#e22498903a483448e94e032e9bbb9c5ccbfc93a3"
  integrity sha512-cYcs6qlgafTud3PAzrrRNbQtfpQ8+y/+M5tKmksS9+M1ckbH6kzY8MrexEM9mcA6JDsukE19iIRvAyYl463sMg==
  dependencies:
    "@babel/helper-plugin-utils" "^7.18.6"

"@babel/plugin-transform-react-constant-elements@^7.18.12":
  version "7.20.2"
  resolved "https://registry.yarnpkg.com/@babel/plugin-transform-react-constant-elements/-/plugin-transform-react-constant-elements-7.20.2.tgz#3f02c784e0b711970d7d8ccc96c4359d64e27ac7"
  integrity sha512-KS/G8YI8uwMGKErLFOHS/ekhqdHhpEloxs43NecQHVgo2QuQSyJhGIY1fL8UGl9wy5ItVwwoUL4YxVqsplGq2g==
  dependencies:
    "@babel/helper-plugin-utils" "^7.20.2"

"@babel/plugin-transform-react-display-name@^7.18.6":
  version "7.18.6"
  resolved "https://registry.yarnpkg.com/@babel/plugin-transform-react-display-name/-/plugin-transform-react-display-name-7.18.6.tgz#8b1125f919ef36ebdfff061d664e266c666b9415"
  integrity sha512-TV4sQ+T013n61uMoygyMRm+xf04Bd5oqFpv2jAEQwSZ8NwQA7zeRPg1LMVg2PWi3zWBz+CLKD+v5bcpZ/BS0aA==
  dependencies:
    "@babel/helper-plugin-utils" "^7.18.6"

"@babel/plugin-transform-react-jsx-development@^7.18.6":
  version "7.18.6"
  resolved "https://registry.yarnpkg.com/@babel/plugin-transform-react-jsx-development/-/plugin-transform-react-jsx-development-7.18.6.tgz#dbe5c972811e49c7405b630e4d0d2e1380c0ddc5"
  integrity sha512-SA6HEjwYFKF7WDjWcMcMGUimmw/nhNRDWxr+KaLSCrkD/LMDBvWRmHAYgE1HDeF8KUuI8OAu+RT6EOtKxSW2qA==
  dependencies:
    "@babel/plugin-transform-react-jsx" "^7.18.6"

"@babel/plugin-transform-react-jsx@^7.18.6":
  version "7.20.7"
  resolved "https://registry.yarnpkg.com/@babel/plugin-transform-react-jsx/-/plugin-transform-react-jsx-7.20.7.tgz#025d85a1935fd7e19dfdcb1b1d4df34d4da484f7"
  integrity sha512-Tfq7qqD+tRj3EoDhY00nn2uP2hsRxgYGi5mLQ5TimKav0a9Lrpd4deE+fcLXU8zFYRjlKPHZhpCvfEA6qnBxqQ==
  dependencies:
    "@babel/helper-annotate-as-pure" "^7.18.6"
    "@babel/helper-module-imports" "^7.18.6"
    "@babel/helper-plugin-utils" "^7.20.2"
    "@babel/plugin-syntax-jsx" "^7.18.6"
    "@babel/types" "^7.20.7"

"@babel/plugin-transform-react-pure-annotations@^7.18.6":
  version "7.18.6"
  resolved "https://registry.yarnpkg.com/@babel/plugin-transform-react-pure-annotations/-/plugin-transform-react-pure-annotations-7.18.6.tgz#561af267f19f3e5d59291f9950fd7b9663d0d844"
  integrity sha512-I8VfEPg9r2TRDdvnHgPepTKvuRomzA8+u+nhY7qSI1fR2hRNebasZEETLyM5mAUr0Ku56OkXJ0I7NHJnO6cJiQ==
  dependencies:
    "@babel/helper-annotate-as-pure" "^7.18.6"
    "@babel/helper-plugin-utils" "^7.18.6"

"@babel/plugin-transform-regenerator@^7.18.6":
  version "7.20.5"
  resolved "https://registry.yarnpkg.com/@babel/plugin-transform-regenerator/-/plugin-transform-regenerator-7.20.5.tgz#57cda588c7ffb7f4f8483cc83bdcea02a907f04d"
  integrity sha512-kW/oO7HPBtntbsahzQ0qSE3tFvkFwnbozz3NWFhLGqH75vLEg+sCGngLlhVkePlCs3Jv0dBBHDzCHxNiFAQKCQ==
  dependencies:
    "@babel/helper-plugin-utils" "^7.20.2"
    regenerator-transform "^0.15.1"

"@babel/plugin-transform-reserved-words@^7.18.6":
  version "7.18.6"
  resolved "https://registry.yarnpkg.com/@babel/plugin-transform-reserved-words/-/plugin-transform-reserved-words-7.18.6.tgz#b1abd8ebf8edaa5f7fe6bbb8d2133d23b6a6f76a"
  integrity sha512-oX/4MyMoypzHjFrT1CdivfKZ+XvIPMFXwwxHp/r0Ddy2Vuomt4HDFGmft1TAY2yiTKiNSsh3kjBAzcM8kSdsjA==
  dependencies:
    "@babel/helper-plugin-utils" "^7.18.6"

"@babel/plugin-transform-shorthand-properties@^7.18.6":
  version "7.18.6"
  resolved "https://registry.yarnpkg.com/@babel/plugin-transform-shorthand-properties/-/plugin-transform-shorthand-properties-7.18.6.tgz#6d6df7983d67b195289be24909e3f12a8f664dc9"
  integrity sha512-eCLXXJqv8okzg86ywZJbRn19YJHU4XUa55oz2wbHhaQVn/MM+XhukiT7SYqp/7o00dg52Rj51Ny+Ecw4oyoygw==
  dependencies:
    "@babel/helper-plugin-utils" "^7.18.6"

"@babel/plugin-transform-spread@^7.19.0":
  version "7.20.7"
  resolved "https://registry.yarnpkg.com/@babel/plugin-transform-spread/-/plugin-transform-spread-7.20.7.tgz#c2d83e0b99d3bf83e07b11995ee24bf7ca09401e"
  integrity sha512-ewBbHQ+1U/VnH1fxltbJqDeWBU1oNLG8Dj11uIv3xVf7nrQu0bPGe5Rf716r7K5Qz+SqtAOVswoVunoiBtGhxw==
  dependencies:
    "@babel/helper-plugin-utils" "^7.20.2"
    "@babel/helper-skip-transparent-expression-wrappers" "^7.20.0"

"@babel/plugin-transform-sticky-regex@^7.18.6":
  version "7.18.6"
  resolved "https://registry.yarnpkg.com/@babel/plugin-transform-sticky-regex/-/plugin-transform-sticky-regex-7.18.6.tgz#c6706eb2b1524028e317720339583ad0f444adcc"
  integrity sha512-kfiDrDQ+PBsQDO85yj1icueWMfGfJFKN1KCkndygtu/C9+XUfydLC8Iv5UYJqRwy4zk8EcplRxEOeLyjq1gm6Q==
  dependencies:
    "@babel/helper-plugin-utils" "^7.18.6"

"@babel/plugin-transform-template-literals@^7.18.9":
  version "7.18.9"
  resolved "https://registry.yarnpkg.com/@babel/plugin-transform-template-literals/-/plugin-transform-template-literals-7.18.9.tgz#04ec6f10acdaa81846689d63fae117dd9c243a5e"
  integrity sha512-S8cOWfT82gTezpYOiVaGHrCbhlHgKhQt8XH5ES46P2XWmX92yisoZywf5km75wv5sYcXDUCLMmMxOLCtthDgMA==
  dependencies:
    "@babel/helper-plugin-utils" "^7.18.9"

"@babel/plugin-transform-typeof-symbol@^7.18.9":
  version "7.18.9"
  resolved "https://registry.yarnpkg.com/@babel/plugin-transform-typeof-symbol/-/plugin-transform-typeof-symbol-7.18.9.tgz#c8cea68263e45addcd6afc9091429f80925762c0"
  integrity sha512-SRfwTtF11G2aemAZWivL7PD+C9z52v9EvMqH9BuYbabyPuKUvSWks3oCg6041pT925L4zVFqaVBeECwsmlguEw==
  dependencies:
    "@babel/helper-plugin-utils" "^7.18.9"

"@babel/plugin-transform-typescript@^7.18.6":
  version "7.20.7"
  resolved "https://registry.yarnpkg.com/@babel/plugin-transform-typescript/-/plugin-transform-typescript-7.20.7.tgz#673f49499cd810ae32a1ea5f3f8fab370987e055"
  integrity sha512-m3wVKEvf6SoszD8pu4NZz3PvfKRCMgk6D6d0Qi9hNnlM5M6CFS92EgF4EiHVLKbU0r/r7ty1hg7NPZwE7WRbYw==
  dependencies:
    "@babel/helper-create-class-features-plugin" "^7.20.7"
    "@babel/helper-plugin-utils" "^7.20.2"
    "@babel/plugin-syntax-typescript" "^7.20.0"

"@babel/plugin-transform-unicode-escapes@^7.18.10":
  version "7.18.10"
  resolved "https://registry.yarnpkg.com/@babel/plugin-transform-unicode-escapes/-/plugin-transform-unicode-escapes-7.18.10.tgz#1ecfb0eda83d09bbcb77c09970c2dd55832aa246"
  integrity sha512-kKAdAI+YzPgGY/ftStBFXTI1LZFju38rYThnfMykS+IXy8BVx+res7s2fxf1l8I35DV2T97ezo6+SGrXz6B3iQ==
  dependencies:
    "@babel/helper-plugin-utils" "^7.18.9"

"@babel/plugin-transform-unicode-regex@^7.18.6":
  version "7.18.6"
  resolved "https://registry.yarnpkg.com/@babel/plugin-transform-unicode-regex/-/plugin-transform-unicode-regex-7.18.6.tgz#194317225d8c201bbae103364ffe9e2cea36cdca"
  integrity sha512-gE7A6Lt7YLnNOL3Pb9BNeZvi+d8l7tcRrG4+pwJjK9hD2xX4mEvjlQW60G9EEmfXVYRPv9VRQcyegIVHCql/AA==
  dependencies:
    "@babel/helper-create-regexp-features-plugin" "^7.18.6"
    "@babel/helper-plugin-utils" "^7.18.6"

"@babel/preset-env@^7.19.4":
  version "7.20.2"
  resolved "https://registry.yarnpkg.com/@babel/preset-env/-/preset-env-7.20.2.tgz#9b1642aa47bb9f43a86f9630011780dab7f86506"
  integrity sha512-1G0efQEWR1EHkKvKHqbG+IN/QdgwfByUpM5V5QroDzGV2t3S/WXNQd693cHiHTlCFMpr9B6FkPFXDA2lQcKoDg==
  dependencies:
    "@babel/compat-data" "^7.20.1"
    "@babel/helper-compilation-targets" "^7.20.0"
    "@babel/helper-plugin-utils" "^7.20.2"
    "@babel/helper-validator-option" "^7.18.6"
    "@babel/plugin-bugfix-safari-id-destructuring-collision-in-function-expression" "^7.18.6"
    "@babel/plugin-bugfix-v8-spread-parameters-in-optional-chaining" "^7.18.9"
    "@babel/plugin-proposal-async-generator-functions" "^7.20.1"
    "@babel/plugin-proposal-class-properties" "^7.18.6"
    "@babel/plugin-proposal-class-static-block" "^7.18.6"
    "@babel/plugin-proposal-dynamic-import" "^7.18.6"
    "@babel/plugin-proposal-export-namespace-from" "^7.18.9"
    "@babel/plugin-proposal-json-strings" "^7.18.6"
    "@babel/plugin-proposal-logical-assignment-operators" "^7.18.9"
    "@babel/plugin-proposal-nullish-coalescing-operator" "^7.18.6"
    "@babel/plugin-proposal-numeric-separator" "^7.18.6"
    "@babel/plugin-proposal-object-rest-spread" "^7.20.2"
    "@babel/plugin-proposal-optional-catch-binding" "^7.18.6"
    "@babel/plugin-proposal-optional-chaining" "^7.18.9"
    "@babel/plugin-proposal-private-methods" "^7.18.6"
    "@babel/plugin-proposal-private-property-in-object" "^7.18.6"
    "@babel/plugin-proposal-unicode-property-regex" "^7.18.6"
    "@babel/plugin-syntax-async-generators" "^7.8.4"
    "@babel/plugin-syntax-class-properties" "^7.12.13"
    "@babel/plugin-syntax-class-static-block" "^7.14.5"
    "@babel/plugin-syntax-dynamic-import" "^7.8.3"
    "@babel/plugin-syntax-export-namespace-from" "^7.8.3"
    "@babel/plugin-syntax-import-assertions" "^7.20.0"
    "@babel/plugin-syntax-json-strings" "^7.8.3"
    "@babel/plugin-syntax-logical-assignment-operators" "^7.10.4"
    "@babel/plugin-syntax-nullish-coalescing-operator" "^7.8.3"
    "@babel/plugin-syntax-numeric-separator" "^7.10.4"
    "@babel/plugin-syntax-object-rest-spread" "^7.8.3"
    "@babel/plugin-syntax-optional-catch-binding" "^7.8.3"
    "@babel/plugin-syntax-optional-chaining" "^7.8.3"
    "@babel/plugin-syntax-private-property-in-object" "^7.14.5"
    "@babel/plugin-syntax-top-level-await" "^7.14.5"
    "@babel/plugin-transform-arrow-functions" "^7.18.6"
    "@babel/plugin-transform-async-to-generator" "^7.18.6"
    "@babel/plugin-transform-block-scoped-functions" "^7.18.6"
    "@babel/plugin-transform-block-scoping" "^7.20.2"
    "@babel/plugin-transform-classes" "^7.20.2"
    "@babel/plugin-transform-computed-properties" "^7.18.9"
    "@babel/plugin-transform-destructuring" "^7.20.2"
    "@babel/plugin-transform-dotall-regex" "^7.18.6"
    "@babel/plugin-transform-duplicate-keys" "^7.18.9"
    "@babel/plugin-transform-exponentiation-operator" "^7.18.6"
    "@babel/plugin-transform-for-of" "^7.18.8"
    "@babel/plugin-transform-function-name" "^7.18.9"
    "@babel/plugin-transform-literals" "^7.18.9"
    "@babel/plugin-transform-member-expression-literals" "^7.18.6"
    "@babel/plugin-transform-modules-amd" "^7.19.6"
    "@babel/plugin-transform-modules-commonjs" "^7.19.6"
    "@babel/plugin-transform-modules-systemjs" "^7.19.6"
    "@babel/plugin-transform-modules-umd" "^7.18.6"
    "@babel/plugin-transform-named-capturing-groups-regex" "^7.19.1"
    "@babel/plugin-transform-new-target" "^7.18.6"
    "@babel/plugin-transform-object-super" "^7.18.6"
    "@babel/plugin-transform-parameters" "^7.20.1"
    "@babel/plugin-transform-property-literals" "^7.18.6"
    "@babel/plugin-transform-regenerator" "^7.18.6"
    "@babel/plugin-transform-reserved-words" "^7.18.6"
    "@babel/plugin-transform-shorthand-properties" "^7.18.6"
    "@babel/plugin-transform-spread" "^7.19.0"
    "@babel/plugin-transform-sticky-regex" "^7.18.6"
    "@babel/plugin-transform-template-literals" "^7.18.9"
    "@babel/plugin-transform-typeof-symbol" "^7.18.9"
    "@babel/plugin-transform-unicode-escapes" "^7.18.10"
    "@babel/plugin-transform-unicode-regex" "^7.18.6"
    "@babel/preset-modules" "^0.1.5"
    "@babel/types" "^7.20.2"
    babel-plugin-polyfill-corejs2 "^0.3.3"
    babel-plugin-polyfill-corejs3 "^0.6.0"
    babel-plugin-polyfill-regenerator "^0.4.1"
    core-js-compat "^3.25.1"
    semver "^6.3.0"

"@babel/preset-modules@^0.1.5":
  version "0.1.5"
  resolved "https://registry.yarnpkg.com/@babel/preset-modules/-/preset-modules-0.1.5.tgz#ef939d6e7f268827e1841638dc6ff95515e115d9"
  integrity sha512-A57th6YRG7oR3cq/yt/Y84MvGgE0eJG2F1JLhKuyG+jFxEgrd/HAMJatiFtmOiZurz+0DkrvbheCLaV5f2JfjA==
  dependencies:
    "@babel/helper-plugin-utils" "^7.0.0"
    "@babel/plugin-proposal-unicode-property-regex" "^7.4.4"
    "@babel/plugin-transform-dotall-regex" "^7.4.4"
    "@babel/types" "^7.4.4"
    esutils "^2.0.2"

"@babel/preset-react@^7.18.6":
  version "7.18.6"
  resolved "https://registry.yarnpkg.com/@babel/preset-react/-/preset-react-7.18.6.tgz#979f76d6277048dc19094c217b507f3ad517dd2d"
  integrity sha512-zXr6atUmyYdiWRVLOZahakYmOBHtWc2WGCkP8PYTgZi0iJXDY2CN180TdrIW4OGOAdLc7TifzDIvtx6izaRIzg==
  dependencies:
    "@babel/helper-plugin-utils" "^7.18.6"
    "@babel/helper-validator-option" "^7.18.6"
    "@babel/plugin-transform-react-display-name" "^7.18.6"
    "@babel/plugin-transform-react-jsx" "^7.18.6"
    "@babel/plugin-transform-react-jsx-development" "^7.18.6"
    "@babel/plugin-transform-react-pure-annotations" "^7.18.6"

"@babel/preset-typescript@^7.18.6":
  version "7.18.6"
  resolved "https://registry.yarnpkg.com/@babel/preset-typescript/-/preset-typescript-7.18.6.tgz#ce64be3e63eddc44240c6358daefac17b3186399"
  integrity sha512-s9ik86kXBAnD760aybBucdpnLsAt0jK1xqJn2juOn9lkOvSHV60os5hxoVJsPzMQxvnUJFAlkont2DvvaYEBtQ==
  dependencies:
    "@babel/helper-plugin-utils" "^7.18.6"
    "@babel/helper-validator-option" "^7.18.6"
    "@babel/plugin-transform-typescript" "^7.18.6"

"@babel/runtime-corejs3@^7.10.2":
  version "7.20.7"
  resolved "https://registry.yarnpkg.com/@babel/runtime-corejs3/-/runtime-corejs3-7.20.7.tgz#a1e5ea3d758ba6beb715210142912e3f29981d84"
  integrity sha512-jr9lCZ4RbRQmCR28Q8U8Fu49zvFqLxTY9AMOUz+iyMohMoAgpEcVxY+wJNay99oXOpOcCTODkk70NDN2aaJEeg==
  dependencies:
    core-js-pure "^3.25.1"
    regenerator-runtime "^0.13.11"

"@babel/runtime@^7.10.2", "@babel/runtime@^7.18.9", "@babel/runtime@^7.8.4":
  version "7.20.7"
  resolved "https://registry.yarnpkg.com/@babel/runtime/-/runtime-7.20.7.tgz#fcb41a5a70550e04a7b708037c7c32f7f356d8fd"
  integrity sha512-UF0tvkUtxwAgZ5W/KrkHf0Rn0fdnLDU9ScxBrEVNUprE/MzirjK4MJUX1/BVDv00Sv8cljtukVK1aky++X1SjQ==
  dependencies:
    regenerator-runtime "^0.13.11"

"@babel/template@^7.18.10", "@babel/template@^7.20.7":
  version "7.20.7"
  resolved "https://registry.yarnpkg.com/@babel/template/-/template-7.20.7.tgz#a15090c2839a83b02aa996c0b4994005841fd5a8"
  integrity sha512-8SegXApWe6VoNw0r9JHpSteLKTpTiLZ4rMlGIm9JQ18KiCtyQiAMEazujAHrUS5flrcqYZa75ukev3P6QmUwUw==
  dependencies:
    "@babel/code-frame" "^7.18.6"
    "@babel/parser" "^7.20.7"
    "@babel/types" "^7.20.7"

"@babel/traverse@^7.20.10", "@babel/traverse@^7.20.5", "@babel/traverse@^7.20.7":
  version "7.20.10"
  resolved "https://registry.yarnpkg.com/@babel/traverse/-/traverse-7.20.10.tgz#2bf98239597fcec12f842756f186a9dde6d09230"
  integrity sha512-oSf1juCgymrSez8NI4A2sr4+uB/mFd9MXplYGPEBnfAuWmmyeVcHa6xLPiaRBcXkcb/28bgxmQLTVwFKE1yfsg==
  dependencies:
    "@babel/code-frame" "^7.18.6"
    "@babel/generator" "^7.20.7"
    "@babel/helper-environment-visitor" "^7.18.9"
    "@babel/helper-function-name" "^7.19.0"
    "@babel/helper-hoist-variables" "^7.18.6"
    "@babel/helper-split-export-declaration" "^7.18.6"
    "@babel/parser" "^7.20.7"
    "@babel/types" "^7.20.7"
    debug "^4.1.0"
    globals "^11.1.0"

"@babel/types@^7.18.6", "@babel/types@^7.18.9", "@babel/types@^7.19.0", "@babel/types@^7.20.0", "@babel/types@^7.20.2", "@babel/types@^7.20.5", "@babel/types@^7.20.7", "@babel/types@^7.4.4":
  version "7.20.7"
  resolved "https://registry.yarnpkg.com/@babel/types/-/types-7.20.7.tgz#54ec75e252318423fc07fb644dc6a58a64c09b7f"
  integrity sha512-69OnhBxSSgK0OzTJai4kyPDiKTIe3j+ctaHdIGVbRahTLAT7L3R9oeXHC2aVSuGYt3cVnoAMDmOCgJ2yaiLMvg==
  dependencies:
    "@babel/helper-string-parser" "^7.19.4"
    "@babel/helper-validator-identifier" "^7.19.1"
    to-fast-properties "^2.0.0"

"@csstools/postcss-cascade-layers@^1.1.1":
  version "1.1.1"
  resolved "https://registry.yarnpkg.com/@csstools/postcss-cascade-layers/-/postcss-cascade-layers-1.1.1.tgz#8a997edf97d34071dd2e37ea6022447dd9e795ad"
  integrity sha512-+KdYrpKC5TgomQr2DlZF4lDEpHcoxnj5IGddYYfBWJAKfj1JtuHUIqMa+E1pJJ+z3kvDViWMqyqPlG4Ja7amQA==
  dependencies:
    "@csstools/selector-specificity" "^2.0.2"
    postcss-selector-parser "^6.0.10"

"@csstools/postcss-color-function@^1.1.1":
  version "1.1.1"
  resolved "https://registry.yarnpkg.com/@csstools/postcss-color-function/-/postcss-color-function-1.1.1.tgz#2bd36ab34f82d0497cfacdc9b18d34b5e6f64b6b"
  integrity sha512-Bc0f62WmHdtRDjf5f3e2STwRAl89N2CLb+9iAwzrv4L2hncrbDwnQD9PCq0gtAt7pOI2leIV08HIBUd4jxD8cw==
  dependencies:
    "@csstools/postcss-progressive-custom-properties" "^1.1.0"
    postcss-value-parser "^4.2.0"

"@csstools/postcss-font-format-keywords@^1.0.1":
  version "1.0.1"
  resolved "https://registry.yarnpkg.com/@csstools/postcss-font-format-keywords/-/postcss-font-format-keywords-1.0.1.tgz#677b34e9e88ae997a67283311657973150e8b16a"
  integrity sha512-ZgrlzuUAjXIOc2JueK0X5sZDjCtgimVp/O5CEqTcs5ShWBa6smhWYbS0x5cVc/+rycTDbjjzoP0KTDnUneZGOg==
  dependencies:
    postcss-value-parser "^4.2.0"

"@csstools/postcss-hwb-function@^1.0.2":
  version "1.0.2"
  resolved "https://registry.yarnpkg.com/@csstools/postcss-hwb-function/-/postcss-hwb-function-1.0.2.tgz#ab54a9fce0ac102c754854769962f2422ae8aa8b"
  integrity sha512-YHdEru4o3Rsbjmu6vHy4UKOXZD+Rn2zmkAmLRfPet6+Jz4Ojw8cbWxe1n42VaXQhD3CQUXXTooIy8OkVbUcL+w==
  dependencies:
    postcss-value-parser "^4.2.0"

"@csstools/postcss-ic-unit@^1.0.1":
  version "1.0.1"
  resolved "https://registry.yarnpkg.com/@csstools/postcss-ic-unit/-/postcss-ic-unit-1.0.1.tgz#28237d812a124d1a16a5acc5c3832b040b303e58"
  integrity sha512-Ot1rcwRAaRHNKC9tAqoqNZhjdYBzKk1POgWfhN4uCOE47ebGcLRqXjKkApVDpjifL6u2/55ekkpnFcp+s/OZUw==
  dependencies:
    "@csstools/postcss-progressive-custom-properties" "^1.1.0"
    postcss-value-parser "^4.2.0"

"@csstools/postcss-is-pseudo-class@^2.0.7":
  version "2.0.7"
  resolved "https://registry.yarnpkg.com/@csstools/postcss-is-pseudo-class/-/postcss-is-pseudo-class-2.0.7.tgz#846ae6c0d5a1eaa878fce352c544f9c295509cd1"
  integrity sha512-7JPeVVZHd+jxYdULl87lvjgvWldYu+Bc62s9vD/ED6/QTGjy0jy0US/f6BG53sVMTBJ1lzKZFpYmofBN9eaRiA==
  dependencies:
    "@csstools/selector-specificity" "^2.0.0"
    postcss-selector-parser "^6.0.10"

"@csstools/postcss-nested-calc@^1.0.0":
  version "1.0.0"
  resolved "https://registry.yarnpkg.com/@csstools/postcss-nested-calc/-/postcss-nested-calc-1.0.0.tgz#d7e9d1d0d3d15cf5ac891b16028af2a1044d0c26"
  integrity sha512-JCsQsw1wjYwv1bJmgjKSoZNvf7R6+wuHDAbi5f/7MbFhl2d/+v+TvBTU4BJH3G1X1H87dHl0mh6TfYogbT/dJQ==
  dependencies:
    postcss-value-parser "^4.2.0"

"@csstools/postcss-normalize-display-values@^1.0.1":
  version "1.0.1"
  resolved "https://registry.yarnpkg.com/@csstools/postcss-normalize-display-values/-/postcss-normalize-display-values-1.0.1.tgz#15da54a36e867b3ac5163ee12c1d7f82d4d612c3"
  integrity sha512-jcOanIbv55OFKQ3sYeFD/T0Ti7AMXc9nM1hZWu8m/2722gOTxFg7xYu4RDLJLeZmPUVQlGzo4jhzvTUq3x4ZUw==
  dependencies:
    postcss-value-parser "^4.2.0"

"@csstools/postcss-oklab-function@^1.1.1":
  version "1.1.1"
  resolved "https://registry.yarnpkg.com/@csstools/postcss-oklab-function/-/postcss-oklab-function-1.1.1.tgz#88cee0fbc8d6df27079ebd2fa016ee261eecf844"
  integrity sha512-nJpJgsdA3dA9y5pgyb/UfEzE7W5Ka7u0CX0/HIMVBNWzWemdcTH3XwANECU6anWv/ao4vVNLTMxhiPNZsTK6iA==
  dependencies:
    "@csstools/postcss-progressive-custom-properties" "^1.1.0"
    postcss-value-parser "^4.2.0"

"@csstools/postcss-progressive-custom-properties@^1.1.0", "@csstools/postcss-progressive-custom-properties@^1.3.0":
  version "1.3.0"
  resolved "https://registry.yarnpkg.com/@csstools/postcss-progressive-custom-properties/-/postcss-progressive-custom-properties-1.3.0.tgz#542292558384361776b45c85226b9a3a34f276fa"
  integrity sha512-ASA9W1aIy5ygskZYuWams4BzafD12ULvSypmaLJT2jvQ8G0M3I8PRQhC0h7mG0Z3LI05+agZjqSR9+K9yaQQjA==
  dependencies:
    postcss-value-parser "^4.2.0"

"@csstools/postcss-stepped-value-functions@^1.0.1":
  version "1.0.1"
  resolved "https://registry.yarnpkg.com/@csstools/postcss-stepped-value-functions/-/postcss-stepped-value-functions-1.0.1.tgz#f8772c3681cc2befed695e2b0b1d68e22f08c4f4"
  integrity sha512-dz0LNoo3ijpTOQqEJLY8nyaapl6umbmDcgj4AD0lgVQ572b2eqA1iGZYTTWhrcrHztWDDRAX2DGYyw2VBjvCvQ==
  dependencies:
    postcss-value-parser "^4.2.0"

"@csstools/postcss-text-decoration-shorthand@^1.0.0":
  version "1.0.0"
  resolved "https://registry.yarnpkg.com/@csstools/postcss-text-decoration-shorthand/-/postcss-text-decoration-shorthand-1.0.0.tgz#ea96cfbc87d921eca914d3ad29340d9bcc4c953f"
  integrity sha512-c1XwKJ2eMIWrzQenN0XbcfzckOLLJiczqy+YvfGmzoVXd7pT9FfObiSEfzs84bpE/VqfpEuAZ9tCRbZkZxxbdw==
  dependencies:
    postcss-value-parser "^4.2.0"

"@csstools/postcss-trigonometric-functions@^1.0.2":
  version "1.0.2"
  resolved "https://registry.yarnpkg.com/@csstools/postcss-trigonometric-functions/-/postcss-trigonometric-functions-1.0.2.tgz#94d3e4774c36d35dcdc88ce091336cb770d32756"
  integrity sha512-woKaLO///4bb+zZC2s80l+7cm07M7268MsyG3M0ActXXEFi6SuhvriQYcb58iiKGbjwwIU7n45iRLEHypB47Og==
  dependencies:
    postcss-value-parser "^4.2.0"

"@csstools/postcss-unset-value@^1.0.2":
  version "1.0.2"
  resolved "https://registry.yarnpkg.com/@csstools/postcss-unset-value/-/postcss-unset-value-1.0.2.tgz#c99bb70e2cdc7312948d1eb41df2412330b81f77"
  integrity sha512-c8J4roPBILnelAsdLr4XOAR/GsTm0GJi4XpcfvoWk3U6KiTCqiFYc63KhRMQQX35jYMp4Ao8Ij9+IZRgMfJp1g==

"@csstools/selector-specificity@^2.0.0", "@csstools/selector-specificity@^2.0.2":
  version "2.0.2"
  resolved "https://registry.yarnpkg.com/@csstools/selector-specificity/-/selector-specificity-2.0.2.tgz#1bfafe4b7ed0f3e4105837e056e0a89b108ebe36"
  integrity sha512-IkpVW/ehM1hWKln4fCA3NzJU8KwD+kIOvPZA4cqxoJHtE21CCzjyp+Kxbu0i5I4tBNOlXPL9mjwnWlL0VEG4Fg==

"@eslint/eslintrc@^1.4.0":
  version "1.4.0"
  resolved "https://registry.yarnpkg.com/@eslint/eslintrc/-/eslintrc-1.4.0.tgz#8ec64e0df3e7a1971ee1ff5158da87389f167a63"
  integrity sha512-7yfvXy6MWLgWSFsLhz5yH3iQ52St8cdUY6FoGieKkRDVxuxmrNuUetIuu6cmjNWwniUHiWXjxCr5tTXDrbYS5A==
  dependencies:
    ajv "^6.12.4"
    debug "^4.3.2"
    espree "^9.4.0"
    globals "^13.19.0"
    ignore "^5.2.0"
    import-fresh "^3.2.1"
    js-yaml "^4.1.0"
    minimatch "^3.1.2"
    strip-json-comments "^3.1.1"

"@humanwhocodes/config-array@^0.11.8":
  version "0.11.8"
  resolved "https://registry.yarnpkg.com/@humanwhocodes/config-array/-/config-array-0.11.8.tgz#03595ac2075a4dc0f191cc2131de14fbd7d410b9"
  integrity sha512-UybHIJzJnR5Qc/MsD9Kr+RpO2h+/P1GhOwdiLPXK5TWk5sgTdu88bTD9UP+CKbPPh5Rni1u0GjAdYQLemG8g+g==
  dependencies:
    "@humanwhocodes/object-schema" "^1.2.1"
    debug "^4.1.1"
    minimatch "^3.0.5"

"@humanwhocodes/module-importer@^1.0.1":
  version "1.0.1"
  resolved "https://registry.yarnpkg.com/@humanwhocodes/module-importer/-/module-importer-1.0.1.tgz#af5b2691a22b44be847b0ca81641c5fb6ad0172c"
  integrity sha512-bxveV4V8v5Yb4ncFTT3rPSgZBOpCkjfK0y4oVVVJwIuDVBRMDXrPyXRL988i5ap9m9bnyEEjWfm5WkBmtffLfA==

"@humanwhocodes/object-schema@^1.2.1":
  version "1.2.1"
  resolved "https://registry.yarnpkg.com/@humanwhocodes/object-schema/-/object-schema-1.2.1.tgz#b520529ec21d8e5945a1851dfd1c32e94e39ff45"
  integrity sha512-ZnQMnLV4e7hDlUvw8H+U8ASL02SS2Gn6+9Ac3wGGLIe7+je2AeAOxPY+izIPJDfFDb7eDjev0Us8MO1iFRN8hA==

"@jridgewell/gen-mapping@^0.1.0":
  version "0.1.1"
  resolved "https://registry.yarnpkg.com/@jridgewell/gen-mapping/-/gen-mapping-0.1.1.tgz#e5d2e450306a9491e3bd77e323e38d7aff315996"
  integrity sha512-sQXCasFk+U8lWYEe66WxRDOE9PjVz4vSM51fTu3Hw+ClTpUSQb718772vH3pyS5pShp6lvQM7SxgIDXXXmOX7w==
  dependencies:
    "@jridgewell/set-array" "^1.0.0"
    "@jridgewell/sourcemap-codec" "^1.4.10"

"@jridgewell/gen-mapping@^0.3.2":
  version "0.3.2"
  resolved "https://registry.yarnpkg.com/@jridgewell/gen-mapping/-/gen-mapping-0.3.2.tgz#c1aedc61e853f2bb9f5dfe6d4442d3b565b253b9"
  integrity sha512-mh65xKQAzI6iBcFzwv28KVWSmCkdRBWoOh+bYQGW3+6OZvbbN3TqMGo5hqYxQniRcH9F2VZIoJCm4pa3BPDK/A==
  dependencies:
    "@jridgewell/set-array" "^1.0.1"
    "@jridgewell/sourcemap-codec" "^1.4.10"
    "@jridgewell/trace-mapping" "^0.3.9"

"@jridgewell/resolve-uri@3.1.0":
  version "3.1.0"
  resolved "https://registry.yarnpkg.com/@jridgewell/resolve-uri/-/resolve-uri-3.1.0.tgz#2203b118c157721addfe69d47b70465463066d78"
  integrity sha512-F2msla3tad+Mfht5cJq7LSXcdudKTWCVYUgw6pLFOOHSTtZlj6SWNYAp+AhuqLmWdBO2X5hPrLcu8cVP8fy28w==

"@jridgewell/set-array@^1.0.0", "@jridgewell/set-array@^1.0.1":
  version "1.1.2"
  resolved "https://registry.yarnpkg.com/@jridgewell/set-array/-/set-array-1.1.2.tgz#7c6cf998d6d20b914c0a55a91ae928ff25965e72"
  integrity sha512-xnkseuNADM0gt2bs+BvhO0p78Mk762YnZdsuzFV018NoG1Sj1SCQvpSqa7XUaTam5vAGasABV9qXASMKnFMwMw==

"@jridgewell/sourcemap-codec@1.4.14", "@jridgewell/sourcemap-codec@^1.4.10":
  version "1.4.14"
  resolved "https://registry.yarnpkg.com/@jridgewell/sourcemap-codec/-/sourcemap-codec-1.4.14.tgz#add4c98d341472a289190b424efbdb096991bb24"
  integrity sha512-XPSJHWmi394fuUuzDnGz1wiKqWfo1yXecHQMRf2l6hztTO+nPru658AyDngaBe7isIxEkRsPR3FZh+s7iVa4Uw==

"@jridgewell/trace-mapping@^0.3.9":
  version "0.3.17"
  resolved "https://registry.yarnpkg.com/@jridgewell/trace-mapping/-/trace-mapping-0.3.17.tgz#793041277af9073b0951a7fe0f0d8c4c98c36985"
  integrity sha512-MCNzAp77qzKca9+W/+I0+sEpaUnZoeasnghNeVc41VZCEKaCH73Vq3BZZ/SzWIgrqE4H4ceI+p+b6C0mHf9T4g==
  dependencies:
    "@jridgewell/resolve-uri" "3.1.0"
    "@jridgewell/sourcemap-codec" "1.4.14"

"@mapbox/hast-util-table-cell-style@^0.2.0":
  version "0.2.0"
  resolved "https://registry.yarnpkg.com/@mapbox/hast-util-table-cell-style/-/hast-util-table-cell-style-0.2.0.tgz#1003f59d54fae6f638cb5646f52110fb3da95b4d"
  integrity sha512-gqaTIGC8My3LVSnU38IwjHVKJC94HSonjvFHDk8/aSrApL8v4uWgm8zJkK7MJIIbHuNOr/+Mv2KkQKcxs6LEZA==
  dependencies:
    unist-util-visit "^1.4.1"

"@marp-team/marp-core@^3.6.0":
  version "3.6.0"
  resolved "https://registry.yarnpkg.com/@marp-team/marp-core/-/marp-core-3.6.0.tgz#858958b96208370fe51f4df98642e2bfe2d090c7"
  integrity sha512-V2tA5nLR4HR+hTGrMTaSLB7bDKi+xz1FrhytOyHV/U2ztRRjAKtlQnul+xPZ7LpRxVsLNwbmO/Alw1AwUx7eXQ==
  dependencies:
    "@marp-team/marpit" "^2.4.2"
    "@marp-team/marpit-svg-polyfill" "^2.1.0"
    highlight.js "^11.7.0"
    katex "^0.16.4"
    mathjax-full "^3.2.2"
    postcss "^8.4.21"
    postcss-selector-parser "^6.0.11"
    xss "^1.0.14"

"@marp-team/marpit-svg-polyfill@^2.1.0":
  version "2.1.0"
  resolved "https://registry.yarnpkg.com/@marp-team/marpit-svg-polyfill/-/marpit-svg-polyfill-2.1.0.tgz#40e7ce3a2aa7496748541cc7053e6779d2f866ac"
  integrity sha512-VqCoAKwv1HJdzZp36dDPxznz2JZgRjkVSSPHpCzk72G2N753F0HPKXjevdjxmzN6gir9bUGBgMD1SguWJIi11A==

"@marp-team/marpit@^2.4.2":
  version "2.5.0"
  resolved "https://registry.yarnpkg.com/@marp-team/marpit/-/marpit-2.5.0.tgz#a3e393815b2d831aba04787ea1d67d4e5ca20bbc"
  integrity sha512-VHxBJR4M371u8GmACtacGjcQY3i7wYSUrMmnpp+ic0a0TBIozgbCCaRHZ8mWd0Bn4CYMpl3bKjZoq6x6Lk75fw==
  dependencies:
    color-string "^1.9.1"
    cssesc "^3.0.0"
    js-yaml "^4.1.0"
    lodash.kebabcase "^4.1.1"
    markdown-it "^13.0.1"
    markdown-it-front-matter "^0.2.3"
    postcss "^8.4.24"

"@next/bundle-analyzer@^13.1.1":
  version "13.1.1"
  resolved "https://registry.yarnpkg.com/@next/bundle-analyzer/-/bundle-analyzer-13.1.1.tgz#f36108dcb953ea518253df5eb9e175642f78b04a"
  integrity sha512-zxC/MOj7gDjvQffHT4QZqcPe1Ny+e6o3wethCZn3liSElMA+kxgEopbziTUXdrvJcd/porq+3Itc8P+gxE/xog==
  dependencies:
    webpack-bundle-analyzer "4.7.0"

"@next/env@13.1.1":
  version "13.1.1"
  resolved "https://registry.yarnpkg.com/@next/env/-/env-13.1.1.tgz#6ff26488dc7674ef2bfdd1ca28fe43eed1113bea"
  integrity sha512-vFMyXtPjSAiOXOywMojxfKIqE3VWN5RCAx+tT3AS3pcKjMLFTCJFUWsKv8hC+87Z1F4W3r68qTwDFZIFmd5Xkw==

"@next/eslint-plugin-next@13.1.1":
  version "13.1.1"
  resolved "https://registry.yarnpkg.com/@next/eslint-plugin-next/-/eslint-plugin-next-13.1.1.tgz#cc5e419cc85587f73f2ac0046a91df01dc6fef8b"
  integrity sha512-SBrOFS8PC3nQ5aeZmawJkjKkWjwK9RoxvBSv/86nZp0ubdoVQoko8r8htALd9ufp16NhacCdqhu9bzZLDWtALQ==
  dependencies:
    glob "7.1.7"

"@next/swc-android-arm-eabi@13.1.1":
  version "13.1.1"
  resolved "https://registry.yarnpkg.com/@next/swc-android-arm-eabi/-/swc-android-arm-eabi-13.1.1.tgz#b5c3cd1f79d5c7e6a3b3562785d4e5ac3555b9e1"
  integrity sha512-qnFCx1kT3JTWhWve4VkeWuZiyjG0b5T6J2iWuin74lORCupdrNukxkq9Pm+Z7PsatxuwVJMhjUoYz7H4cWzx2A==

"@next/swc-android-arm64@13.1.1":
  version "13.1.1"
  resolved "https://registry.yarnpkg.com/@next/swc-android-arm64/-/swc-android-arm64-13.1.1.tgz#e2ca9ccbba9ef770cb19fbe96d1ac00fe4cb330d"
  integrity sha512-eCiZhTzjySubNqUnNkQCjU3Fh+ep3C6b5DCM5FKzsTH/3Gr/4Y7EiaPZKILbvnXmhWtKPIdcY6Zjx51t4VeTfA==

"@next/swc-darwin-arm64@13.1.1":
  version "13.1.1"
  resolved "https://registry.yarnpkg.com/@next/swc-darwin-arm64/-/swc-darwin-arm64-13.1.1.tgz#4af00877332231bbd5a3703435fdd0b011e74767"
  integrity sha512-9zRJSSIwER5tu9ADDkPw5rIZ+Np44HTXpYMr0rkM656IvssowPxmhK0rTreC1gpUCYwFsRbxarUJnJsTWiutPg==

"@next/swc-darwin-x64@13.1.1":
  version "13.1.1"
  resolved "https://registry.yarnpkg.com/@next/swc-darwin-x64/-/swc-darwin-x64-13.1.1.tgz#bf4cb09e7e6ec6d91e031118dde2dd17078bcbbc"
  integrity sha512-qWr9qEn5nrnlhB0rtjSdR00RRZEtxg4EGvicIipqZWEyayPxhUu6NwKiG8wZiYZCLfJ5KWr66PGSNeDMGlNaiA==

"@next/swc-freebsd-x64@13.1.1":
  version "13.1.1"
  resolved "https://registry.yarnpkg.com/@next/swc-freebsd-x64/-/swc-freebsd-x64-13.1.1.tgz#6933ea1264328e8523e28818f912cd53824382d4"
  integrity sha512-UwP4w/NcQ7V/VJEj3tGVszgb4pyUCt3lzJfUhjDMUmQbzG9LDvgiZgAGMYH6L21MoyAATJQPDGiAMWAPKsmumA==

"@next/swc-linux-arm-gnueabihf@13.1.1":
  version "13.1.1"
  resolved "https://registry.yarnpkg.com/@next/swc-linux-arm-gnueabihf/-/swc-linux-arm-gnueabihf-13.1.1.tgz#b5896967aaba3873d809c3ad2e2039e89acde419"
  integrity sha512-CnsxmKHco9sosBs1XcvCXP845Db+Wx1G0qouV5+Gr+HT/ZlDYEWKoHVDgnJXLVEQzq4FmHddBNGbXvgqM1Gfkg==

"@next/swc-linux-arm64-gnu@13.1.1":
  version "13.1.1"
  resolved "https://registry.yarnpkg.com/@next/swc-linux-arm64-gnu/-/swc-linux-arm64-gnu-13.1.1.tgz#91b3e9ea8575b1ded421c0ea0739b7bccf228469"
  integrity sha512-JfDq1eri5Dif+VDpTkONRd083780nsMCOKoFG87wA0sa4xL8LGcXIBAkUGIC1uVy9SMsr2scA9CySLD/i+Oqiw==

"@next/swc-linux-arm64-musl@13.1.1":
  version "13.1.1"
  resolved "https://registry.yarnpkg.com/@next/swc-linux-arm64-musl/-/swc-linux-arm64-musl-13.1.1.tgz#83149ea05d7d55f3664d608dbe004c0d125f9147"
  integrity sha512-GA67ZbDq2AW0CY07zzGt07M5b5Yaq5qUpFIoW3UFfjOPgb0Sqf3DAW7GtFMK1sF4ROHsRDMGQ9rnT0VM2dVfKA==

"@next/swc-linux-x64-gnu@13.1.1":
  version "13.1.1"
  resolved "https://registry.yarnpkg.com/@next/swc-linux-x64-gnu/-/swc-linux-x64-gnu-13.1.1.tgz#d7d0777b56de0dd82b78055772e13e18594a15ca"
  integrity sha512-nnjuBrbzvqaOJaV+XgT8/+lmXrSCOt1YYZn/irbDb2fR2QprL6Q7WJNgwsZNxiLSfLdv+2RJGGegBx9sLBEzGA==

"@next/swc-linux-x64-musl@13.1.1":
  version "13.1.1"
  resolved "https://registry.yarnpkg.com/@next/swc-linux-x64-musl/-/swc-linux-x64-musl-13.1.1.tgz#41655722b127133cd95ab5bc8ca1473e9ab6876f"
  integrity sha512-CM9xnAQNIZ8zf/igbIT/i3xWbQZYaF397H+JroF5VMOCUleElaMdQLL5riJml8wUfPoN3dtfn2s4peSr3azz/g==

"@next/swc-win32-arm64-msvc@13.1.1":
  version "13.1.1"
  resolved "https://registry.yarnpkg.com/@next/swc-win32-arm64-msvc/-/swc-win32-arm64-msvc-13.1.1.tgz#f10da3dfc9b3c2bbd202f5d449a9b807af062292"
  integrity sha512-pzUHOGrbgfGgPlOMx9xk3QdPJoRPU+om84hqVoe6u+E0RdwOG0Ho/2UxCgDqmvpUrMab1Deltlt6RqcXFpnigQ==

"@next/swc-win32-ia32-msvc@13.1.1":
  version "13.1.1"
  resolved "https://registry.yarnpkg.com/@next/swc-win32-ia32-msvc/-/swc-win32-ia32-msvc-13.1.1.tgz#4c0102b9b18ece15c818056d07e3917ee9dade78"
  integrity sha512-WeX8kVS46aobM9a7Xr/kEPcrTyiwJqQv/tbw6nhJ4fH9xNZ+cEcyPoQkwPo570dCOLz3Zo9S2q0E6lJ/EAUOBg==

"@next/swc-win32-x64-msvc@13.1.1":
  version "13.1.1"
  resolved "https://registry.yarnpkg.com/@next/swc-win32-x64-msvc/-/swc-win32-x64-msvc-13.1.1.tgz#c209a37da13be27b722f9c40c40ab4b094866244"
  integrity sha512-mVF0/3/5QAc5EGVnb8ll31nNvf3BWpPY4pBb84tk+BfQglWLqc5AC9q1Ht/YMWiEgs8ALNKEQ3GQnbY0bJF2Gg==

"@nodelib/fs.scandir@2.1.5":
  version "2.1.5"
  resolved "https://registry.yarnpkg.com/@nodelib/fs.scandir/-/fs.scandir-2.1.5.tgz#7619c2eb21b25483f6d167548b4cfd5a7488c3d5"
  integrity sha512-vq24Bq3ym5HEQm2NKCr3yXDwjc7vTsEThRDnkp2DK9p1uqLR+DHurm/NOTo0KG7HYHU7eppKZj3MyqYuMBf62g==
  dependencies:
    "@nodelib/fs.stat" "2.0.5"
    run-parallel "^1.1.9"

"@nodelib/fs.stat@2.0.5", "@nodelib/fs.stat@^2.0.2":
  version "2.0.5"
  resolved "https://registry.yarnpkg.com/@nodelib/fs.stat/-/fs.stat-2.0.5.tgz#5bd262af94e9d25bd1e71b05deed44876a222e8b"
  integrity sha512-RkhPPp2zrqDAQA/2jNhnztcPAlv64XdhIp7a7454A5ovI7Bukxgt7MX7udwAu3zg1DcpPU0rz3VV1SeaqvY4+A==

"@nodelib/fs.walk@^1.2.3", "@nodelib/fs.walk@^1.2.8":
  version "1.2.8"
  resolved "https://registry.yarnpkg.com/@nodelib/fs.walk/-/fs.walk-1.2.8.tgz#e95737e8bb6746ddedf69c556953494f196fe69a"
  integrity sha512-oGB+UxlgWcgQkgwo8GcEGwemoTFt3FIO9ababBmaGwXIoBKZ+GTy0pP185beGg7Llih/NSHSV2XAs1lnznocSg==
  dependencies:
    "@nodelib/fs.scandir" "2.1.5"
    fastq "^1.6.0"

"@opencensus/web-types@0.0.7":
  version "0.0.7"
  resolved "https://registry.yarnpkg.com/@opencensus/web-types/-/web-types-0.0.7.tgz#4426de1fe5aa8f624db395d2152b902874f0570a"
  integrity sha512-xB+w7ZDAu3YBzqH44rCmG9/RlrOmFuDPt/bpf17eJr8eZSrLt7nc7LnWdxM9Mmoj/YKMHpxRg28txu3TcpiL+g==

"@opentelemetry/api@1.0.0-rc.0":
  version "1.0.0-rc.0"
  resolved "https://registry.yarnpkg.com/@opentelemetry/api/-/api-1.0.0-rc.0.tgz#0c7c3f5e1285f99cedb563d74ad1adb9822b5144"
  integrity sha512-iXKByCMfrlO5S6Oh97BuM56tM2cIBB0XsL/vWF/AtJrJEKx4MC/Xdu0xDsGXMGcNWpqF7ujMsjjnp0+UHBwnDQ==

"@opentelemetry/api@^0.6.1":
  version "0.6.1"
  resolved "https://registry.yarnpkg.com/@opentelemetry/api/-/api-0.6.1.tgz#a00b504801f408230b9ad719716fe91ad888c642"
  integrity sha512-wpufGZa7tTxw7eAsjXJtiyIQ42IWQdX9iUQp7ACJcKo1hCtuhLU+K2Nv1U6oRwT1oAlZTE6m4CgWKZBhOiau3Q==
  dependencies:
    "@opentelemetry/context-base" "^0.6.1"

"@opentelemetry/context-base@^0.6.1":
  version "0.6.1"
  resolved "https://registry.yarnpkg.com/@opentelemetry/context-base/-/context-base-0.6.1.tgz#b260e454ee4f9635ea024fc83be225e397f15363"
  integrity sha512-5bHhlTBBq82ti3qPT15TRxkYTFPPQWbnkkQkmHPtqiS1XcTB69cEKd3Jm7Cfi/vkPoyxapmePE9tyA7EzLt8SQ==

"@pkgr/utils@^2.3.1":
  version "2.3.1"
  resolved "https://registry.yarnpkg.com/@pkgr/utils/-/utils-2.3.1.tgz#0a9b06ffddee364d6642b3cd562ca76f55b34a03"
  integrity sha512-wfzX8kc1PMyUILA+1Z/EqoE4UCXGy0iRGMhPwdfae1+f0OXlLqCk+By+aMzgJBzR9AzS4CDizioG6Ss1gvAFJw==
  dependencies:
    cross-spawn "^7.0.3"
    is-glob "^4.0.3"
    open "^8.4.0"
    picocolors "^1.0.0"
    tiny-glob "^0.2.9"
    tslib "^2.4.0"

"@polka/url@^1.0.0-next.20":
  version "1.0.0-next.21"
  resolved "https://registry.yarnpkg.com/@polka/url/-/url-1.0.0-next.21.tgz#5de5a2385a35309427f6011992b544514d559aa1"
  integrity sha512-a5Sab1C4/icpTZVzZc5Ghpz88yQtGOyNqYXcZgOssB2uuAr+wF/MvN6bgtW32q7HHrvBki+BsZ0OuNv6EV3K9g==

"@primer/octicons-react@^17.10.0":
  version "17.10.0"
  resolved "https://registry.yarnpkg.com/@primer/octicons-react/-/octicons-react-17.10.0.tgz#69753f8b6977cccb733e791c2ffc31c8f09cbfcb"
  integrity sha512-6uJeWWPrReHNlGLlsp4bL2rmUr1mmlaKfFNTAkVnzi2Nnp8MmLhGhtdWAktXfFUOll1JF4AacrEK3j91Xq99UQ==

"@rushstack/eslint-patch@^1.1.3":
  version "1.2.0"
  resolved "https://registry.yarnpkg.com/@rushstack/eslint-patch/-/eslint-patch-1.2.0.tgz#8be36a1f66f3265389e90b5f9c9962146758f728"
  integrity sha512-sXo/qW2/pAcmT43VoRKOJbDOfV3cYpq3szSVfIThQXNt+E4DfKj361vaAt3c88U5tPUxzEswam7GW48PJqtKAg==

"@rushstack/node-core-library@3.53.3":
  version "3.53.3"
  resolved "https://registry.yarnpkg.com/@rushstack/node-core-library/-/node-core-library-3.53.3.tgz#e78e0dc1545f6cd7d80b0408cf534aefc62fbbe2"
  integrity sha512-H0+T5koi5MFhJUd5ND3dI3bwLhvlABetARl78L3lWftJVQEPyzcgTStvTTRiIM5mCltyTM8VYm6BuCtNUuxD0Q==
  dependencies:
    "@types/node" "12.20.24"
    colors "~1.2.1"
    fs-extra "~7.0.1"
    import-lazy "~4.0.0"
    jju "~1.4.0"
    resolve "~1.17.0"
    semver "~7.3.0"
    z-schema "~5.0.2"

"@rushstack/package-deps-hash@^3.2.4":
  version "3.2.66"
  resolved "https://registry.yarnpkg.com/@rushstack/package-deps-hash/-/package-deps-hash-3.2.66.tgz#1fc4f121500aa3670c4c5edf388722ffb001ddbd"
  integrity sha512-LpsJZ8H7bmEvPEluw9/6Ucf92xiqomZ0P4RSw1YGABYfwt/eOGBYQ2VhyBJsfkQFTRBlIOGCy3GvwvRMRUKz+A==
  dependencies:
    "@rushstack/node-core-library" "3.53.3"

"@svgr/babel-plugin-add-jsx-attribute@^6.5.1":
  version "6.5.1"
  resolved "https://registry.yarnpkg.com/@svgr/babel-plugin-add-jsx-attribute/-/babel-plugin-add-jsx-attribute-6.5.1.tgz#74a5d648bd0347bda99d82409d87b8ca80b9a1ba"
  integrity sha512-9PYGcXrAxitycIjRmZB+Q0JaN07GZIWaTBIGQzfaZv+qr1n8X1XUEJ5rZ/vx6OVD9RRYlrNnXWExQXcmZeD/BQ==

"@svgr/babel-plugin-remove-jsx-attribute@*":
  version "6.5.0"
  resolved "https://registry.yarnpkg.com/@svgr/babel-plugin-remove-jsx-attribute/-/babel-plugin-remove-jsx-attribute-6.5.0.tgz#652bfd4ed0a0699843585cda96faeb09d6e1306e"
  integrity sha512-8zYdkym7qNyfXpWvu4yq46k41pyNM9SOstoWhKlm+IfdCE1DdnRKeMUPsWIEO/DEkaWxJ8T9esNdG3QwQ93jBA==

"@svgr/babel-plugin-remove-jsx-empty-expression@*":
  version "6.5.0"
  resolved "https://registry.yarnpkg.com/@svgr/babel-plugin-remove-jsx-empty-expression/-/babel-plugin-remove-jsx-empty-expression-6.5.0.tgz#4b78994ab7d39032c729903fc2dd5c0fa4565cb8"
  integrity sha512-NFdxMq3xA42Kb1UbzCVxplUc0iqSyM9X8kopImvFnB+uSDdzIHOdbs1op8ofAvVRtbg4oZiyRl3fTYeKcOe9Iw==

"@svgr/babel-plugin-replace-jsx-attribute-value@^6.5.1":
  version "6.5.1"
  resolved "https://registry.yarnpkg.com/@svgr/babel-plugin-replace-jsx-attribute-value/-/babel-plugin-replace-jsx-attribute-value-6.5.1.tgz#fb9d22ea26d2bc5e0a44b763d4c46d5d3f596c60"
  integrity sha512-8DPaVVE3fd5JKuIC29dqyMB54sA6mfgki2H2+swh+zNJoynC8pMPzOkidqHOSc6Wj032fhl8Z0TVn1GiPpAiJg==

"@svgr/babel-plugin-svg-dynamic-title@^6.5.1":
  version "6.5.1"
  resolved "https://registry.yarnpkg.com/@svgr/babel-plugin-svg-dynamic-title/-/babel-plugin-svg-dynamic-title-6.5.1.tgz#01b2024a2b53ffaa5efceaa0bf3e1d5a4c520ce4"
  integrity sha512-FwOEi0Il72iAzlkaHrlemVurgSQRDFbk0OC8dSvD5fSBPHltNh7JtLsxmZUhjYBZo2PpcU/RJvvi6Q0l7O7ogw==

"@svgr/babel-plugin-svg-em-dimensions@^6.5.1":
  version "6.5.1"
  resolved "https://registry.yarnpkg.com/@svgr/babel-plugin-svg-em-dimensions/-/babel-plugin-svg-em-dimensions-6.5.1.tgz#dd3fa9f5b24eb4f93bcf121c3d40ff5facecb217"
  integrity sha512-gWGsiwjb4tw+ITOJ86ndY/DZZ6cuXMNE/SjcDRg+HLuCmwpcjOktwRF9WgAiycTqJD/QXqL2f8IzE2Rzh7aVXA==

"@svgr/babel-plugin-transform-react-native-svg@^6.5.1":
  version "6.5.1"
  resolved "https://registry.yarnpkg.com/@svgr/babel-plugin-transform-react-native-svg/-/babel-plugin-transform-react-native-svg-6.5.1.tgz#1d8e945a03df65b601551097d8f5e34351d3d305"
  integrity sha512-2jT3nTayyYP7kI6aGutkyfJ7UMGtuguD72OjeGLwVNyfPRBD8zQthlvL+fAbAKk5n9ZNcvFkp/b1lZ7VsYqVJg==

"@svgr/babel-plugin-transform-svg-component@^6.5.1":
  version "6.5.1"
  resolved "https://registry.yarnpkg.com/@svgr/babel-plugin-transform-svg-component/-/babel-plugin-transform-svg-component-6.5.1.tgz#48620b9e590e25ff95a80f811544218d27f8a250"
  integrity sha512-a1p6LF5Jt33O3rZoVRBqdxL350oge54iZWHNI6LJB5tQ7EelvD/Mb1mfBiZNAan0dt4i3VArkFRjA4iObuNykQ==

"@svgr/babel-preset@^6.5.1":
  version "6.5.1"
  resolved "https://registry.yarnpkg.com/@svgr/babel-preset/-/babel-preset-6.5.1.tgz#b90de7979c8843c5c580c7e2ec71f024b49eb828"
  integrity sha512-6127fvO/FF2oi5EzSQOAjo1LE3OtNVh11R+/8FXa+mHx1ptAaS4cknIjnUA7e6j6fwGGJ17NzaTJFUwOV2zwCw==
  dependencies:
    "@svgr/babel-plugin-add-jsx-attribute" "^6.5.1"
    "@svgr/babel-plugin-remove-jsx-attribute" "*"
    "@svgr/babel-plugin-remove-jsx-empty-expression" "*"
    "@svgr/babel-plugin-replace-jsx-attribute-value" "^6.5.1"
    "@svgr/babel-plugin-svg-dynamic-title" "^6.5.1"
    "@svgr/babel-plugin-svg-em-dimensions" "^6.5.1"
    "@svgr/babel-plugin-transform-react-native-svg" "^6.5.1"
    "@svgr/babel-plugin-transform-svg-component" "^6.5.1"

"@svgr/core@^6.5.1":
  version "6.5.1"
  resolved "https://registry.yarnpkg.com/@svgr/core/-/core-6.5.1.tgz#d3e8aa9dbe3fbd747f9ee4282c1c77a27410488a"
  integrity sha512-/xdLSWxK5QkqG524ONSjvg3V/FkNyCv538OIBdQqPNaAta3AsXj/Bd2FbvR87yMbXO2hFSWiAe/Q6IkVPDw+mw==
  dependencies:
    "@babel/core" "^7.19.6"
    "@svgr/babel-preset" "^6.5.1"
    "@svgr/plugin-jsx" "^6.5.1"
    camelcase "^6.2.0"
    cosmiconfig "^7.0.1"

"@svgr/hast-util-to-babel-ast@^6.5.1":
  version "6.5.1"
  resolved "https://registry.yarnpkg.com/@svgr/hast-util-to-babel-ast/-/hast-util-to-babel-ast-6.5.1.tgz#81800bd09b5bcdb968bf6ee7c863d2288fdb80d2"
  integrity sha512-1hnUxxjd83EAxbL4a0JDJoD3Dao3hmjvyvyEV8PzWmLK3B9m9NPlW7GKjFyoWE8nM7HnXzPcmmSyOW8yOddSXw==
  dependencies:
    "@babel/types" "^7.20.0"
    entities "^4.4.0"

"@svgr/plugin-jsx@^6.5.1":
  version "6.5.1"
  resolved "https://registry.yarnpkg.com/@svgr/plugin-jsx/-/plugin-jsx-6.5.1.tgz#0e30d1878e771ca753c94e69581c7971542a7072"
  integrity sha512-+UdQxI3jgtSjCykNSlEMuy1jSRQlGC7pqBCPvkG/2dATdWo082zHTTK3uhnAju2/6XpE6B5mZ3z4Z8Ns01S8Gw==
  dependencies:
    "@babel/core" "^7.19.6"
    "@svgr/babel-preset" "^6.5.1"
    "@svgr/hast-util-to-babel-ast" "^6.5.1"
    svg-parser "^2.0.4"

"@svgr/plugin-svgo@^6.5.1":
  version "6.5.1"
  resolved "https://registry.yarnpkg.com/@svgr/plugin-svgo/-/plugin-svgo-6.5.1.tgz#0f91910e988fc0b842f88e0960c2862e022abe84"
  integrity sha512-omvZKf8ixP9z6GWgwbtmP9qQMPX4ODXi+wzbVZgomNFsUIlHA1sf4fThdwTWSsZGgvGAG6yE+b/F5gWUkcZ/iQ==
  dependencies:
    cosmiconfig "^7.0.1"
    deepmerge "^4.2.2"
    svgo "^2.8.0"

"@svgr/webpack@^6.5.1":
  version "6.5.1"
  resolved "https://registry.yarnpkg.com/@svgr/webpack/-/webpack-6.5.1.tgz#ecf027814fc1cb2decc29dc92f39c3cf691e40e8"
  integrity sha512-cQ/AsnBkXPkEK8cLbv4Dm7JGXq2XrumKnL1dRpJD9rIO2fTIlJI9a1uCciYG1F2aUsox/hJQyNGbt3soDxSRkA==
  dependencies:
    "@babel/core" "^7.19.6"
    "@babel/plugin-transform-react-constant-elements" "^7.18.12"
    "@babel/preset-env" "^7.19.4"
    "@babel/preset-react" "^7.18.6"
    "@babel/preset-typescript" "^7.18.6"
    "@svgr/core" "^6.5.1"
    "@svgr/plugin-jsx" "^6.5.1"
    "@svgr/plugin-svgo" "^6.5.1"

"@swc/helpers@0.4.14":
  version "0.4.14"
  resolved "https://registry.yarnpkg.com/@swc/helpers/-/helpers-0.4.14.tgz#1352ac6d95e3617ccb7c1498ff019654f1e12a74"
  integrity sha512-4C7nX/dvpzB7za4Ql9K81xK3HPxCpHMgwTZVyf+9JQ6VUbn9jjZVN7/Nkdz/Ugzs2CSjqnL/UPXroiVBVHUWUw==
  dependencies:
    tslib "^2.4.0"

"@trysound/sax@0.2.0":
  version "0.2.0"
  resolved "https://registry.yarnpkg.com/@trysound/sax/-/sax-0.2.0.tgz#cccaab758af56761eb7bf37af6f03f326dd798ad"
  integrity sha512-L7z9BgrNEcYyUYtF+HaEfiS5ebkh9jXqbszz7pC0hRBPaatV0XjSD3+eHrpqFemQfgwiFF0QPIarnIihIDn7OA==

"@tsconfig/recommended@^1.0.1":
  version "1.0.1"
  resolved "https://registry.yarnpkg.com/@tsconfig/recommended/-/recommended-1.0.1.tgz#7619bad397e06ead1c5182926c944e0ca6177f52"
  integrity sha512-2xN+iGTbPBEzGSnVp/Hd64vKJCJWxsi9gfs88x4PPMyEjHJoA3o5BY9r5OLPHIZU2pAQxkSAsJFqn6itClP8mQ==

"@types/classnames@^2.3.1":
  version "2.3.1"
  resolved "https://registry.yarnpkg.com/@types/classnames/-/classnames-2.3.1.tgz#3c2467aa0f1a93f1f021e3b9bcf938bd5dfdc0dd"
  integrity sha512-zeOWb0JGBoVmlQoznvqXbE0tEC/HONsnoUNH19Hc96NFsTAwTXbTqb8FMYkru1F/iqp7a18Ws3nWJvtA1sHD1A==
  dependencies:
    classnames "*"

"@types/debug@^4.0.0":
  version "4.1.7"
  resolved "https://registry.yarnpkg.com/@types/debug/-/debug-4.1.7.tgz#7cc0ea761509124709b8b2d1090d8f6c17aadb82"
  integrity sha512-9AonUzyTjXXhEOa0DnqpzZi6VHlqKMswga9EXjpXnnqxwLtdvPPtlO8evrI5D9S6asFRCQ6v+wpiUKbw+vKqyg==
  dependencies:
    "@types/ms" "*"

"@types/hast@^2.0.0", "@types/hast@^2.3.2":
  version "2.3.4"
  resolved "https://registry.yarnpkg.com/@types/hast/-/hast-2.3.4.tgz#8aa5ef92c117d20d974a82bdfb6a648b08c0bafc"
  integrity sha512-wLEm0QvaoawEDoTRwzTXp4b4jpwiJDvR5KMnFnVodm3scufTlBOWRD6N1OBf9TZMhjlNsSfcO5V+7AF4+Vy+9g==
  dependencies:
    "@types/unist" "*"

"@types/json-schema@^7.0.8", "@types/json-schema@^7.0.9":
  version "7.0.11"
  resolved "https://registry.yarnpkg.com/@types/json-schema/-/json-schema-7.0.11.tgz#d421b6c527a3037f7c84433fd2c4229e016863d3"
  integrity sha512-wOuvG1SN4Us4rez+tylwwwCV1psiNVOkJeM3AUWUNWg/jDQY2+HE/444y5gc+jBmRqASOm2Oeh5c1axHobwRKQ==

"@types/json5@^0.0.29":
  version "0.0.29"
  resolved "https://registry.yarnpkg.com/@types/json5/-/json5-0.0.29.tgz#ee28707ae94e11d2b827bcbe5270bcea7f3e71ee"
  integrity sha512-dRLjCWHYg4oaA77cxO64oO+7JwCwnIzkZPdrrC71jQmQtlhM556pwKo5bUzqvZndkVbeFLIIi+9TC40JNF5hNQ==

"@types/mdast@^3.0.0":
  version "3.0.10"
  resolved "https://registry.yarnpkg.com/@types/mdast/-/mdast-3.0.10.tgz#4724244a82a4598884cbbe9bcfd73dff927ee8af"
  integrity sha512-W864tg/Osz1+9f4lrGTZpCSO5/z4608eUp19tbozkq2HJK6i3z1kT0H9tlADXuYIb1YYOBByU4Jsqkk75q48qA==
  dependencies:
    "@types/unist" "*"

"@types/mdurl@^1.0.0":
  version "1.0.2"
  resolved "https://registry.yarnpkg.com/@types/mdurl/-/mdurl-1.0.2.tgz#e2ce9d83a613bacf284c7be7d491945e39e1f8e9"
  integrity sha512-eC4U9MlIcu2q0KQmXszyn5Akca/0jrQmwDRgpAMJai7qBWq4amIQhZyNau4VYGtCeALvW1/NtjzJJ567aZxfKA==

"@types/ms@*":
  version "0.7.31"
  resolved "https://registry.yarnpkg.com/@types/ms/-/ms-0.7.31.tgz#31b7ca6407128a3d2bbc27fe2d21b345397f6197"
  integrity sha512-iiUgKzV9AuaEkZqkOLDIvlQiL6ltuZd9tGcW3gwpnX8JbuiuhFlEGmmFXEXkN50Cvq7Os88IY2v0dkDqXYWVgA==

"@types/node-fetch@^2.5.0":
  version "2.6.2"
  resolved "https://registry.yarnpkg.com/@types/node-fetch/-/node-fetch-2.6.2.tgz#d1a9c5fd049d9415dce61571557104dec3ec81da"
  integrity sha512-DHqhlq5jeESLy19TYhLakJ07kNumXWjcDdxXsLUMJZ6ue8VZJj4kLPQVE/2mdHh3xZziNF1xppu5lwmS53HR+A==
  dependencies:
    "@types/node" "*"
    form-data "^3.0.0"

"@types/node@*", "@types/node@~18.11.18":
  version "18.11.18"
  resolved "https://registry.yarnpkg.com/@types/node/-/node-18.11.18.tgz#8dfb97f0da23c2293e554c5a50d61ef134d7697f"
  integrity sha512-DHQpWGjyQKSHj3ebjFI/wRKcqQcdR+MoFBygntYOZytCqNfkd2ZC4ARDJ2DQqhjH5p85Nnd3jhUJIXrszFX/JA==

"@types/node@12.20.24":
  version "12.20.24"
  resolved "https://registry.yarnpkg.com/@types/node/-/node-12.20.24.tgz#c37ac69cb2948afb4cef95f424fa0037971a9a5c"
  integrity sha512-yxDeaQIAJlMav7fH5AQqPH1u8YIuhYJXYBzxaQ4PifsU0GDO38MSdmEDeRlIxrKbC6NbEaaEHDanWb+y30U8SQ==

"@types/parse-json@^4.0.0":
  version "4.0.0"
  resolved "https://registry.yarnpkg.com/@types/parse-json/-/parse-json-4.0.0.tgz#2f8bb441434d163b35fb8ffdccd7138927ffb8c0"
  integrity sha512-//oorEZjL6sbPcKUaCdIGlIUeH26mgzimjBB77G6XRgnDl/L5wOnpyBGRe/Mmf5CVW3PwEBE1NjiMZ/ssFh4wA==

"@types/prop-types@*":
  version "15.7.5"
  resolved "https://registry.yarnpkg.com/@types/prop-types/-/prop-types-15.7.5.tgz#5f19d2b85a98e9558036f6a3cacc8819420f05cf"
  integrity sha512-JCB8C6SnDoQf0cNycqd/35A7MjcnK+ZTqE7judS6o7utxUCg6imJg3QK2qzHKszlTjcj2cn+NwMB2i96ubpj7w==

"@types/react@^17.0.0":
  version "17.0.52"
  resolved "https://registry.yarnpkg.com/@types/react/-/react-17.0.52.tgz#10d8b907b5c563ac014a541f289ae8eaa9bf2e9b"
  integrity sha512-vwk8QqVODi0VaZZpDXQCmEmiOuyjEFPY7Ttaw5vjM112LOq37yz1CDJGrRJwA1fYEq4Iitd5rnjd1yWAc/bT+A==
  dependencies:
    "@types/prop-types" "*"
    "@types/scheduler" "*"
    csstype "^3.0.2"

"@types/react@^18.0.26":
  version "18.0.26"
  resolved "https://registry.yarnpkg.com/@types/react/-/react-18.0.26.tgz#8ad59fc01fef8eaf5c74f4ea392621749f0b7917"
  integrity sha512-hCR3PJQsAIXyxhTNSiDFY//LhnMZWpNNr5etoCqx/iUfGc5gXWtQR2Phl908jVR6uPXacojQWTg4qRpkxTuGug==
  dependencies:
    "@types/prop-types" "*"
    "@types/scheduler" "*"
    csstype "^3.0.2"

"@types/resize-observer-browser@^0.1.7":
  version "0.1.7"
  resolved "https://registry.yarnpkg.com/@types/resize-observer-browser/-/resize-observer-browser-0.1.7.tgz#294aaadf24ac6580b8fbd1fe3ab7b59fe85f9ef3"
  integrity sha512-G9eN0Sn0ii9PWQ3Vl72jDPgeJwRWhv2Qk/nQkJuWmRmOB4HX3/BhD5SE1dZs/hzPZL/WKnvF0RHdTSG54QJFyg==

"@types/scheduler@*":
  version "0.16.2"
  resolved "https://registry.yarnpkg.com/@types/scheduler/-/scheduler-0.16.2.tgz#1a62f89525723dde24ba1b01b092bf5df8ad4d39"
  integrity sha512-hppQEBDmlwhFAXKJX2KnWLYu5yMfi91yazPb2l+lbJiwW+wdo1gNeRA+3RgNSO39WYX2euey41KEwnqesU2Jew==

"@types/semver@^7.3.12":
  version "7.3.13"
  resolved "https://registry.yarnpkg.com/@types/semver/-/semver-7.3.13.tgz#da4bfd73f49bd541d28920ab0e2bf0ee80f71c91"
  integrity sha512-21cFJr9z3g5dW8B0CVI9g2O9beqaThGQ6ZFBqHfwhzLDKUxaqTIy3vnfah/UPkfOiF2pLq+tGz+W8RyCskuslw==

"@types/tunnel@^0.0.1":
  version "0.0.1"
  resolved "https://registry.yarnpkg.com/@types/tunnel/-/tunnel-0.0.1.tgz#0d72774768b73df26f25df9184273a42da72b19c"
  integrity sha512-AOqu6bQu5MSWwYvehMXLukFHnupHrpZ8nvgae5Ggie9UwzDR1CCwoXgSSWNZJuyOlCdfdsWMA5F2LlmvyoTv8A==
  dependencies:
    "@types/node" "*"

"@types/unist@*", "@types/unist@^2.0.0":
  version "2.0.6"
  resolved "https://registry.yarnpkg.com/@types/unist/-/unist-2.0.6.tgz#250a7b16c3b91f672a24552ec64678eeb1d3a08d"
  integrity sha512-PBjIUxZHOuj0R15/xuwJYjFi+KZdNFrehocChv4g5hu6aFroHue8m0lBP0POdK2nKzbw0cgV1mws8+V/JAcEkQ==

"@types/webpack-env@^1.18.0":
  version "1.18.0"
  resolved "https://registry.yarnpkg.com/@types/webpack-env/-/webpack-env-1.18.0.tgz#ed6ecaa8e5ed5dfe8b2b3d00181702c9925f13fb"
  integrity sha512-56/MAlX5WMsPVbOg7tAxnYvNYMMWr/QJiIp6BxVSW3JJXUVzzOn64qW8TzQyMSqSUFM2+PVI4aUHcHOzIz/1tg==

"@typescript-eslint/eslint-plugin@^5.47.1":
  version "5.47.1"
  resolved "https://registry.yarnpkg.com/@typescript-eslint/eslint-plugin/-/eslint-plugin-5.47.1.tgz#50cc5085578a7fa22cd46a0806c2e5eae858af02"
  integrity sha512-r4RZ2Jl9kcQN7K/dcOT+J7NAimbiis4sSM9spvWimsBvDegMhKLA5vri2jG19PmIPbDjPeWzfUPQ2hjEzA4Nmg==
  dependencies:
    "@typescript-eslint/scope-manager" "5.47.1"
    "@typescript-eslint/type-utils" "5.47.1"
    "@typescript-eslint/utils" "5.47.1"
    debug "^4.3.4"
    ignore "^5.2.0"
    natural-compare-lite "^1.4.0"
    regexpp "^3.2.0"
    semver "^7.3.7"
    tsutils "^3.21.0"

"@typescript-eslint/parser@^5.42.0", "@typescript-eslint/parser@^5.47.1":
  version "5.47.1"
  resolved "https://registry.yarnpkg.com/@typescript-eslint/parser/-/parser-5.47.1.tgz#c4bf16f8c3c7608ce4bf8ff804b677fc899f173f"
  integrity sha512-9Vb+KIv29r6GPu4EboWOnQM7T+UjpjXvjCPhNORlgm40a9Ia9bvaPJswvtae1gip2QEeVeGh6YquqAzEgoRAlw==
  dependencies:
    "@typescript-eslint/scope-manager" "5.47.1"
    "@typescript-eslint/types" "5.47.1"
    "@typescript-eslint/typescript-estree" "5.47.1"
    debug "^4.3.4"

"@typescript-eslint/scope-manager@5.47.1":
  version "5.47.1"
  resolved "https://registry.yarnpkg.com/@typescript-eslint/scope-manager/-/scope-manager-5.47.1.tgz#0d302b3c2f20ab24e4787bf3f5a0d8c449b823bd"
  integrity sha512-9hsFDsgUwrdOoW1D97Ewog7DYSHaq4WKuNs0LHF9RiCmqB0Z+XRR4Pf7u7u9z/8CciHuJ6yxNws1XznI3ddjEw==
  dependencies:
    "@typescript-eslint/types" "5.47.1"
    "@typescript-eslint/visitor-keys" "5.47.1"

"@typescript-eslint/type-utils@5.47.1":
  version "5.47.1"
  resolved "https://registry.yarnpkg.com/@typescript-eslint/type-utils/-/type-utils-5.47.1.tgz#aee13314f840ab336c1adb49a300856fd16d04ce"
  integrity sha512-/UKOeo8ee80A7/GJA427oIrBi/Gd4osk/3auBUg4Rn9EahFpevVV1mUK8hjyQD5lHPqX397x6CwOk5WGh1E/1w==
  dependencies:
    "@typescript-eslint/typescript-estree" "5.47.1"
    "@typescript-eslint/utils" "5.47.1"
    debug "^4.3.4"
    tsutils "^3.21.0"

"@typescript-eslint/types@5.47.1":
  version "5.47.1"
  resolved "https://registry.yarnpkg.com/@typescript-eslint/types/-/types-5.47.1.tgz#459f07428aec5a8c4113706293c2ae876741ac8e"
  integrity sha512-CmALY9YWXEpwuu6377ybJBZdtSAnzXLSQcxLSqSQSbC7VfpMu/HLVdrnVJj7ycI138EHqocW02LPJErE35cE9A==

"@typescript-eslint/typescript-estree@5.47.1":
  version "5.47.1"
  resolved "https://registry.yarnpkg.com/@typescript-eslint/typescript-estree/-/typescript-estree-5.47.1.tgz#b9d8441308aca53df7f69b2c67a887b82c9ed418"
  integrity sha512-4+ZhFSuISAvRi2xUszEj0xXbNTHceV9GbH9S8oAD2a/F9SW57aJNQVOCxG8GPfSWH/X4eOPdMEU2jYVuWKEpWA==
  dependencies:
    "@typescript-eslint/types" "5.47.1"
    "@typescript-eslint/visitor-keys" "5.47.1"
    debug "^4.3.4"
    globby "^11.1.0"
    is-glob "^4.0.3"
    semver "^7.3.7"
    tsutils "^3.21.0"

"@typescript-eslint/utils@5.47.1":
  version "5.47.1"
  resolved "https://registry.yarnpkg.com/@typescript-eslint/utils/-/utils-5.47.1.tgz#595f25ac06e9ee28c339fd43c709402820b13d7b"
  integrity sha512-l90SdwqfmkuIVaREZ2ykEfCezepCLxzWMo5gVfcJsJCaT4jHT+QjgSkYhs5BMQmWqE9k3AtIfk4g211z/sTMVw==
  dependencies:
    "@types/json-schema" "^7.0.9"
    "@types/semver" "^7.3.12"
    "@typescript-eslint/scope-manager" "5.47.1"
    "@typescript-eslint/types" "5.47.1"
    "@typescript-eslint/typescript-estree" "5.47.1"
    eslint-scope "^5.1.1"
    eslint-utils "^3.0.0"
    semver "^7.3.7"

"@typescript-eslint/visitor-keys@5.47.1":
  version "5.47.1"
  resolved "https://registry.yarnpkg.com/@typescript-eslint/visitor-keys/-/visitor-keys-5.47.1.tgz#d35c2da544dbb685db9c5b5b85adac0a1d74d1f2"
  integrity sha512-rF3pmut2JCCjh6BLRhNKdYjULMb1brvoaiWDlHfLNVgmnZ0sBVJrs3SyaKE1XoDDnJuAx/hDQryHYmPUuNq0ig==
  dependencies:
    "@typescript-eslint/types" "5.47.1"
    eslint-visitor-keys "^3.3.0"

"@xmldom/xmldom@^0.8.0":
  version "0.8.6"
  resolved "https://registry.yarnpkg.com/@xmldom/xmldom/-/xmldom-0.8.6.tgz#8a1524eb5bd5e965c1e3735476f0262469f71440"
  integrity sha512-uRjjusqpoqfmRkTaNuLJ2VohVr67Q5YwDATW3VU7PfzTj6IRaihGrYI7zckGZjxQPBIp63nfvJbM+Yu5ICh0Bg==

"@yarnpkg/lockfile@^1.1.0":
  version "1.1.0"
  resolved "https://registry.yarnpkg.com/@yarnpkg/lockfile/-/lockfile-1.1.0.tgz#e77a97fbd345b76d83245edcd17d393b1b41fb31"
  integrity sha512-GpSwvyXOcOOlV70vbnzjj4fW5xW/FdUF6nQEt1ENy7m4ZCczi1+/buVUPAqmGfqznsORNFzUMjctTIp8a9tuCQ==

abort-controller@^3.0.0:
  version "3.0.0"
  resolved "https://registry.yarnpkg.com/abort-controller/-/abort-controller-3.0.0.tgz#eaf54d53b62bae4138e809ca225c8439a6efb392"
  integrity sha512-h8lQ8tacZYnR3vNQTgibj+tODHI5/+l06Au2Pcriv/Gmet0eaj4TwWH41sO9wnHDiQsEj19q0drzdWdeAHtweg==
  dependencies:
    event-target-shim "^5.0.0"

acorn-jsx@^5.3.2:
  version "5.3.2"
  resolved "https://registry.yarnpkg.com/acorn-jsx/-/acorn-jsx-5.3.2.tgz#7ed5bb55908b3b2f1bc55c6af1653bada7f07937"
  integrity sha512-rq9s+JNhf0IChjtDXxllJ7g41oZk5SlXtp0LHwyA5cejwn7vKmKp4pPri6YEePv2PU65sAsegbXtIinmDFDXgQ==

acorn-node@^1.8.2:
  version "1.8.2"
  resolved "https://registry.yarnpkg.com/acorn-node/-/acorn-node-1.8.2.tgz#114c95d64539e53dede23de8b9d96df7c7ae2af8"
  integrity sha512-8mt+fslDufLYntIoPAaIMUe/lrbrehIiwmR3t2k9LljIzoigEPF27eLk2hy8zSGzmR/ogr7zbRKINMo1u0yh5A==
  dependencies:
    acorn "^7.0.0"
    acorn-walk "^7.0.0"
    xtend "^4.0.2"

acorn-walk@^7.0.0:
  version "7.2.0"
  resolved "https://registry.yarnpkg.com/acorn-walk/-/acorn-walk-7.2.0.tgz#0de889a601203909b0fbe07b8938dc21d2e967bc"
  integrity sha512-OPdCF6GsMIP+Az+aWfAAOEt2/+iVDKE7oy6lJ098aoe59oAmK76qV6Gw60SbZ8jHuG2wH058GF4pLFbYamYrVA==

acorn-walk@^8.0.0:
  version "8.2.0"
  resolved "https://registry.yarnpkg.com/acorn-walk/-/acorn-walk-8.2.0.tgz#741210f2e2426454508853a2f44d0ab83b7f69c1"
  integrity sha512-k+iyHEuPgSw6SbuDpGQM+06HQUa04DZ3o+F6CSzXMvvI5KMvnaEqXe+YVe555R9nn6GPt404fos4wcgpw12SDA==

acorn@^7.0.0:
  version "7.4.1"
  resolved "https://registry.yarnpkg.com/acorn/-/acorn-7.4.1.tgz#feaed255973d2e77555b83dbc08851a6c63520fa"
  integrity sha512-nQyp0o1/mNdbTO1PO6kHkwSrmgZ0MT/jCCpNiwbUjGoRN4dlBhqJtoQuCnEOKzgTVwg0ZWiCoQy6SxMebQVh8A==

acorn@^8.0.4, acorn@^8.8.0:
  version "8.8.1"
  resolved "https://registry.yarnpkg.com/acorn/-/acorn-8.8.1.tgz#0a3f9cbecc4ec3bea6f0a80b66ae8dd2da250b73"
  integrity sha512-7zFpHzhnqYKrkYdUjF1HI1bzd0VygEGX8lFk4k5zVMqHEoES+P+7TKI+EvLO9WVMJ8eekdO0aDEK044xTXwPPA==

ajv-keywords@^3.5.2:
  version "3.5.2"
  resolved "https://registry.yarnpkg.com/ajv-keywords/-/ajv-keywords-3.5.2.tgz#31f29da5ab6e00d1c2d329acf7b5929614d5014d"
  integrity sha512-5p6WTN0DdTGVQk6VjcEju19IgaHudalcfabD7yhDGeA6bcQnmL+CpveLJq/3hvfwd1aof6L386Ougkx6RfyMIQ==

ajv@^6.10.0, ajv@^6.12.4, ajv@^6.12.5:
  version "6.12.6"
  resolved "https://registry.yarnpkg.com/ajv/-/ajv-6.12.6.tgz#baf5a62e802b07d977034586f8c3baf5adf26df4"
  integrity sha512-j3fVLgvTo527anyYyJOGTYJbG+vnnQYvE0m5mmkc1TK+nxAppkCLMIL0aZ4dblVCNoGShhm+kzE4ZUykBoMg4g==
  dependencies:
    fast-deep-equal "^3.1.1"
    fast-json-stable-stringify "^2.0.0"
    json-schema-traverse "^0.4.1"
    uri-js "^4.2.2"

ansi-regex@^2.0.0:
  version "2.1.1"
  resolved "https://registry.yarnpkg.com/ansi-regex/-/ansi-regex-2.1.1.tgz#c3b33ab5ee360d86e0e628f0468ae7ef27d654df"
  integrity sha512-TIGnTpdo+E3+pCyAluZvtED5p5wCqLdezCyhPZzKPcxvFplEt4i+W7OONCKgeZFT3+y5NZZfOOS/Bdcanm1MYA==

ansi-regex@^5.0.1:
  version "5.0.1"
  resolved "https://registry.yarnpkg.com/ansi-regex/-/ansi-regex-5.0.1.tgz#082cb2c89c9fe8659a311a53bd6a4dc5301db304"
  integrity sha512-quJQXlTSUGL2LH9SUXo8VwsY4soanhgo6LNSm84E1LBcE8s3O0wpdiRzyR9z/ZZJMlMWv37qOOb9pdJlMUEKFQ==

ansi-styles@^3.2.1:
  version "3.2.1"
  resolved "https://registry.yarnpkg.com/ansi-styles/-/ansi-styles-3.2.1.tgz#41fbb20243e50b12be0f04b8dedbf07520ce841d"
  integrity sha512-VT0ZI6kZRdTh8YyJw3SMbYm/u+NqfsAxEpWO0Pf9sq8/e94WxxOpPKx9FR1FlyCtOVDNOQ+8ntlqFxiRc+r5qA==
  dependencies:
    color-convert "^1.9.0"

ansi-styles@^4.0.0, ansi-styles@^4.1.0:
  version "4.3.0"
  resolved "https://registry.yarnpkg.com/ansi-styles/-/ansi-styles-4.3.0.tgz#edd803628ae71c04c85ae7a0906edad34b648937"
  integrity sha512-zbB9rCJAT1rbjiVDb2hqKFHNYLxgtk8NURxZ3IZwD3F6NtxbXZQCnnSi1Lkx+IDohdPlFp222wVALIheZJQSEg==
  dependencies:
    color-convert "^2.0.1"

anymatch@^3.0.3, anymatch@~3.1.2:
  version "3.1.3"
  resolved "https://registry.yarnpkg.com/anymatch/-/anymatch-3.1.3.tgz#790c58b19ba1720a84205b57c618d5ad8524973e"
  integrity sha512-KMReFUr0B4t+D+OBkjR3KYqvocp2XaSzO55UcB6mgQMd3KbcE+mWTyvVV7D/zsdEbNnV6acZUutkiHQXvTr1Rw==
  dependencies:
    normalize-path "^3.0.0"
    picomatch "^2.0.4"

aproba@^1.0.3:
  version "1.2.0"
  resolved "https://registry.yarnpkg.com/aproba/-/aproba-1.2.0.tgz#6802e6264efd18c790a1b0d517f0f2627bf2c94a"
  integrity sha512-Y9J6ZjXtoYh8RnXVCMOU/ttDmk1aBjunq9vO0ta5x85WDQiQfUF9sIPBITdbiiIVcBo03Hi3jMxigBtsddlXRw==

are-we-there-yet@~1.1.2:
  version "1.1.7"
  resolved "https://registry.yarnpkg.com/are-we-there-yet/-/are-we-there-yet-1.1.7.tgz#b15474a932adab4ff8a50d9adfa7e4e926f21146"
  integrity sha512-nxwy40TuMiUGqMyRHgCSWZ9FM4VAoRP4xUYSTv5ImRog+h9yISPbVH7H8fASCIzYn9wlEv4zvFL7uKDMCFQm3g==
  dependencies:
    delegates "^1.0.0"
    readable-stream "^2.0.6"

arg@^5.0.2:
  version "5.0.2"
  resolved "https://registry.yarnpkg.com/arg/-/arg-5.0.2.tgz#c81433cc427c92c4dcf4865142dbca6f15acd59c"
  integrity sha512-PYjyFOLKQ9y57JvQ6QLo8dAgNqswh8M1RMJYdQduT6xbWSgK36P/Z/v+p888pM69jMMfS8Xd8F6I1kQ/I9HUGg==

argparse@^1.0.7:
  version "1.0.10"
  resolved "https://registry.yarnpkg.com/argparse/-/argparse-1.0.10.tgz#bcd6791ea5ae09725e17e5ad988134cd40b3d911"
  integrity sha512-o5Roy6tNG4SL/FOkCAN6RzjiakZS25RLYFrcMttJqbdd8BWrnA+fGz57iN5Pb06pvBGvl5gQ0B48dJlslXvoTg==
  dependencies:
    sprintf-js "~1.0.2"

argparse@^2.0.1:
  version "2.0.1"
  resolved "https://registry.yarnpkg.com/argparse/-/argparse-2.0.1.tgz#246f50f3ca78a3240f6c997e8a9bd1eac49e4b38"
  integrity sha512-8+9WqebbFzpX9OR+Wa6O29asIogeRMzcGtAINdpMHHyAg10f05aSFVBbcEqGf/PXw1EjAZ+q2/bEBg3DvurK3Q==

aria-query@^4.2.2:
  version "4.2.2"
  resolved "https://registry.yarnpkg.com/aria-query/-/aria-query-4.2.2.tgz#0d2ca6c9aceb56b8977e9fed6aed7e15bbd2f83b"
  integrity sha512-o/HelwhuKpTj/frsOsbNLNgnNGVIFsVP/SW2BSF14gVl7kAfMOJ6/8wUAUvG1R1NHKrfG+2sHZTu0yauT1qBrA==
  dependencies:
    "@babel/runtime" "^7.10.2"
    "@babel/runtime-corejs3" "^7.10.2"

array-includes@^3.1.4, array-includes@^3.1.5, array-includes@^3.1.6:
  version "3.1.6"
  resolved "https://registry.yarnpkg.com/array-includes/-/array-includes-3.1.6.tgz#9e9e720e194f198266ba9e18c29e6a9b0e4b225f"
  integrity sha512-sgTbLvL6cNnw24FnbaDyjmvddQ2ML8arZsgaJhoABMoplz/4QRhtrYS+alr1BUM1Bwp6dhx8vVCBSLG+StwOFw==
  dependencies:
    call-bind "^1.0.2"
    define-properties "^1.1.4"
    es-abstract "^1.20.4"
    get-intrinsic "^1.1.3"
    is-string "^1.0.7"

array-union@^2.1.0:
  version "2.1.0"
  resolved "https://registry.yarnpkg.com/array-union/-/array-union-2.1.0.tgz#b798420adbeb1de828d84acd8a2e23d3efe85e8d"
  integrity sha512-HGyxoOTYUyCM6stUe6EJgnd4EoewAI7zMdfqO+kGjnlZmBDz/cR5pf8r/cR4Wq60sL/p0IkcjUEEPwS3GFrIyw==

array.prototype.flat@^1.2.5:
  version "1.3.1"
  resolved "https://registry.yarnpkg.com/array.prototype.flat/-/array.prototype.flat-1.3.1.tgz#ffc6576a7ca3efc2f46a143b9d1dda9b4b3cf5e2"
  integrity sha512-roTU0KWIOmJ4DRLmwKd19Otg0/mT3qPNt0Qb3GWW8iObuZXxrjB/pzn0R3hqpRSWg4HCwqx+0vwOnWnvlOyeIA==
  dependencies:
    call-bind "^1.0.2"
    define-properties "^1.1.4"
    es-abstract "^1.20.4"
    es-shim-unscopables "^1.0.0"

array.prototype.flatmap@^1.3.1:
  version "1.3.1"
  resolved "https://registry.yarnpkg.com/array.prototype.flatmap/-/array.prototype.flatmap-1.3.1.tgz#1aae7903c2100433cb8261cd4ed310aab5c4a183"
  integrity sha512-8UGn9O1FDVvMNB0UlLv4voxRMze7+FpHyF5mSMRjWHUMlpoDViniy05870VlxhfgTnLbpuwTzvD76MTtWxB/mQ==
  dependencies:
    call-bind "^1.0.2"
    define-properties "^1.1.4"
    es-abstract "^1.20.4"
    es-shim-unscopables "^1.0.0"

array.prototype.tosorted@^1.1.1:
  version "1.1.1"
  resolved "https://registry.yarnpkg.com/array.prototype.tosorted/-/array.prototype.tosorted-1.1.1.tgz#ccf44738aa2b5ac56578ffda97c03fd3e23dd532"
  integrity sha512-pZYPXPRl2PqWcsUs6LOMn+1f1532nEoPTYowBtqLwAW+W8vSVhkIGnmOX1t/UQjD6YGI0vcD2B1U7ZFGQH9jnQ==
  dependencies:
    call-bind "^1.0.2"
    define-properties "^1.1.4"
    es-abstract "^1.20.4"
    es-shim-unscopables "^1.0.0"
    get-intrinsic "^1.1.3"

ast-types-flow@^0.0.7:
  version "0.0.7"
  resolved "https://registry.yarnpkg.com/ast-types-flow/-/ast-types-flow-0.0.7.tgz#f70b735c6bca1a5c9c22d982c3e39e7feba3bdad"
  integrity sha512-eBvWn1lvIApYMhzQMsu9ciLfkBY499mFZlNqG+/9WR7PVlroQw0vG30cOQQbaKz3sCEc44TAOu2ykzqXSNnwag==

asynckit@^0.4.0:
  version "0.4.0"
  resolved "https://registry.yarnpkg.com/asynckit/-/asynckit-0.4.0.tgz#c79ed97f7f34cb8f2ba1bc9790bcc366474b4b79"
  integrity sha512-Oei9OH4tRh0YqU3GxhX79dM/mwVgvbZJaSNaRk+bshkj0S5cfHcgYakreBjrHwatXKbz+IoIdYLxrKim2MjW0Q==

autoprefixer@^10.4.13:
  version "10.4.13"
  resolved "https://registry.yarnpkg.com/autoprefixer/-/autoprefixer-10.4.13.tgz#b5136b59930209a321e9fa3dca2e7c4d223e83a8"
  integrity sha512-49vKpMqcZYsJjwotvt4+h/BCjJVnhGwcLpDt5xkcaOG3eLrG/HUYLagrihYsQ+qrIBgIzX1Rw7a6L8I/ZA1Atg==
  dependencies:
    browserslist "^4.21.4"
    caniuse-lite "^1.0.30001426"
    fraction.js "^4.2.0"
    normalize-range "^0.1.2"
    picocolors "^1.0.0"
    postcss-value-parser "^4.2.0"

axe-core@^4.4.3:
  version "4.6.1"
  resolved "https://registry.yarnpkg.com/axe-core/-/axe-core-4.6.1.tgz#79cccdee3e3ab61a8f42c458d4123a6768e6fbce"
  integrity sha512-lCZN5XRuOnpG4bpMq8v0khrWtUOn+i8lZSb6wHZH56ZfbIEv6XwJV84AAueh9/zi7qPVJ/E4yz6fmsiyOmXR4w==

axobject-query@^2.2.0:
  version "2.2.0"
  resolved "https://registry.yarnpkg.com/axobject-query/-/axobject-query-2.2.0.tgz#943d47e10c0b704aa42275e20edf3722648989be"
  integrity sha512-Td525n+iPOOyUQIeBfcASuG6uJsDOITl7Mds5gFyerkWiX7qhUTdYUBlSgNMyVqtSJqwpt1kXGLdUt6SykLMRA==

babel-plugin-polyfill-corejs2@^0.3.3:
  version "0.3.3"
  resolved "https://registry.yarnpkg.com/babel-plugin-polyfill-corejs2/-/babel-plugin-polyfill-corejs2-0.3.3.tgz#5d1bd3836d0a19e1b84bbf2d9640ccb6f951c122"
  integrity sha512-8hOdmFYFSZhqg2C/JgLUQ+t52o5nirNwaWM2B9LWteozwIvM14VSwdsCAUET10qT+kmySAlseadmfeeSWFCy+Q==
  dependencies:
    "@babel/compat-data" "^7.17.7"
    "@babel/helper-define-polyfill-provider" "^0.3.3"
    semver "^6.1.1"

babel-plugin-polyfill-corejs3@^0.6.0:
  version "0.6.0"
  resolved "https://registry.yarnpkg.com/babel-plugin-polyfill-corejs3/-/babel-plugin-polyfill-corejs3-0.6.0.tgz#56ad88237137eade485a71b52f72dbed57c6230a"
  integrity sha512-+eHqR6OPcBhJOGgsIar7xoAB1GcSwVUA3XjAd7HJNzOXT4wv6/H7KIdA/Nc60cvUlDbKApmqNvD1B1bzOt4nyA==
  dependencies:
    "@babel/helper-define-polyfill-provider" "^0.3.3"
    core-js-compat "^3.25.1"

babel-plugin-polyfill-regenerator@^0.4.1:
  version "0.4.1"
  resolved "https://registry.yarnpkg.com/babel-plugin-polyfill-regenerator/-/babel-plugin-polyfill-regenerator-0.4.1.tgz#390f91c38d90473592ed43351e801a9d3e0fd747"
  integrity sha512-NtQGmyQDXjQqQ+IzRkBVwEOz9lQ4zxAQZgoAYEtU9dJjnl1Oc98qnN7jcp+bE7O7aYzVpavXE3/VKXNzUbh7aw==
  dependencies:
    "@babel/helper-define-polyfill-provider" "^0.3.3"

backfill-cache@^5.6.1, backfill-cache@^5.6.3:
  version "5.6.3"
  resolved "https://registry.yarnpkg.com/backfill-cache/-/backfill-cache-5.6.3.tgz#4d5d883f9f833a1866a7c15389cd423c9b737e15"
  integrity sha512-wH3SJBKw2x5trhXUfL+lnr3cQAAyclsS9rMGM4f6XNPjec8xNqpZ0EOpJ+GULuXbozvxQBoynkfbAxWUAAvKpA==
  dependencies:
    "@azure/storage-blob" "12.1.2"
    "@rushstack/package-deps-hash" "^3.2.4"
    backfill-config "^6.3.1"
    backfill-logger "^5.1.3"
    execa "^5.0.0"
    find-up "^5.0.0"
    fs-extra "^8.1.0"
    globby "^11.0.0"
    p-limit "^3.0.0"
    tar-fs "^2.1.0"

backfill-config@^6.3.0, backfill-config@^6.3.1:
  version "6.3.1"
  resolved "https://registry.yarnpkg.com/backfill-config/-/backfill-config-6.3.1.tgz#7044e003dd9f5f71e277eef3d0184d213f8c4298"
  integrity sha512-k+NsMZyinQaKqb/yRUahp2+PwXcRU2SHpOkbXOAHIlqN2qZO78hUfjViBj8YoJ7gcweWY59dP4jdgo6q3nDoEg==
  dependencies:
    backfill-logger "^5.1.3"
    find-up "^5.0.0"
    fs-extra "^8.1.0"
    pkg-dir "^4.2.0"

backfill-hasher@^6.4.5:
  version "6.4.5"
  resolved "https://registry.yarnpkg.com/backfill-hasher/-/backfill-hasher-6.4.5.tgz#23c45263e6c4d20c344d22e944a7fc02ff2b61e8"
  integrity sha512-u0E2yWAqTUYhhxWurrPie84DJh7MZ/oyPewo7HqD6AkyqGez3CRQqH2jrqyBEpk/ELpWKbQbQ9lO68b1JDZLwA==
  dependencies:
    "@rushstack/package-deps-hash" "^3.2.4"
    backfill-config "^6.3.1"
    backfill-logger "^5.1.3"
    find-up "^5.0.0"
    fs-extra "^8.1.0"
    workspace-tools "^0.29.0"

backfill-logger@^5.1.3:
  version "5.1.3"
  resolved "https://registry.yarnpkg.com/backfill-logger/-/backfill-logger-5.1.3.tgz#29d4e9d205e2f44a95336db95652d6d2973e1fb8"
  integrity sha512-S1QUP+q3WWqcXWfwVt/jpi3r61CGWWJBfxGpzLPbRE8vMUw71P8sA+zYSx7M8ZI1PNZrxSA/TKq/NhoiMYXnpA==
  dependencies:
    chalk "^4.1.1"
    filenamify "^4.1.0"
    fs-extra "^8.1.0"

backfill-utils-dotenv@^5.1.1:
  version "5.1.1"
  resolved "https://registry.yarnpkg.com/backfill-utils-dotenv/-/backfill-utils-dotenv-5.1.1.tgz#eedf05badad4bd34fbac5d020f37f3ca634c9669"
  integrity sha512-hSdY1pflGFf4xXXpI51bnNPr8arS3ga5tSeyeTjIdohC5IwUf+Eldz2yeSMrbqtP3PKIuxHc2RcwTJfL5jSBfg==
  dependencies:
    dotenv "^8.1.0"
    find-up "^5.0.0"

backfill@^6.1.21:
  version "6.1.26"
  resolved "https://registry.yarnpkg.com/backfill/-/backfill-6.1.26.tgz#f1dd9e79c0817d400e7a12df5ea67a641ed7050d"
  integrity sha512-FPkLgXXZ8mna3q1PuJ4EVtWh27NhaW5RnM+6OQvkSBjutAOiVCVHRGDLU/Et6a692sedfWTsqrxGJuE1jK+eLA==
  dependencies:
    anymatch "^3.0.3"
    backfill-cache "^5.6.3"
    backfill-config "^6.3.1"
    backfill-hasher "^6.4.5"
    backfill-logger "^5.1.3"
    backfill-utils-dotenv "^5.1.1"
    chokidar "^3.2.1"
    execa "^5.0.0"
    find-up "^5.0.0"
    fs-extra "^8.1.0"
    globby "^11.0.0"
    yargs "^16.1.1"

bail@^2.0.0:
  version "2.0.2"
  resolved "https://registry.yarnpkg.com/bail/-/bail-2.0.2.tgz#d26f5cd8fe5d6f832a31517b9f7c356040ba6d5d"
  integrity sha512-0xO6mYd7JB2YesxDKplafRpsiOzPt9V02ddPCLbY1xYGPOX24NTyN50qnUxgCPcSoYMhKpAuBTjQoRZCAkUDRw==

balanced-match@^1.0.0:
  version "1.0.2"
  resolved "https://registry.yarnpkg.com/balanced-match/-/balanced-match-1.0.2.tgz#e83e3a7e3f300b34cb9d87f615fa0cbf357690ee"
  integrity sha512-3oSeUO0TMV67hN1AmbXsK4yaqU7tjiHlbxRDZOpH0KW9+CeX4bRAaX0Anxt0tx2MrpRpWwQaPwIlISEJhYU5Pw==

base64-js@^1.3.1:
  version "1.5.1"
  resolved "https://registry.yarnpkg.com/base64-js/-/base64-js-1.5.1.tgz#1b1b440160a5bf7ad40b650f095963481903930a"
  integrity sha512-AKpaYlHn8t4SVbOHCy+b5+KKgvR4vrsD8vbvrbiQJps7fKDTkjkDry6ji0rUJjC0kzbNePLwzxq8iypo41qeWA==

big.js@^5.2.2:
  version "5.2.2"
  resolved "https://registry.yarnpkg.com/big.js/-/big.js-5.2.2.tgz#65f0af382f578bcdc742bd9c281e9cb2d7768328"
  integrity sha512-vyL2OymJxmarO8gxMr0mhChsO9QGwhynfuu4+MHTAW6czfq9humCB7rKpUjDd9YUiDPU4mzpyupFSvOClAwbmQ==

binary-extensions@^2.0.0:
  version "2.2.0"
  resolved "https://registry.yarnpkg.com/binary-extensions/-/binary-extensions-2.2.0.tgz#75f502eeaf9ffde42fc98829645be4ea76bd9e2d"
  integrity sha512-jDctJ/IVQbZoJykoeHbhXpOlNBqGNcwXJKJog42E5HDPUwQTSdjCHdihjj0DlnheQ7blbT6dHOafNAiS8ooQKA==

bl@^4.0.3:
  version "4.1.0"
  resolved "https://registry.yarnpkg.com/bl/-/bl-4.1.0.tgz#451535264182bec2fbbc83a62ab98cf11d9f7b3a"
  integrity sha512-1W07cM9gS6DcLperZfFSj+bWLtaPGSOHWhPiGzXmvVJbRLdG82sH/Kn8EtW1VqWVA54AKf2h5k5BbnIbwF3h6w==
  dependencies:
    buffer "^5.5.0"
    inherits "^2.0.4"
    readable-stream "^3.4.0"

body-scroll-lock@^4.0.0-beta.0:
  version "4.0.0-beta.0"
  resolved "https://registry.yarnpkg.com/body-scroll-lock/-/body-scroll-lock-4.0.0-beta.0.tgz#4f78789d10e6388115c0460cd6d7d4dd2bbc4f7e"
  integrity sha512-a7tP5+0Mw3YlUJcGAKUqIBkYYGlYxk2fnCasq/FUph1hadxlTRjF+gAcZksxANnaMnALjxEddmSi/H3OR8ugcQ==

boolbase@^1.0.0:
  version "1.0.0"
  resolved "https://registry.yarnpkg.com/boolbase/-/boolbase-1.0.0.tgz#68dff5fbe60c51eb37725ea9e3ed310dcc1e776e"
  integrity sha512-JZOSA7Mo9sNGB8+UjSgzdLtokWAky1zbztM3WRLCbZ70/3cTANmQmOdR7y2g+J0e2WXywy1yS468tY+IruqEww==

brace-expansion@^1.1.7:
  version "1.1.11"
  resolved "https://registry.yarnpkg.com/brace-expansion/-/brace-expansion-1.1.11.tgz#3c7fcbf529d87226f3d2f52b966ff5271eb441dd"
  integrity sha512-iCuPHDFgrHX7H2vEI/5xpz07zSHB00TpugqhmYtVmMO6518mCuRMoOYFldEBl0g187ufozdaHgWKcYFb61qGiA==
  dependencies:
    balanced-match "^1.0.0"
    concat-map "0.0.1"

braces@^3.0.2, braces@~3.0.2:
  version "3.0.2"
  resolved "https://registry.yarnpkg.com/braces/-/braces-3.0.2.tgz#3454e1a462ee8d599e236df336cd9ea4f8afe107"
  integrity sha512-b8um+L1RzM3WDSzvhm6gIz1yfTbBt6YTlcEKAvsmqCZZFw46z626lVj9j1yEPW33H5H+lBQpZMP1k8l+78Ha0A==
  dependencies:
    fill-range "^7.0.1"

browserslist@^4.21.3, browserslist@^4.21.4:
  version "4.21.4"
  resolved "https://registry.yarnpkg.com/browserslist/-/browserslist-4.21.4.tgz#e7496bbc67b9e39dd0f98565feccdcb0d4ff6987"
  integrity sha512-CBHJJdDmgjl3daYjN5Cp5kbTf1mUhZoS+beLklHIvkOWscs83YAhLlF3Wsh/lciQYAcbBJgTOD44VtG31ZM4Hw==
  dependencies:
    caniuse-lite "^1.0.30001400"
    electron-to-chromium "^1.4.251"
    node-releases "^2.0.6"
    update-browserslist-db "^1.0.9"

buffer@^5.5.0:
  version "5.7.1"
  resolved "https://registry.yarnpkg.com/buffer/-/buffer-5.7.1.tgz#ba62e7c13133053582197160851a8f648e99eed0"
  integrity sha512-EHcyIPBQ4BSGlvjB16k5KgAJ27CIsHY/2JBmCRReo48y9rQ3MaUzWX3KVlBa4U7MyX02HdVj0K7C3WaB3ju7FQ==
  dependencies:
    base64-js "^1.3.1"
    ieee754 "^1.1.13"

call-bind@^1.0.0, call-bind@^1.0.2:
  version "1.0.2"
  resolved "https://registry.yarnpkg.com/call-bind/-/call-bind-1.0.2.tgz#b1d4e89e688119c3c9a903ad30abb2f6a919be3c"
  integrity sha512-7O+FbCihrB5WGbFYesctwmTKae6rOiIzmz1icreWJ+0aA7LJfuqhEso2T9ncpcFtzMQtzXf2QGGueWJGTYsqrA==
  dependencies:
    function-bind "^1.1.1"
    get-intrinsic "^1.0.2"

caller-callsite@^2.0.0:
  version "2.0.0"
  resolved "https://registry.yarnpkg.com/caller-callsite/-/caller-callsite-2.0.0.tgz#847e0fce0a223750a9a027c54b33731ad3154134"
  integrity sha512-JuG3qI4QOftFsZyOn1qq87fq5grLIyk1JYd5lJmdA+fG7aQ9pA/i3JIJGcO3q0MrRcHlOt1U+ZeHW8Dq9axALQ==
  dependencies:
    callsites "^2.0.0"

caller-path@^2.0.0:
  version "2.0.0"
  resolved "https://registry.yarnpkg.com/caller-path/-/caller-path-2.0.0.tgz#468f83044e369ab2010fac5f06ceee15bb2cb1f4"
  integrity sha512-MCL3sf6nCSXOwCTzvPKhN18TU7AHTvdtam8DAogxcrJ8Rjfbbg7Lgng64H9Iy+vUV6VGFClN/TyxBkAebLRR4A==
  dependencies:
    caller-callsite "^2.0.0"

callsites@^2.0.0:
  version "2.0.0"
  resolved "https://registry.yarnpkg.com/callsites/-/callsites-2.0.0.tgz#06eb84f00eea413da86affefacbffb36093b3c50"
  integrity sha512-ksWePWBloaWPxJYQ8TL0JHvtci6G5QTKwQ95RcWAa/lzoAKuAOflGdAK92hpHXjkwb8zLxoLNUoNYZgVsaJzvQ==

callsites@^3.0.0:
  version "3.1.0"
  resolved "https://registry.yarnpkg.com/callsites/-/callsites-3.1.0.tgz#b3630abd8943432f54b3f0519238e33cd7df2f73"
  integrity sha512-P8BjAsXvZS+VIDUI11hHCQEv74YT67YUi5JJFNWIqL235sBmjX4+qx9Muvls5ivyNENctx46xQLQ3aTuE7ssaQ==

camelcase-css@^2.0.1:
  version "2.0.1"
  resolved "https://registry.yarnpkg.com/camelcase-css/-/camelcase-css-2.0.1.tgz#ee978f6947914cc30c6b44741b6ed1df7f043fd5"
  integrity sha512-QOSvevhslijgYwRx6Rv7zKdMF8lbRmx+uQGx2+vDc+KI/eBnsy9kit5aj23AgGu3pa4t9AgwbnXWqS+iOY+2aA==

camelcase@^5.0.0:
  version "5.3.1"
  resolved "https://registry.yarnpkg.com/camelcase/-/camelcase-5.3.1.tgz#e3c9b31569e106811df242f715725a1f4c494320"
  integrity sha512-L28STB170nwWS63UjtlEOE3dldQApaJXZkOI1uMFfzf3rRuPegHaHesyee+YxQ+W6SvRDQV6UrdOdRiR153wJg==

camelcase@^6.2.0:
  version "6.3.0"
  resolved "https://registry.yarnpkg.com/camelcase/-/camelcase-6.3.0.tgz#5685b95eb209ac9c0c177467778c9c84df58ba9a"
  integrity sha512-Gmy6FhYlCY7uOElZUSbxo2UCDH8owEk996gkbrpsgGtrJLM3J7jGxl9Ic7Qwwj4ivOE5AWZWRMecDdF7hqGjFA==

caniuse-lite@^1.0.30001400, caniuse-lite@^1.0.30001406, caniuse-lite@^1.0.30001426:
  version "1.0.30001441"
  resolved "https://registry.yarnpkg.com/caniuse-lite/-/caniuse-lite-1.0.30001441.tgz#987437b266260b640a23cd18fbddb509d7f69f3e"
  integrity sha512-OyxRR4Vof59I3yGWXws6i908EtGbMzVUi3ganaZQHmydk1iwDhRnvaPG2WaR0KcqrDFKrxVZHULT396LEPhXfg==

ccount@^2.0.0:
  version "2.0.1"
  resolved "https://registry.yarnpkg.com/ccount/-/ccount-2.0.1.tgz#17a3bf82302e0870d6da43a01311a8bc02a3ecf5"
  integrity sha512-eyrF0jiFpY+3drT6383f1qhkbGsLSifNAjA61IUjZjmLCWjItY6LB9ft9YhoDgwfmclB2zhu51Lc7+95b8NRAg==

chalk@^2.0.0:
  version "2.4.2"
  resolved "https://registry.yarnpkg.com/chalk/-/chalk-2.4.2.tgz#cd42541677a54333cf541a49108c1432b44c9424"
  integrity sha512-Mti+f9lpJNcwF4tWV8/OrTTtF1gZi+f8FqlyAdouralcFWFQWF2+NgCHShjkCb+IFBLq9buZwE1xckQU4peSuQ==
  dependencies:
    ansi-styles "^3.2.1"
    escape-string-regexp "^1.0.5"
    supports-color "^5.3.0"

chalk@^4.0.0, chalk@^4.1.0, chalk@^4.1.1:
  version "4.1.2"
  resolved "https://registry.yarnpkg.com/chalk/-/chalk-4.1.2.tgz#aac4e2b7734a740867aeb16bf02aad556a1e7a01"
  integrity sha512-oKnbhFyRIXpUuez8iBMmyEa4nbj4IOQyuhc/wy9kY7/WVPcwIO9VA668Pu8RkO7+0G76SLROeyw9CpQ061i4mA==
  dependencies:
    ansi-styles "^4.1.0"
    supports-color "^7.1.0"

character-entities@^2.0.0:
  version "2.0.2"
  resolved "https://registry.yarnpkg.com/character-entities/-/character-entities-2.0.2.tgz#2d09c2e72cd9523076ccb21157dff66ad43fcc22"
  integrity sha512-shx7oQ0Awen/BRIdkjkvz54PnEEI/EjwXDSIZp86/KKdbafHh1Df/RYGBhn4hbe2+uKC9FnT5UCEdyPz3ai9hQ==

chokidar@^3.2.1, chokidar@^3.5.3:
  version "3.5.3"
  resolved "https://registry.yarnpkg.com/chokidar/-/chokidar-3.5.3.tgz#1cf37c8707b932bd1af1ae22c0432e2acd1903bd"
  integrity sha512-Dr3sfKRP6oTcjf2JmUmFJfeVMvXBdegxB0iVQ5eb2V10uFJUCAS8OByZdVAyVb8xXNz3GjjTgj9kLWsZTqE6kw==
  dependencies:
    anymatch "~3.1.2"
    braces "~3.0.2"
    glob-parent "~5.1.2"
    is-binary-path "~2.1.0"
    is-glob "~4.0.1"
    normalize-path "~3.0.0"
    readdirp "~3.6.0"
  optionalDependencies:
    fsevents "~2.3.2"

chownr@^1.1.1:
  version "1.1.4"
  resolved "https://registry.yarnpkg.com/chownr/-/chownr-1.1.4.tgz#6fc9d7b42d32a583596337666e7d08084da2cc6b"
  integrity sha512-jJ0bqzaylmJtVnNgzTeSOs8DPavpbYgEr/b0YL8/2GO3xJEhInFmhKMUnEJQjZumK7KXGFhUy89PrsJWlakBVg==

classnames@*, classnames@^2.3.2:
  version "2.3.2"
  resolved "https://registry.yarnpkg.com/classnames/-/classnames-2.3.2.tgz#351d813bf0137fcc6a76a16b88208d2560a0d924"
  integrity sha512-CSbhY4cFEJRe6/GQzIk5qXZ4Jeg5pcsP7b5peFSDpffpe1cqjASH/n9UTjBwOp6XpMSTwQ8Za2K5V02ueA7Tmw==

client-only@0.0.1:
  version "0.0.1"
  resolved "https://registry.yarnpkg.com/client-only/-/client-only-0.0.1.tgz#38bba5d403c41ab150bff64a95c85013cf73bca1"
  integrity sha512-IV3Ou0jSMzZrd3pZ48nLkT9DA7Ag1pnPzaiQhpW7c3RbcqqzvzzVu+L8gfqMp/8IM2MQtSiqaCxrrcfu8I8rMA==

cliui@^7.0.2:
  version "7.0.4"
  resolved "https://registry.yarnpkg.com/cliui/-/cliui-7.0.4.tgz#a0265ee655476fc807aea9df3df8df7783808b4f"
  integrity sha512-OcRE68cOsVMXp1Yvonl/fzkQOyjLSu/8bhPDfQt0e0/Eb283TKP20Fs2MqoPsr9SwA595rRCA+QMzYc9nBP+JQ==
  dependencies:
    string-width "^4.2.0"
    strip-ansi "^6.0.0"
    wrap-ansi "^7.0.0"

code-point-at@^1.0.0:
  version "1.1.0"
  resolved "https://registry.yarnpkg.com/code-point-at/-/code-point-at-1.1.0.tgz#0d070b4d043a5bea33a2f1a40e2edb3d9a4ccf77"
  integrity sha512-RpAVKQA5T63xEj6/giIbUEtZwJ4UFIc3ZtvEkiaUERylqe8xb5IvqcgOurZLahv93CLKfxcw5YI+DZcUBRyLXA==

color-convert@^1.9.0:
  version "1.9.3"
  resolved "https://registry.yarnpkg.com/color-convert/-/color-convert-1.9.3.tgz#bb71850690e1f136567de629d2d5471deda4c1e8"
  integrity sha512-QfAUtd+vFdAtFQcC8CCyYt1fYWxSqAiK2cSD6zDB8N3cpsEBAvRxp9zOGg6G/SHHJYAT88/az/IuDGALsNVbGg==
  dependencies:
    color-name "1.1.3"

color-convert@^2.0.1:
  version "2.0.1"
  resolved "https://registry.yarnpkg.com/color-convert/-/color-convert-2.0.1.tgz#72d3a68d598c9bdb3af2ad1e84f21d896abd4de3"
  integrity sha512-RRECPsj7iu/xb5oKYcsFHSppFNnsj/52OVTRKb4zP5onXwVF3zVmmToNcOfGC+CRDpfK/U584fMg38ZHCaElKQ==
  dependencies:
    color-name "~1.1.4"

color-name@1.1.3:
  version "1.1.3"
  resolved "https://registry.yarnpkg.com/color-name/-/color-name-1.1.3.tgz#a7d0558bd89c42f795dd42328f740831ca53bc25"
  integrity sha512-72fSenhMw2HZMTVHeCA9KCmpEIbzWiQsjN+BHcBbS9vr1mtt+vJjPdksIBNUmKAW8TFUDPJK5SUU3QhE9NEXDw==

color-name@^1.0.0, color-name@^1.1.4, color-name@~1.1.4:
  version "1.1.4"
  resolved "https://registry.yarnpkg.com/color-name/-/color-name-1.1.4.tgz#c2a09a87acbde69543de6f63fa3995c826c536a2"
  integrity sha512-dOy+3AuW3a2wNbZHIuMZpTcgjGuLU/uBL/ubcZF9OXbDo8ff4O8yVp5Bf0efS8uEoYo5q4Fx7dY9OgQGXgAsQA==

color-string@^1.9.1:
  version "1.9.1"
  resolved "https://registry.yarnpkg.com/color-string/-/color-string-1.9.1.tgz#4467f9146f036f855b764dfb5bf8582bf342c7a4"
  integrity sha512-shrVawQFojnZv6xM40anx4CkoDP+fZsw/ZerEMsW/pyzsRbElpsL/DBVW7q3ExxwusdNXI3lXpuhEZkzs8p5Eg==
  dependencies:
    color-name "^1.0.0"
    simple-swizzle "^0.2.2"

colors@~1.2.1:
  version "1.2.5"
  resolved "https://registry.yarnpkg.com/colors/-/colors-1.2.5.tgz#89c7ad9a374bc030df8013241f68136ed8835afc"
  integrity sha512-erNRLao/Y3Fv54qUa0LBB+//Uf3YwMUmdJinN20yMXm9zdKKqH9wt7R9IIVZ+K7ShzfpLV/Zg8+VyrBJYB4lpg==

combined-stream@^1.0.8:
  version "1.0.8"
  resolved "https://registry.yarnpkg.com/combined-stream/-/combined-stream-1.0.8.tgz#c3d45a8b34fd730631a110a8a2520682b31d5a7f"
  integrity sha512-FQN4MRfuJeHf7cBbBMJFXhKSDq+2kAArBlmRBvcvFE5BB1HZKXtSFASDhdlz9zOYwxh8lDdnvmMOe/+5cdoEdg==
  dependencies:
    delayed-stream "~1.0.0"

comma-separated-tokens@^2.0.0:
  version "2.0.3"
  resolved "https://registry.yarnpkg.com/comma-separated-tokens/-/comma-separated-tokens-2.0.3.tgz#4e89c9458acb61bc8fef19f4529973b2392839ee"
  integrity sha512-Fu4hJdvzeylCfQPp9SGWidpzrMs7tTrlu6Vb8XGaRGck8QSNZJJp538Wrb60Lax4fPwR64ViY468OIUTbRlGZg==

commander@9.2.0:
  version "9.2.0"
  resolved "https://registry.yarnpkg.com/commander/-/commander-9.2.0.tgz#6e21014b2ed90d8b7c9647230d8b7a94a4a419a9"
  integrity sha512-e2i4wANQiSXgnrBlIatyHtP1odfUp0BbV5Y5nEGbxtIrStkEOAAzCUirvLBNXHLr7kwLvJl6V+4V3XV9x7Wd9w==

commander@^2.20.3:
  version "2.20.3"
  resolved "https://registry.yarnpkg.com/commander/-/commander-2.20.3.tgz#fd485e84c03eb4881c20722ba48035e8531aeb33"
  integrity sha512-GpVkmM8vF2vQUkj2LvZmD35JxeJOLCwJ9cUkugyk2nuhbv3+mJvpLYYt+0+USMxE+oj+ey/lJEnhZw75x/OMcQ==

commander@^7.2.0:
  version "7.2.0"
  resolved "https://registry.yarnpkg.com/commander/-/commander-7.2.0.tgz#a36cb57d0b501ce108e4d20559a150a391d97ab7"
  integrity sha512-QrWXB+ZQSVPmIWIhtEO9H+gwHaMGYiF5ChvoJ+K9ZGHG/sVsa6yiesAD1GC/x46sET00Xlwo1u49RVVVzvcSkw==

commander@^8.0.0:
  version "8.3.0"
  resolved "https://registry.yarnpkg.com/commander/-/commander-8.3.0.tgz#4837ea1b2da67b9c616a67afbb0fafee567bca66"
  integrity sha512-OkTL9umf+He2DZkUq8f8J9of7yL6RJKI24dVITBmNfZBmri9zYZQrKkuXiKhyfPSu8tUhnVBB1iKXevvnlR4Ww==

commander@^9.4.1:
  version "9.4.1"
  resolved "https://registry.yarnpkg.com/commander/-/commander-9.4.1.tgz#d1dd8f2ce6faf93147295c0df13c7c21141cfbdd"
  integrity sha512-5EEkTNyHNGFPD2H+c/dXXfQZYa/scCKasxWcXJaWnNJ99pnQN9Vnmqow+p+PlFPE63Q6mThaZws1T+HxfpgtPw==

concat-map@0.0.1:
  version "0.0.1"
  resolved "https://registry.yarnpkg.com/concat-map/-/concat-map-0.0.1.tgz#d8a96bd77fd68df7793a73036a3ba0d5405d477b"
  integrity sha512-/Srv4dswyQNBfohGpz9o6Yb3Gz3SrUDqBH5rTuhGR7ahtlbYKnVxw2bCFMRljaA7EXHaXZ8wsHdodFvbkhKmqg==

console-control-strings@^1.0.0, console-control-strings@~1.1.0:
  version "1.1.0"
  resolved "https://registry.yarnpkg.com/console-control-strings/-/console-control-strings-1.1.0.tgz#3d7cf4464db6446ea644bf4b39507f9851008e8e"
  integrity sha512-ty/fTekppD2fIwRvnZAVdeOiGd1c7YXEixbgJTNzqcxJWKQnjJ/V1bNEEE6hygpM3WjwHFUVK6HTjWSzV4a8sQ==

convert-source-map@^1.7.0:
  version "1.9.0"
  resolved "https://registry.yarnpkg.com/convert-source-map/-/convert-source-map-1.9.0.tgz#7faae62353fb4213366d0ca98358d22e8368b05f"
  integrity sha512-ASFBup0Mz1uyiIjANan1jzLQami9z1PoYSZCiiYW2FczPbenXc45FZdBZLzOT+r6+iciuEModtmCti+hjaAk0A==

core-js-compat@^3.25.1:
  version "3.27.1"
  resolved "https://registry.yarnpkg.com/core-js-compat/-/core-js-compat-3.27.1.tgz#b5695eb25c602d72b1d30cbfba3cb7e5e4cf0a67"
  integrity sha512-Dg91JFeCDA17FKnneN7oCMz4BkQ4TcffkgHP4OWwp9yx3pi7ubqMDXXSacfNak1PQqjc95skyt+YBLHQJnkJwA==
  dependencies:
    browserslist "^4.21.4"

core-js-pure@^3.25.1:
  version "3.27.1"
  resolved "https://registry.yarnpkg.com/core-js-pure/-/core-js-pure-3.27.1.tgz#ede4a6b8440585c7190062757069c01d37a19dca"
  integrity sha512-BS2NHgwwUppfeoqOXqi08mUqS5FiZpuRuJJpKsaME7kJz0xxuk0xkhDdfMIlP/zLa80krBqss1LtD7f889heAw==

core-util-is@~1.0.0:
  version "1.0.3"
  resolved "https://registry.yarnpkg.com/core-util-is/-/core-util-is-1.0.3.tgz#a6042d3634c2b27e9328f837b965fac83808db85"
  integrity sha512-ZQBvi1DcpJ4GDqanjucZ2Hj3wEO5pZDS89BWbkcrvdxksJorwUDDZamX9ldFkp9aw2lmBDLgkObEA4DWNJ9FYQ==

cosmiconfig@^5.0.0:
  version "5.2.1"
  resolved "https://registry.yarnpkg.com/cosmiconfig/-/cosmiconfig-5.2.1.tgz#040f726809c591e77a17c0a3626ca45b4f168b1a"
  integrity sha512-H65gsXo1SKjf8zmrJ67eJk8aIRKV5ff2D4uKZIBZShbhGSpEmsQOPW/SKMKYhSTrqR7ufy6RP69rPogdaPh/kA==
  dependencies:
    import-fresh "^2.0.0"
    is-directory "^0.3.1"
    js-yaml "^3.13.1"
    parse-json "^4.0.0"

cosmiconfig@^7.0.0, cosmiconfig@^7.0.1:
  version "7.1.0"
  resolved "https://registry.yarnpkg.com/cosmiconfig/-/cosmiconfig-7.1.0.tgz#1443b9afa596b670082ea46cbd8f6a62b84635f6"
  integrity sha512-AdmX6xUzdNASswsFtmwSt7Vj8po9IuqXm0UXz7QKPuEUmPB4XyjGfaAr2PSuELMwkRMVH1EpIkX5bTZGRB3eCA==
  dependencies:
    "@types/parse-json" "^4.0.0"
    import-fresh "^3.2.1"
    parse-json "^5.0.0"
    path-type "^4.0.0"
    yaml "^1.10.0"

cross-spawn@^7.0.2, cross-spawn@^7.0.3:
  version "7.0.3"
  resolved "https://registry.yarnpkg.com/cross-spawn/-/cross-spawn-7.0.3.tgz#f73a85b9d5d41d045551c177e2882d4ac85728a6"
  integrity sha512-iRDPJKUPVEND7dHPO8rkbOnPpyDygcDFtWjpeWNCgy8WP2rXcxXL8TskReQl6OrB2G7+UJrags1q15Fudc7G6w==
  dependencies:
    path-key "^3.1.0"
    shebang-command "^2.0.0"
    which "^2.0.1"

css-blank-pseudo@^3.0.3:
  version "3.0.3"
  resolved "https://registry.yarnpkg.com/css-blank-pseudo/-/css-blank-pseudo-3.0.3.tgz#36523b01c12a25d812df343a32c322d2a2324561"
  integrity sha512-VS90XWtsHGqoM0t4KpH053c4ehxZ2E6HtGI7x68YFV0pTo/QmkV/YFA+NnlvK8guxZVNWGQhVNJGC39Q8XF4OQ==
  dependencies:
    postcss-selector-parser "^6.0.9"

css-has-pseudo@^3.0.4:
  version "3.0.4"
  resolved "https://registry.yarnpkg.com/css-has-pseudo/-/css-has-pseudo-3.0.4.tgz#57f6be91ca242d5c9020ee3e51bbb5b89fc7af73"
  integrity sha512-Vse0xpR1K9MNlp2j5w1pgWIJtm1a8qS0JwS9goFYcImjlHEmywP9VUF05aGBXzGpDJF86QXk4L0ypBmwPhGArw==
  dependencies:
    postcss-selector-parser "^6.0.9"

css-prefers-color-scheme@^6.0.3:
  version "6.0.3"
  resolved "https://registry.yarnpkg.com/css-prefers-color-scheme/-/css-prefers-color-scheme-6.0.3.tgz#ca8a22e5992c10a5b9d315155e7caee625903349"
  integrity sha512-4BqMbZksRkJQx2zAjrokiGMd07RqOa2IxIrrN10lyBe9xhn9DEvjUK79J6jkeiv9D9hQFXKb6g1jwU62jziJZA==

css-select@^4.1.3:
  version "4.3.0"
  resolved "https://registry.yarnpkg.com/css-select/-/css-select-4.3.0.tgz#db7129b2846662fd8628cfc496abb2b59e41529b"
  integrity sha512-wPpOYtnsVontu2mODhA19JrqWxNsfdatRKd64kmpRbQgh1KtItko5sTnEpPdpSaJszTOhEMlF/RPz28qj4HqhQ==
  dependencies:
    boolbase "^1.0.0"
    css-what "^6.0.1"
    domhandler "^4.3.1"
    domutils "^2.8.0"
    nth-check "^2.0.1"

css-tree@^1.1.2, css-tree@^1.1.3:
  version "1.1.3"
  resolved "https://registry.yarnpkg.com/css-tree/-/css-tree-1.1.3.tgz#eb4870fb6fd7707327ec95c2ff2ab09b5e8db91d"
  integrity sha512-tRpdppF7TRazZrjJ6v3stzv93qxRcSsFmW6cX0Zm2NVKpxE1WV1HblnghVv9TreireHkqI/VDEsfolRF1p6y7Q==
  dependencies:
    mdn-data "2.0.14"
    source-map "^0.6.1"

css-what@^6.0.1:
  version "6.1.0"
  resolved "https://registry.yarnpkg.com/css-what/-/css-what-6.1.0.tgz#fb5effcf76f1ddea2c81bdfaa4de44e79bac70f4"
  integrity sha512-HTUrgRJ7r4dsZKU6GjmpfRK1O76h97Z8MfS1G0FozR+oF2kG6Vfe8JE6zwrkbxigziPHinCJ+gCPjA9EaBDtRw==

cssdb@^7.1.0:
  version "7.2.0"
  resolved "https://registry.yarnpkg.com/cssdb/-/cssdb-7.2.0.tgz#f44bd4abc430f0ff7f4c64b8a1fb857a753f77a8"
  integrity sha512-JYlIsE7eKHSi0UNuCyo96YuIDFqvhGgHw4Ck6lsN+DP0Tp8M64UTDT2trGbkMDqnCoEjks7CkS0XcjU0rkvBdg==

cssesc@^3.0.0:
  version "3.0.0"
  resolved "https://registry.yarnpkg.com/cssesc/-/cssesc-3.0.0.tgz#37741919903b868565e1c09ea747445cd18983ee"
  integrity sha512-/Tb/JcjK111nNScGob5MNtsntNM1aCNUDipB/TkwZFhyDrrE47SOx/18wF2bbjgc3ZzCSKW1T5nt5EbFoAz/Vg==

cssfilter@0.0.10:
  version "0.0.10"
  resolved "https://registry.yarnpkg.com/cssfilter/-/cssfilter-0.0.10.tgz#c6d2672632a2e5c83e013e6864a42ce8defd20ae"
  integrity sha512-FAaLDaplstoRsDR8XGYH51znUN0UY7nMc6Z9/fvE8EXGwvJE9hu7W2vHwx1+bd6gCYnln9nLbzxFTrcO9YQDZw==

csso@^4.2.0:
  version "4.2.0"
  resolved "https://registry.yarnpkg.com/csso/-/csso-4.2.0.tgz#ea3a561346e8dc9f546d6febedd50187cf389529"
  integrity sha512-wvlcdIbf6pwKEk7vHj8/Bkc0B4ylXZruLvOgs9doS5eOsOpuodOV2zJChSpkp+pRpYQLQMeF04nr3Z68Sta9jA==
  dependencies:
    css-tree "^1.1.2"

csstype@^3.0.2:
  version "3.1.1"
  resolved "https://registry.yarnpkg.com/csstype/-/csstype-3.1.1.tgz#841b532c45c758ee546a11d5bd7b7b473c8c30b9"
  integrity sha512-DJR/VvkAvSZW9bTouZue2sSxDwdTN92uHjqeKVm+0dAqdfNykRzQ95tay8aXMBAAPpUiq4Qcug2L7neoRh2Egw==

cuint@^0.2.2:
  version "0.2.2"
  resolved "https://registry.yarnpkg.com/cuint/-/cuint-0.2.2.tgz#408086d409550c2631155619e9fa7bcadc3b991b"
  integrity sha512-d4ZVpCW31eWwCMe1YT3ur7mUDnTXbgwyzaL320DrcRT45rfjYxkt5QWLrmOJ+/UEAI2+fQgKe/fCjR8l4TpRgw==

damerau-levenshtein@^1.0.8:
  version "1.0.8"
  resolved "https://registry.yarnpkg.com/damerau-levenshtein/-/damerau-levenshtein-1.0.8.tgz#b43d286ccbd36bc5b2f7ed41caf2d0aba1f8a6e7"
  integrity sha512-sdQSFB7+llfUcQHUQO3+B8ERRj0Oa4w9POWMI/puGtuf7gFywGmkaLCElnudfTiKZV+NvHqL0ifzdrI8Ro7ESA==

data-uri-to-buffer@^4.0.0:
  version "4.0.0"
  resolved "https://registry.yarnpkg.com/data-uri-to-buffer/-/data-uri-to-buffer-4.0.0.tgz#b5db46aea50f6176428ac05b73be39a57701a64b"
  integrity sha512-Vr3mLBA8qWmcuschSLAOogKgQ/Jwxulv3RNE4FXnYWRGujzrRWQI4m12fQqRkwX06C0KanhLr4hK+GydchZsaA==

debug@^2.6.9:
  version "2.6.9"
  resolved "https://registry.yarnpkg.com/debug/-/debug-2.6.9.tgz#5d128515df134ff327e90a4c93f4e077a536341f"
  integrity sha512-bC7ElrdJaJnPbAP+1EotYvqZsb3ecl5wi6Bfi6BJTUcNowp6cvspg0jXznRTKDjm/E7AdgFBVeAPVMNcKGsHMA==
  dependencies:
    ms "2.0.0"

debug@^3.2.7:
  version "3.2.7"
  resolved "https://registry.yarnpkg.com/debug/-/debug-3.2.7.tgz#72580b7e9145fb39b6676f9c5e5fb100b934179a"
  integrity sha512-CFjzYYAi4ThfiQvizrFQevTTXHtnCqWfe7x1AhgEscTz6ZbLbfoLRLPugTQyBth6f8ZERVUSyWHFD/7Wu4t1XQ==
  dependencies:
    ms "^2.1.1"

debug@^4.0.0, debug@^4.1.0, debug@^4.1.1, debug@^4.3.2, debug@^4.3.4:
  version "4.3.4"
  resolved "https://registry.yarnpkg.com/debug/-/debug-4.3.4.tgz#1319f6579357f2338d3337d2cdd4914bb5dcc865"
  integrity sha512-PRWFHuSU3eDtQJPvnNY7Jcket1j0t5OuOsFzPPzsekD52Zl8qUfFIPEiswXqIvHWGVHOgX+7G/vCNNhehwxfkQ==
  dependencies:
    ms "2.1.2"

decamelize@^1.2.0:
  version "1.2.0"
  resolved "https://registry.yarnpkg.com/decamelize/-/decamelize-1.2.0.tgz#f6534d15148269b20352e7bee26f501f9a191290"
  integrity sha512-z2S+W9X73hAUUki+N+9Za2lBlun89zigOyGrsax+KUQ6wKW4ZoWpEYBkGhQjwAjjDCkWxhY0VKEhk8wzY7F5cA==

decode-named-character-reference@^1.0.0:
  version "1.0.2"
  resolved "https://registry.yarnpkg.com/decode-named-character-reference/-/decode-named-character-reference-1.0.2.tgz#daabac9690874c394c81e4162a0304b35d824f0e"
  integrity sha512-O8x12RzrUF8xyVcY0KJowWsmaJxQbmy0/EtnNtHRpsOcT7dFk5W598coHqBVpmWo1oQQfsCqfCmkZN5DJrZVdg==
  dependencies:
    character-entities "^2.0.0"

deep-is@^0.1.3:
  version "0.1.4"
  resolved "https://registry.yarnpkg.com/deep-is/-/deep-is-0.1.4.tgz#a6f2dce612fadd2ef1f519b73551f17e85199831"
  integrity sha512-oIPzksmTg4/MriiaYGO+okXDT7ztn/w3Eptv/+gSIdMdKsJo0u4CfYNFJPy+4SKMuCqGw2wxnA+URMg3t8a/bQ==

deepmerge@^4.2.2:
  version "4.2.2"
  resolved "https://registry.yarnpkg.com/deepmerge/-/deepmerge-4.2.2.tgz#44d2ea3679b8f4d4ffba33f03d865fc1e7bf4955"
  integrity sha512-FJ3UgI4gIl+PHZm53knsuSFpE+nESMr7M4v9QcgB7S63Kj/6WqMiFQJpBBYz1Pt+66bZpP3Q7Lye0Oo9MPKEdg==

define-lazy-prop@^2.0.0:
  version "2.0.0"
  resolved "https://registry.yarnpkg.com/define-lazy-prop/-/define-lazy-prop-2.0.0.tgz#3f7ae421129bcaaac9bc74905c98a0009ec9ee7f"
  integrity sha512-Ds09qNh8yw3khSjiJjiUInaGX9xlqZDY7JVryGxdxV7NPeuqQfplOpQ66yJFZut3jLa5zOwkXw1g9EI2uKh4Og==

define-properties@^1.1.3, define-properties@^1.1.4:
  version "1.1.4"
  resolved "https://registry.yarnpkg.com/define-properties/-/define-properties-1.1.4.tgz#0b14d7bd7fbeb2f3572c3a7eda80ea5d57fb05b1"
  integrity sha512-uckOqKcfaVvtBdsVkdPv3XjveQJsNQqmhXgRi8uhvWWuPYZCNlzT8qAyblUgNoXdHdjMTzAqeGjAoli8f+bzPA==
  dependencies:
    has-property-descriptors "^1.0.0"
    object-keys "^1.1.1"

defined@^1.0.0:
  version "1.0.1"
  resolved "https://registry.yarnpkg.com/defined/-/defined-1.0.1.tgz#c0b9db27bfaffd95d6f61399419b893df0f91ebf"
  integrity sha512-hsBd2qSVCRE+5PmNdHt1uzyrFu5d3RwmFDKzyNZMFq/EwDNJF7Ee5+D5oEKF0hU6LhtoUF1macFvOe4AskQC1Q==

delayed-stream@~1.0.0:
  version "1.0.0"
  resolved "https://registry.yarnpkg.com/delayed-stream/-/delayed-stream-1.0.0.tgz#df3ae199acadfb7d440aaae0b29e2272b24ec619"
  integrity sha512-ZySD7Nf91aLB0RxL4KGrKHBXl7Eds1DAmEdcoVawXnLD7SDhpNgtuII2aAkg7a7QS41jxPSZ17p4VdGnMHk3MQ==

delegates@^1.0.0:
  version "1.0.0"
  resolved "https://registry.yarnpkg.com/delegates/-/delegates-1.0.0.tgz#84c6e159b81904fdca59a0ef44cd870d31250f9a"
  integrity sha512-bd2L678uiWATM6m5Z1VzNCErI3jiGzt6HGY8OVICs40JQq/HALfbyNJmp0UDakEY4pMMaN0Ly5om/B1VI/+xfQ==

dequal@^2.0.0:
  version "2.0.3"
  resolved "https://registry.yarnpkg.com/dequal/-/dequal-2.0.3.tgz#2644214f1997d39ed0ee0ece72335490a7ac67be"
  integrity sha512-0je+qPKHEMohvfRTCEo3CrPG6cAzAYgmzKyxRiYSSDkS6eGJdyVJm7WaYA5ECaAD9wLB2T4EEeymA5aFVcYXCA==

detective@^5.2.1:
  version "5.2.1"
  resolved "https://registry.yarnpkg.com/detective/-/detective-5.2.1.tgz#6af01eeda11015acb0e73f933242b70f24f91034"
  integrity sha512-v9XE1zRnz1wRtgurGu0Bs8uHKFSTdteYZNbIPFVhUZ39L/S79ppMpdmVOZAnoz1jfEFodc48n6MX483Xo3t1yw==
  dependencies:
    acorn-node "^1.8.2"
    defined "^1.0.0"
    minimist "^1.2.6"

didyoumean@^1.2.2:
  version "1.2.2"
  resolved "https://registry.yarnpkg.com/didyoumean/-/didyoumean-1.2.2.tgz#989346ffe9e839b4555ecf5666edea0d3e8ad037"
  integrity sha512-gxtyfqMg7GKyhQmb056K7M3xszy/myH8w+B4RT+QXBQsvAOdc3XymqDDPHx1BgPgsdAA5SIifona89YtRATDzw==

diff@^5.0.0:
  version "5.1.0"
  resolved "https://registry.yarnpkg.com/diff/-/diff-5.1.0.tgz#bc52d298c5ea8df9194800224445ed43ffc87e40"
  integrity sha512-D+mk+qE8VC/PAUrlAU34N+VfXev0ghe5ywmpqrawphmVZc1bEfn56uo9qpyGp1p4xpzOHkSW4ztBd6L7Xx4ACw==

dir-glob@^3.0.1:
  version "3.0.1"
  resolved "https://registry.yarnpkg.com/dir-glob/-/dir-glob-3.0.1.tgz#56dbf73d992a4a93ba1584f4534063fd2e41717f"
  integrity sha512-WkrWp9GR4KXfKGYzOLmTuGVi1UWFfws377n9cc55/tb6DuqyF6pcQ5AbiHEshaDpY9v6oaSr2XCDidGmMwdzIA==
  dependencies:
    path-type "^4.0.0"

dlv@^1.1.3:
  version "1.1.3"
  resolved "https://registry.yarnpkg.com/dlv/-/dlv-1.1.3.tgz#5c198a8a11453596e751494d49874bc7732f2e79"
  integrity sha512-+HlytyjlPKnIG8XuRG8WvmBP8xs8P71y+SKKS6ZXWoEgLuePxtDoUEiH7WkdePWrQ5JBpE6aoVqfZfJUQkjXwA==

doctrine@^2.1.0:
  version "2.1.0"
  resolved "https://registry.yarnpkg.com/doctrine/-/doctrine-2.1.0.tgz#5cd01fc101621b42c4cd7f5d1a66243716d3f39d"
  integrity sha512-35mSku4ZXK0vfCuHEDAwt55dg2jNajHZ1odvF+8SSr82EsZY4QmXfuWso8oEd8zRhVObSN18aM0CjSdoBX7zIw==
  dependencies:
    esutils "^2.0.2"

doctrine@^3.0.0:
  version "3.0.0"
  resolved "https://registry.yarnpkg.com/doctrine/-/doctrine-3.0.0.tgz#addebead72a6574db783639dc87a121773973961"
  integrity sha512-yS+Q5i3hBf7GBkd4KG8a7eBNNWNGLTaEwwYWUijIYM7zrlYDM0BFXHjjPWlWZ1Rg7UaddZeIDmi9jF3HmqiQ2w==
  dependencies:
    esutils "^2.0.2"

dom-serializer@^1.0.1:
  version "1.4.1"
  resolved "https://registry.yarnpkg.com/dom-serializer/-/dom-serializer-1.4.1.tgz#de5d41b1aea290215dc45a6dae8adcf1d32e2d30"
  integrity sha512-VHwB3KfrcOOkelEG2ZOfxqLZdfkil8PtJi4P8N2MMXucZq2yLp75ClViUlOVwyoHEDjYU433Aq+5zWP61+RGag==
  dependencies:
    domelementtype "^2.0.1"
    domhandler "^4.2.0"
    entities "^2.0.0"

dom7@^4.0.4:
  version "4.0.4"
  resolved "https://registry.yarnpkg.com/dom7/-/dom7-4.0.4.tgz#8b68c5d8e5e2ed0fddb1cb93e433bc9060c8f3fb"
  integrity sha512-DSSgBzQ4rJWQp1u6o+3FVwMNnT5bzQbMb+o31TjYYeRi05uAcpF8koxdfzeoe5ElzPmua7W7N28YJhF7iEKqIw==
  dependencies:
    ssr-window "^4.0.0"

domelementtype@^2.0.1, domelementtype@^2.2.0:
  version "2.3.0"
  resolved "https://registry.yarnpkg.com/domelementtype/-/domelementtype-2.3.0.tgz#5c45e8e869952626331d7aab326d01daf65d589d"
  integrity sha512-OLETBj6w0OsagBwdXnPdN0cnMfF9opN69co+7ZrbfPGrdpPVNBUj02spi6B1N7wChLQiPn4CSH/zJvXw56gmHw==

domhandler@^4.2.0, domhandler@^4.3.1:
  version "4.3.1"
  resolved "https://registry.yarnpkg.com/domhandler/-/domhandler-4.3.1.tgz#8d792033416f59d68bc03a5aa7b018c1ca89279c"
  integrity sha512-GrwoxYN+uWlzO8uhUXRl0P+kHE4GtVPfYzVLcUxPL7KNdHKj66vvlhiweIHqYYXWlw+T8iLMp42Lm67ghw4WMQ==
  dependencies:
    domelementtype "^2.2.0"

domutils@^2.8.0:
  version "2.8.0"
  resolved "https://registry.yarnpkg.com/domutils/-/domutils-2.8.0.tgz#4437def5db6e2d1f5d6ee859bd95ca7d02048135"
  integrity sha512-w96Cjofp72M5IIhpjgobBimYEfoPjx1Vx0BSX9P30WBdZW2WIKU0T1Bd0kz2eNZ9ikjKgHbEyKx8BB6H1L3h3A==
  dependencies:
    dom-serializer "^1.0.1"
    domelementtype "^2.2.0"
    domhandler "^4.2.0"

dot-prop@^7.2.0:
  version "7.2.0"
  resolved "https://registry.yarnpkg.com/dot-prop/-/dot-prop-7.2.0.tgz#468172a3529779814d21a779c1ba2f6d76609809"
  integrity sha512-Ol/IPXUARn9CSbkrdV4VJo7uCy1I3VuSiWCaFSg+8BdUOzF9n3jefIpcgAydvUZbTdEBZs2vEiTiS9m61ssiDA==
  dependencies:
    type-fest "^2.11.2"

dotenv@^8.1.0:
  version "8.6.0"
  resolved "https://registry.yarnpkg.com/dotenv/-/dotenv-8.6.0.tgz#061af664d19f7f4d8fc6e4ff9b584ce237adcb8b"
  integrity sha512-IrPdXQsk2BbzvCBGBOTmmSH5SodmqZNt4ERAZDmW4CT+tL8VtvinqywuANaFu4bOMWki16nqf0e4oC0QIaDr/g==

duplexer@^0.1.2:
  version "0.1.2"
  resolved "https://registry.yarnpkg.com/duplexer/-/duplexer-0.1.2.tgz#3abe43aef3835f8ae077d136ddce0f276b0400e6"
  integrity sha512-jtD6YG370ZCIi/9GTaJKQxWTZD045+4R4hTk/x1UyoqadyJ9x9CgSi1RlVDQF8U2sxLLSnFkCaMihqljHIWgMg==

electron-to-chromium@^1.4.251:
  version "1.4.284"
  resolved "https://registry.yarnpkg.com/electron-to-chromium/-/electron-to-chromium-1.4.284.tgz#61046d1e4cab3a25238f6bf7413795270f125592"
  integrity sha512-M8WEXFuKXMYMVr45fo8mq0wUrrJHheiKZf6BArTKk9ZBYCKJEOU5H8cdWgDT+qCVZf7Na4lVUaZsA+h6uA9+PA==

emoji-regex@^8.0.0:
  version "8.0.0"
  resolved "https://registry.yarnpkg.com/emoji-regex/-/emoji-regex-8.0.0.tgz#e818fd69ce5ccfcb404594f842963bf53164cc37"
  integrity sha512-MSjYzcWNOA0ewAHpz0MxpYFvwg6yjy1NG3xteoqz644VCo/RPgnr1/GGt+ic3iJTzQ8Eu3TdM14SawnVUmGE6A==

emoji-regex@^9.2.2:
  version "9.2.2"
  resolved "https://registry.yarnpkg.com/emoji-regex/-/emoji-regex-9.2.2.tgz#840c8803b0d8047f4ff0cf963176b32d4ef3ed72"
  integrity sha512-L18DaJsXSUk2+42pv8mLs5jJT2hqFkFE4j21wOmgbUqsZ2hL72NsUU785g9RXgo3s0ZNgVl42TiHp3ZtOv/Vyg==

emojis-list@^3.0.0:
  version "3.0.0"
  resolved "https://registry.yarnpkg.com/emojis-list/-/emojis-list-3.0.0.tgz#5570662046ad29e2e916e71aae260abdff4f6a78"
  integrity sha512-/kyM18EfinwXZbno9FyUGeFh87KC8HRQBQGildHZbEuRyWFOmv1U10o9BBp8XVZDVNNuQKyIGIu5ZYAAXJ0V2Q==

end-of-stream@^1.1.0, end-of-stream@^1.4.1:
  version "1.4.4"
  resolved "https://registry.yarnpkg.com/end-of-stream/-/end-of-stream-1.4.4.tgz#5ae64a5f45057baf3626ec14da0ca5e4b2431eb0"
  integrity sha512-+uw1inIHVPQoaVuHzRyXd21icM+cnt4CzD5rW+NC1wjOUSTOs+Te7FOv7AhN7vS9x/oIyhLP5PR1H+phQAHu5Q==
  dependencies:
    once "^1.4.0"

enhanced-resolve@^5.10.0:
  version "5.12.0"
  resolved "https://registry.yarnpkg.com/enhanced-resolve/-/enhanced-resolve-5.12.0.tgz#300e1c90228f5b570c4d35babf263f6da7155634"
  integrity sha512-QHTXI/sZQmko1cbDoNAa3mJ5qhWUUNAq3vR0/YiD379fWQrcfuoX1+HW2S0MTt7XmoPLapdaDKUtelUSPic7hQ==
  dependencies:
    graceful-fs "^4.2.4"
    tapable "^2.2.0"

entities@^2.0.0:
  version "2.2.0"
  resolved "https://registry.yarnpkg.com/entities/-/entities-2.2.0.tgz#098dc90ebb83d8dffa089d55256b351d34c4da55"
  integrity sha512-p92if5Nz619I0w+akJrLZH0MX0Pb5DX39XOwQTtXSdQQOaYH03S1uIQp4mhOZtAXrxq4ViO67YTiLBo2638o9A==

entities@^4.4.0:
  version "4.4.0"
  resolved "https://registry.yarnpkg.com/entities/-/entities-4.4.0.tgz#97bdaba170339446495e653cfd2db78962900174"
  integrity sha512-oYp7156SP8LkeGD0GF85ad1X9Ai79WtRsZ2gxJqtBuzH+98YUV6jkHEKlZkMbcrjJjIVJNIDP/3WL9wQkoPbWA==

entities@~3.0.1:
  version "3.0.1"
  resolved "https://registry.yarnpkg.com/entities/-/entities-3.0.1.tgz#2b887ca62585e96db3903482d336c1006c3001d4"
  integrity sha512-WiyBqoomrwMdFG1e0kqvASYfnlb0lp8M5o5Fw2OFq1hNZxxcNk8Ik0Xm7LxzBhuidnZB/UtBqVCgUz3kBOP51Q==

error-ex@^1.3.1:
  version "1.3.2"
  resolved "https://registry.yarnpkg.com/error-ex/-/error-ex-1.3.2.tgz#b4ac40648107fdcdcfae242f428bea8a14d4f1bf"
  integrity sha512-7dFHNmqeFSEt2ZBsCriorKnn3Z2pj+fd9kmI6QoWw4//DL+icEBfc0U7qJCisqrTsKTjw4fNFy2pW9OqStD84g==
  dependencies:
    is-arrayish "^0.2.1"

es-abstract@^1.19.0, es-abstract@^1.20.4:
  version "1.20.5"
  resolved "https://registry.yarnpkg.com/es-abstract/-/es-abstract-1.20.5.tgz#e6dc99177be37cacda5988e692c3fa8b218e95d2"
  integrity sha512-7h8MM2EQhsCA7pU/Nv78qOXFpD8Rhqd12gYiSJVkrH9+e8VuA8JlPJK/hQjjlLv6pJvx/z1iRFKzYb0XT/RuAQ==
  dependencies:
    call-bind "^1.0.2"
    es-to-primitive "^1.2.1"
    function-bind "^1.1.1"
    function.prototype.name "^1.1.5"
    get-intrinsic "^1.1.3"
    get-symbol-description "^1.0.0"
    gopd "^1.0.1"
    has "^1.0.3"
    has-property-descriptors "^1.0.0"
    has-symbols "^1.0.3"
    internal-slot "^1.0.3"
    is-callable "^1.2.7"
    is-negative-zero "^2.0.2"
    is-regex "^1.1.4"
    is-shared-array-buffer "^1.0.2"
    is-string "^1.0.7"
    is-weakref "^1.0.2"
    object-inspect "^1.12.2"
    object-keys "^1.1.1"
    object.assign "^4.1.4"
    regexp.prototype.flags "^1.4.3"
    safe-regex-test "^1.0.0"
    string.prototype.trimend "^1.0.6"
    string.prototype.trimstart "^1.0.6"
    unbox-primitive "^1.0.2"

es-shim-unscopables@^1.0.0:
  version "1.0.0"
  resolved "https://registry.yarnpkg.com/es-shim-unscopables/-/es-shim-unscopables-1.0.0.tgz#702e632193201e3edf8713635d083d378e510241"
  integrity sha512-Jm6GPcCdC30eMLbZ2x8z2WuRwAws3zTBBKuusffYVUrNj/GVSUAZ+xKMaUpfNDR5IbyNA5LJbaecoUVbmUcB1w==
  dependencies:
    has "^1.0.3"

es-to-primitive@^1.2.1:
  version "1.2.1"
  resolved "https://registry.yarnpkg.com/es-to-primitive/-/es-to-primitive-1.2.1.tgz#e55cd4c9cdc188bcefb03b366c736323fc5c898a"
  integrity sha512-QCOllgZJtaUo9miYBcLChTUaHNjJF3PYs1VidD7AwiEj1kYxKeQTctLAezAOH5ZKRH0g2IgPn6KwB4IT8iRpvA==
  dependencies:
    is-callable "^1.1.4"
    is-date-object "^1.0.1"
    is-symbol "^1.0.2"

escalade@^3.1.1:
  version "3.1.1"
  resolved "https://registry.yarnpkg.com/escalade/-/escalade-3.1.1.tgz#d8cfdc7000965c5a0174b4a82eaa5c0552742e40"
  integrity sha512-k0er2gUkLf8O0zKJiAhmkTnJlTvINGv7ygDNPbeIsX/TJjGJZHuh9B2UxbsaEkmlEo9MfhrSzmhIlhRlI2GXnw==

escape-string-regexp@^1.0.2, escape-string-regexp@^1.0.5:
  version "1.0.5"
  resolved "https://registry.yarnpkg.com/escape-string-regexp/-/escape-string-regexp-1.0.5.tgz#1b61c0562190a8dff6ae3bb2cf0200ca130b86d4"
  integrity sha512-vbRorB5FUQWvla16U8R/qgaFIya2qGzwDrNmCZuYKrbdSUMG6I1ZCGQRefkRVhuOkIGVne7BQ35DSfo1qvJqFg==

escape-string-regexp@^4.0.0:
  version "4.0.0"
  resolved "https://registry.yarnpkg.com/escape-string-regexp/-/escape-string-regexp-4.0.0.tgz#14ba83a5d373e3d311e5afca29cf5bfad965bf34"
  integrity sha512-TtpcNJ3XAzx3Gq8sWRzJaVajRs0uVxA2YAkdb1jm2YkPz4G6egUFAyA3n5vtEIZefPk5Wa4UXbKuS5fKkJWdgA==

escape-string-regexp@^5.0.0:
  version "5.0.0"
  resolved "https://registry.yarnpkg.com/escape-string-regexp/-/escape-string-regexp-5.0.0.tgz#4683126b500b61762f2dbebace1806e8be31b1c8"
  integrity sha512-/veY75JbMK4j1yjvuUxuVsiS/hr/4iHs9FTT6cgTexxdE0Ly/glccBAkloH/DofkjRbZU3bnoj38mOmhkZ0lHw==

eslint-config-next@^13.1.1:
  version "13.1.1"
  resolved "https://registry.yarnpkg.com/eslint-config-next/-/eslint-config-next-13.1.1.tgz#b1a6602b0a339820585d4b2f8d2e08866b6699a7"
  integrity sha512-/5S2XGWlGaiqrRhzpn51ux5JUSLwx8PVK2keLi5xk7QmhfYB8PqE6R6SlVw6hgnf/VexvUXSrlNJ/su00NhtHQ==
  dependencies:
    "@next/eslint-plugin-next" "13.1.1"
    "@rushstack/eslint-patch" "^1.1.3"
    "@typescript-eslint/parser" "^5.42.0"
    eslint-import-resolver-node "^0.3.6"
    eslint-import-resolver-typescript "^3.5.2"
    eslint-plugin-import "^2.26.0"
    eslint-plugin-jsx-a11y "^6.5.1"
    eslint-plugin-react "^7.31.7"
    eslint-plugin-react-hooks "^4.5.0"

eslint-config-prettier@^8.3.0:
  version "8.5.0"
  resolved "https://registry.yarnpkg.com/eslint-config-prettier/-/eslint-config-prettier-8.5.0.tgz#5a81680ec934beca02c7b1a61cf8ca34b66feab1"
  integrity sha512-obmWKLUNCnhtQRKc+tmnYuQl0pFU1ibYJQ5BGhTVB08bHe9wC8qUeG7c08dj9XX+AuPj1YSGSQIHl1pnDHZR0Q==

eslint-import-resolver-node@^0.3.6:
  version "0.3.6"
  resolved "https://registry.yarnpkg.com/eslint-import-resolver-node/-/eslint-import-resolver-node-0.3.6.tgz#4048b958395da89668252001dbd9eca6b83bacbd"
  integrity sha512-0En0w03NRVMn9Uiyn8YRPDKvWjxCWkslUEhGNTdGx15RvPJYQ+lbOlqrlNI2vEAs4pDYK4f/HN2TbDmk5TP0iw==
  dependencies:
    debug "^3.2.7"
    resolve "^1.20.0"

eslint-import-resolver-typescript@^3.5.2:
  version "3.5.2"
  resolved "https://registry.yarnpkg.com/eslint-import-resolver-typescript/-/eslint-import-resolver-typescript-3.5.2.tgz#9431acded7d898fd94591a08ea9eec3514c7de91"
  integrity sha512-zX4ebnnyXiykjhcBvKIf5TNvt8K7yX6bllTRZ14MiurKPjDpCAZujlszTdB8pcNXhZcOf+god4s9SjQa5GnytQ==
  dependencies:
    debug "^4.3.4"
    enhanced-resolve "^5.10.0"
    get-tsconfig "^4.2.0"
    globby "^13.1.2"
    is-core-module "^2.10.0"
    is-glob "^4.0.3"
    synckit "^0.8.4"

eslint-module-utils@^2.7.3:
  version "2.7.4"
  resolved "https://registry.yarnpkg.com/eslint-module-utils/-/eslint-module-utils-2.7.4.tgz#4f3e41116aaf13a20792261e61d3a2e7e0583974"
  integrity sha512-j4GT+rqzCoRKHwURX7pddtIPGySnX9Si/cgMI5ztrcqOPtk5dDEeZ34CQVPphnqkJytlc97Vuk05Um2mJ3gEQA==
  dependencies:
    debug "^3.2.7"

eslint-plugin-import@^2.25.4, eslint-plugin-import@^2.26.0:
  version "2.26.0"
  resolved "https://registry.yarnpkg.com/eslint-plugin-import/-/eslint-plugin-import-2.26.0.tgz#f812dc47be4f2b72b478a021605a59fc6fe8b88b"
  integrity sha512-hYfi3FXaM8WPLf4S1cikh/r4IxnO6zrhZbEGz2b660EJRbuxgpDS5gkCuYgGWg2xxh2rBuIr4Pvhve/7c31koA==
  dependencies:
    array-includes "^3.1.4"
    array.prototype.flat "^1.2.5"
    debug "^2.6.9"
    doctrine "^2.1.0"
    eslint-import-resolver-node "^0.3.6"
    eslint-module-utils "^2.7.3"
    has "^1.0.3"
    is-core-module "^2.8.1"
    is-glob "^4.0.3"
    minimatch "^3.1.2"
    object.values "^1.1.5"
    resolve "^1.22.0"
    tsconfig-paths "^3.14.1"

eslint-plugin-jsx-a11y@^6.5.1:
  version "6.6.1"
  resolved "https://registry.yarnpkg.com/eslint-plugin-jsx-a11y/-/eslint-plugin-jsx-a11y-6.6.1.tgz#93736fc91b83fdc38cc8d115deedfc3091aef1ff"
  integrity sha512-sXgFVNHiWffBq23uiS/JaP6eVR622DqwB4yTzKvGZGcPq6/yZ3WmOZfuBks/vHWo9GaFOqC2ZK4i6+C35knx7Q==
  dependencies:
    "@babel/runtime" "^7.18.9"
    aria-query "^4.2.2"
    array-includes "^3.1.5"
    ast-types-flow "^0.0.7"
    axe-core "^4.4.3"
    axobject-query "^2.2.0"
    damerau-levenshtein "^1.0.8"
    emoji-regex "^9.2.2"
    has "^1.0.3"
    jsx-ast-utils "^3.3.2"
    language-tags "^1.0.5"
    minimatch "^3.1.2"
    semver "^6.3.0"

eslint-plugin-react-hooks@^4.5.0:
  version "4.6.0"
  resolved "https://registry.yarnpkg.com/eslint-plugin-react-hooks/-/eslint-plugin-react-hooks-4.6.0.tgz#4c3e697ad95b77e93f8646aaa1630c1ba607edd3"
  integrity sha512-oFc7Itz9Qxh2x4gNHStv3BqJq54ExXmfC+a1NjAta66IAN87Wu0R/QArgIS9qKzX3dXKPI9H5crl9QchNMY9+g==

eslint-plugin-react@^7.31.7:
  version "7.31.11"
  resolved "https://registry.yarnpkg.com/eslint-plugin-react/-/eslint-plugin-react-7.31.11.tgz#011521d2b16dcf95795df688a4770b4eaab364c8"
  integrity sha512-TTvq5JsT5v56wPa9OYHzsrOlHzKZKjV+aLgS+55NJP/cuzdiQPC7PfYoUjMoxlffKtvijpk7vA/jmuqRb9nohw==
  dependencies:
    array-includes "^3.1.6"
    array.prototype.flatmap "^1.3.1"
    array.prototype.tosorted "^1.1.1"
    doctrine "^2.1.0"
    estraverse "^5.3.0"
    jsx-ast-utils "^2.4.1 || ^3.0.0"
    minimatch "^3.1.2"
    object.entries "^1.1.6"
    object.fromentries "^2.0.6"
    object.hasown "^1.1.2"
    object.values "^1.1.6"
    prop-types "^15.8.1"
    resolve "^2.0.0-next.3"
    semver "^6.3.0"
    string.prototype.matchall "^4.0.8"

eslint-scope@^5.1.1:
  version "5.1.1"
  resolved "https://registry.yarnpkg.com/eslint-scope/-/eslint-scope-5.1.1.tgz#e786e59a66cb92b3f6c1fb0d508aab174848f48c"
  integrity sha512-2NxwbF/hZ0KpepYN0cNbo+FN6XoK7GaHlQhgx/hIZl6Va0bF45RQOOwhLIy8lQDbuCiadSLCBnH2CFYquit5bw==
  dependencies:
    esrecurse "^4.3.0"
    estraverse "^4.1.1"

eslint-scope@^7.1.1:
  version "7.1.1"
  resolved "https://registry.yarnpkg.com/eslint-scope/-/eslint-scope-7.1.1.tgz#fff34894c2f65e5226d3041ac480b4513a163642"
  integrity sha512-QKQM/UXpIiHcLqJ5AOyIW7XZmzjkzQXYE54n1++wb0u9V/abW3l9uQnxX8Z5Xd18xyKIMTUAyQ0k1e8pz6LUrw==
  dependencies:
    esrecurse "^4.3.0"
    estraverse "^5.2.0"

eslint-utils@^3.0.0:
  version "3.0.0"
  resolved "https://registry.yarnpkg.com/eslint-utils/-/eslint-utils-3.0.0.tgz#8aebaface7345bb33559db0a1f13a1d2d48c3672"
  integrity sha512-uuQC43IGctw68pJA1RgbQS8/NP7rch6Cwd4j3ZBtgo4/8Flj4eGE7ZYSZRN3iq5pVUv6GPdW5Z1RFleo84uLDA==
  dependencies:
    eslint-visitor-keys "^2.0.0"

eslint-visitor-keys@^2.0.0:
  version "2.1.0"
  resolved "https://registry.yarnpkg.com/eslint-visitor-keys/-/eslint-visitor-keys-2.1.0.tgz#f65328259305927392c938ed44eb0a5c9b2bd303"
  integrity sha512-0rSmRBzXgDzIsD6mGdJgevzgezI534Cer5L/vyMX0kHzT/jiB43jRhd9YUlMGYLQy2zprNmoT8qasCGtY+QaKw==

eslint-visitor-keys@^3.3.0:
  version "3.3.0"
  resolved "https://registry.yarnpkg.com/eslint-visitor-keys/-/eslint-visitor-keys-3.3.0.tgz#f6480fa6b1f30efe2d1968aa8ac745b862469826"
  integrity sha512-mQ+suqKJVyeuwGYHAdjMFqjCyfl8+Ldnxuyp3ldiMBFKkvytrXUZWaiPCEav8qDHKty44bD+qV1IP4T+w+xXRA==

eslint@^8.30.0:
  version "8.30.0"
  resolved "https://registry.yarnpkg.com/eslint/-/eslint-8.30.0.tgz#83a506125d089eef7c5b5910eeea824273a33f50"
  integrity sha512-MGADB39QqYuzEGov+F/qb18r4i7DohCDOfatHaxI2iGlPuC65bwG2gxgO+7DkyL38dRFaRH7RaRAgU6JKL9rMQ==
  dependencies:
    "@eslint/eslintrc" "^1.4.0"
    "@humanwhocodes/config-array" "^0.11.8"
    "@humanwhocodes/module-importer" "^1.0.1"
    "@nodelib/fs.walk" "^1.2.8"
    ajv "^6.10.0"
    chalk "^4.0.0"
    cross-spawn "^7.0.2"
    debug "^4.3.2"
    doctrine "^3.0.0"
    escape-string-regexp "^4.0.0"
    eslint-scope "^7.1.1"
    eslint-utils "^3.0.0"
    eslint-visitor-keys "^3.3.0"
    espree "^9.4.0"
    esquery "^1.4.0"
    esutils "^2.0.2"
    fast-deep-equal "^3.1.3"
    file-entry-cache "^6.0.1"
    find-up "^5.0.0"
    glob-parent "^6.0.2"
    globals "^13.19.0"
    grapheme-splitter "^1.0.4"
    ignore "^5.2.0"
    import-fresh "^3.0.0"
    imurmurhash "^0.1.4"
    is-glob "^4.0.0"
    is-path-inside "^3.0.3"
    js-sdsl "^4.1.4"
    js-yaml "^4.1.0"
    json-stable-stringify-without-jsonify "^1.0.1"
    levn "^0.4.1"
    lodash.merge "^4.6.2"
    minimatch "^3.1.2"
    natural-compare "^1.4.0"
    optionator "^0.9.1"
    regexpp "^3.2.0"
    strip-ansi "^6.0.1"
    strip-json-comments "^3.1.0"
    text-table "^0.2.0"

esm@^3.2.25:
  version "3.2.25"
  resolved "https://registry.yarnpkg.com/esm/-/esm-3.2.25.tgz#342c18c29d56157688ba5ce31f8431fbb795cc10"
  integrity sha512-U1suiZ2oDVWv4zPO56S0NcR5QriEahGtdN2OR6FiOG4WJvcjBVFB0qI4+eKoWFH483PKGuLuu6V8Z4T5g63UVA==

espree@^9.4.0:
  version "9.4.1"
  resolved "https://registry.yarnpkg.com/espree/-/espree-9.4.1.tgz#51d6092615567a2c2cff7833445e37c28c0065bd"
  integrity sha512-XwctdmTO6SIvCzd9810yyNzIrOrqNYV9Koizx4C/mRhf9uq0o4yHoCEU/670pOxOL/MSraektvSAji79kX90Vg==
  dependencies:
    acorn "^8.8.0"
    acorn-jsx "^5.3.2"
    eslint-visitor-keys "^3.3.0"

esprima@^4.0.0:
  version "4.0.1"
  resolved "https://registry.yarnpkg.com/esprima/-/esprima-4.0.1.tgz#13b04cdb3e6c5d19df91ab6987a8695619b0aa71"
  integrity sha512-eGuFFw7Upda+g4p+QHvnW0RyTX/SVeJBDM/gCtMARO0cLuT2HcEKnTPvhjV6aGeqrCB/sbNop0Kszm0jsaWU4A==

esquery@^1.4.0:
  version "1.4.0"
  resolved "https://registry.yarnpkg.com/esquery/-/esquery-1.4.0.tgz#2148ffc38b82e8c7057dfed48425b3e61f0f24a5"
  integrity sha512-cCDispWt5vHHtwMY2YrAQ4ibFkAL8RbH5YGBnZBc90MolvvfkkQcJro/aZiAQUlQ3qgrYS6D6v8Gc5G5CQsc9w==
  dependencies:
    estraverse "^5.1.0"

esrecurse@^4.3.0:
  version "4.3.0"
  resolved "https://registry.yarnpkg.com/esrecurse/-/esrecurse-4.3.0.tgz#7ad7964d679abb28bee72cec63758b1c5d2c9921"
  integrity sha512-KmfKL3b6G+RXvP8N1vr3Tq1kL/oCFgn2NYXEtqP8/L3pKapUA4G8cFVaoF3SU323CD4XypR/ffioHmkti6/Tag==
  dependencies:
    estraverse "^5.2.0"

estraverse@^4.1.1:
  version "4.3.0"
  resolved "https://registry.yarnpkg.com/estraverse/-/estraverse-4.3.0.tgz#398ad3f3c5a24948be7725e83d11a7de28cdbd1d"
  integrity sha512-39nnKffWz8xN1BU/2c79n9nB9HDzo0niYUqx6xyqUnyoAnQyyWpOTdZEeiCch8BBu515t4wp9ZmgVfVhn9EBpw==

estraverse@^5.1.0, estraverse@^5.2.0, estraverse@^5.3.0:
  version "5.3.0"
  resolved "https://registry.yarnpkg.com/estraverse/-/estraverse-5.3.0.tgz#2eea5290702f26ab8fe5370370ff86c965d21123"
  integrity sha512-MMdARuVEQziNTeJD8DgMqmhwR11BRQ/cBP+pLtYdSTnf3MIO8fFeiINEbX36ZdNlfU/7A9f3gUw49B3oQsvwBA==

esutils@^2.0.2:
  version "2.0.3"
  resolved "https://registry.yarnpkg.com/esutils/-/esutils-2.0.3.tgz#74d2eb4de0b8da1293711910d50775b9b710ef64"
  integrity sha512-kVscqXk4OCp68SZ0dkgEKVi6/8ij300KBWTJq32P/dYeWTSwK41WyTxalN1eRmA5Z9UU/LX9D7FWSmV9SAYx6g==

event-target-shim@^5.0.0:
  version "5.0.1"
  resolved "https://registry.yarnpkg.com/event-target-shim/-/event-target-shim-5.0.1.tgz#5d4d3ebdf9583d63a5333ce2deb7480ab2b05789"
  integrity sha512-i/2XbnSz/uxRCU6+NdVJgKWDTM427+MqYbkQzD321DuCQJUqOuJKIA0IM2+W2xtYHdKOmZ4dR6fExsd4SXL+WQ==

events@^3.0.0:
  version "3.3.0"
  resolved "https://registry.yarnpkg.com/events/-/events-3.3.0.tgz#31a95ad0a924e2d2c419a813aeb2c4e878ea7400"
  integrity sha512-mQw+2fkQbALzQ7V0MY0IqdnXNOeTtP4r0lN9z7AAawCXgqea7bDii20AYrIBrFd/Hx0M2Ocz6S111CaFkUcb0Q==

execa@5.1.1, execa@^5.0.0:
  version "5.1.1"
  resolved "https://registry.yarnpkg.com/execa/-/execa-5.1.1.tgz#f80ad9cbf4298f7bd1d4c9555c21e93741c411dd"
  integrity sha512-8uSpZZocAZRBAPIEINJj3Lo9HyGitllczc27Eh5YYojjMFMn8yHMDMaUHE2Jqfq05D/wucwI4JGURyXt1vchyg==
  dependencies:
    cross-spawn "^7.0.3"
    get-stream "^6.0.0"
    human-signals "^2.1.0"
    is-stream "^2.0.0"
    merge-stream "^2.0.0"
    npm-run-path "^4.0.1"
    onetime "^5.1.2"
    signal-exit "^3.0.3"
    strip-final-newline "^2.0.0"

extend-shallow@^2.0.1:
  version "2.0.1"
  resolved "https://registry.yarnpkg.com/extend-shallow/-/extend-shallow-2.0.1.tgz#51af7d614ad9a9f610ea1bafbb989d6b1c56890f"
  integrity sha512-zCnTtlxNoAiDc3gqY2aYAWFx7XWWiasuF2K8Me5WbN8otHKTUKBwjPtNpRs/rbUZm7KxWAaNj7P1a/p52GbVug==
  dependencies:
    is-extendable "^0.1.0"

extend@^3.0.0:
  version "3.0.2"
  resolved "https://registry.yarnpkg.com/extend/-/extend-3.0.2.tgz#f8b1136b4071fbd8eb140aff858b1019ec2915fa"
  integrity sha512-fjquC59cD7CyW6urNXK0FBufkZcoiGG80wTuPujX590cB5Ttln20E2UB4S/WARVqhXffZl2LNgS+gQdPIIim/g==

fast-deep-equal@^3.1.1, fast-deep-equal@^3.1.3:
  version "3.1.3"
  resolved "https://registry.yarnpkg.com/fast-deep-equal/-/fast-deep-equal-3.1.3.tgz#3a7d56b559d6cbc3eb512325244e619a65c6c525"
  integrity sha512-f3qQ9oQy9j2AhBe/H9VC91wLmKBCCU/gDOnKNAYG5hswO7BLKj09Hc5HYNz9cGI++xlpDCIgDaitVs03ATR84Q==

fast-glob@^3.2.11, fast-glob@^3.2.12, fast-glob@^3.2.9:
  version "3.2.12"
  resolved "https://registry.yarnpkg.com/fast-glob/-/fast-glob-3.2.12.tgz#7f39ec99c2e6ab030337142da9e0c18f37afae80"
  integrity sha512-DVj4CQIYYow0BlaelwK1pHl5n5cRSJfM60UA0zK891sVInoPri2Ekj7+e1CT3/3qxXenpI+nBBmQAcJPJgaj4w==
  dependencies:
    "@nodelib/fs.stat" "^2.0.2"
    "@nodelib/fs.walk" "^1.2.3"
    glob-parent "^5.1.2"
    merge2 "^1.3.0"
    micromatch "^4.0.4"

fast-json-stable-stringify@^2.0.0:
  version "2.1.0"
  resolved "https://registry.yarnpkg.com/fast-json-stable-stringify/-/fast-json-stable-stringify-2.1.0.tgz#874bf69c6f404c2b5d99c481341399fd55892633"
  integrity sha512-lhd/wF+Lk98HZoTCtlVraHtfh5XYijIjalXck7saUtuanSDyLMxnHhSXEDJqHxD7msR8D0uCmqlkwjCV8xvwHw==

fast-levenshtein@^2.0.6:
  version "2.0.6"
  resolved "https://registry.yarnpkg.com/fast-levenshtein/-/fast-levenshtein-2.0.6.tgz#3d8a5c66883a16a30ca8643e851f19baa7797917"
  integrity sha512-DCXu6Ifhqcks7TZKY3Hxp3y6qphY5SJZmrWMDrKcERSOXWQdMhU9Ig/PYrzyw/ul9jOIyh0N4M0tbC5hodg8dw==

fastq@^1.6.0:
  version "1.14.0"
  resolved "https://registry.yarnpkg.com/fastq/-/fastq-1.14.0.tgz#107f69d7295b11e0fccc264e1fc6389f623731ce"
  integrity sha512-eR2D+V9/ExcbF9ls441yIuN6TI2ED1Y2ZcA5BmMtJsOkWOFRJQ0Jt0g1UwqXJJVAb+V+umH5Dfr8oh4EVP7VVg==
  dependencies:
    reusify "^1.0.4"

fetch-blob@^3.1.2, fetch-blob@^3.1.4:
  version "3.2.0"
  resolved "https://registry.yarnpkg.com/fetch-blob/-/fetch-blob-3.2.0.tgz#f09b8d4bbd45adc6f0c20b7e787e793e309dcce9"
  integrity sha512-7yAQpD2UMJzLi1Dqv7qFYnPbaPx7ZfFK6PiIxQ4PfkGPyNyl2Ugx+a/umUonmKqjhM4DnfbMvdX6otXq83soQQ==
  dependencies:
    node-domexception "^1.0.0"
    web-streams-polyfill "^3.0.3"

file-entry-cache@^6.0.1:
  version "6.0.1"
  resolved "https://registry.yarnpkg.com/file-entry-cache/-/file-entry-cache-6.0.1.tgz#211b2dd9659cb0394b073e7323ac3c933d522027"
  integrity sha512-7Gps/XWymbLk2QLYK4NzpMOrYjMhdIxXuIvy2QBsLE6ljuodKvdkWs/cpyJJ3CVIVpH0Oi1Hvg1ovbMzLdFBBg==
  dependencies:
    flat-cache "^3.0.4"

filename-reserved-regex@^2.0.0:
  version "2.0.0"
  resolved "https://registry.yarnpkg.com/filename-reserved-regex/-/filename-reserved-regex-2.0.0.tgz#abf73dfab735d045440abfea2d91f389ebbfa229"
  integrity sha512-lc1bnsSr4L4Bdif8Xb/qrtokGbq5zlsms/CYH8PP+WtCkGNF65DPiQY8vG3SakEdRn8Dlnm+gW/qWKKjS5sZzQ==

filenamify@^4.1.0:
  version "4.3.0"
  resolved "https://registry.yarnpkg.com/filenamify/-/filenamify-4.3.0.tgz#62391cb58f02b09971c9d4f9d63b3cf9aba03106"
  integrity sha512-hcFKyUG57yWGAzu1CMt/dPzYZuv+jAJUT85bL8mrXvNe6hWj6yEHEc4EdcgiA6Z3oi1/9wXJdZPXF2dZNgwgOg==
  dependencies:
    filename-reserved-regex "^2.0.0"
    strip-outer "^1.0.1"
    trim-repeated "^1.0.0"

fill-range@^7.0.1:
  version "7.0.1"
  resolved "https://registry.yarnpkg.com/fill-range/-/fill-range-7.0.1.tgz#1919a6a7c75fe38b2c7c77e5198535da9acdda40"
  integrity sha512-qOo9F+dMUmC2Lcb4BbVvnKJxTPjCm+RRpe4gDuGrzkL7mEVl/djYSu2OdQ2Pa302N4oqkSg9ir6jaLWJ2USVpQ==
  dependencies:
    to-regex-range "^5.0.1"

find-up@^4.0.0:
  version "4.1.0"
  resolved "https://registry.yarnpkg.com/find-up/-/find-up-4.1.0.tgz#97afe7d6cdc0bc5928584b7c8d7b16e8a9aa5d19"
  integrity sha512-PpOwAdQ/YlXQ2vj8a3h8IipDuYRi3wceVQQGYWxNINccq40Anw7BlsEXCMbt1Zt+OLA6Fq9suIpIWD0OsnISlw==
  dependencies:
    locate-path "^5.0.0"
    path-exists "^4.0.0"

find-up@^5.0.0:
  version "5.0.0"
  resolved "https://registry.yarnpkg.com/find-up/-/find-up-5.0.0.tgz#4c92819ecb7083561e4f4a240a86be5198f536fc"
  integrity sha512-78/PXT1wlLLDgTzDs7sjq9hzz0vXD+zn+7wypEe4fXQxCmdmqfGsEPQxmiCSQI3ajFV91bVSsvNtrJRiW6nGng==
  dependencies:
    locate-path "^6.0.0"
    path-exists "^4.0.0"

flat-cache@^3.0.4:
  version "3.0.4"
  resolved "https://registry.yarnpkg.com/flat-cache/-/flat-cache-3.0.4.tgz#61b0338302b2fe9f957dcc32fc2a87f1c3048b11"
  integrity sha512-dm9s5Pw7Jc0GvMYbshN6zchCA9RgQlzzEZX3vylR9IqFfS8XciblUXOKfW6SiuJ0e13eDYZoZV5wdrev7P3Nwg==
  dependencies:
    flatted "^3.1.0"
    rimraf "^3.0.2"

flatted@^3.1.0:
  version "3.2.7"
  resolved "https://registry.yarnpkg.com/flatted/-/flatted-3.2.7.tgz#609f39207cb614b89d0765b477cb2d437fbf9787"
  integrity sha512-5nqDSxl8nn5BSNxyR3n4I6eDmbolI6WT+QqR547RwxQapgjQBmtktdP+HTBb/a/zLsbzERTONyUB5pefh5TtjQ==

focus-trap-react@^10.0.2:
  version "10.0.2"
  resolved "https://registry.yarnpkg.com/focus-trap-react/-/focus-trap-react-10.0.2.tgz#eed4ce5b508bf3a0ce2ce63151c5c0f34a8f8529"
  integrity sha512-MnN2cmdgpY7NY74ePOio4kbO5A3ILhrg1g5OGbgIQjcWEv1hhcbh6e98K0a+df88hNbE+4i9r8ji9aQnHou6GA==
  dependencies:
    focus-trap "^7.2.0"
    tabbable "^6.0.1"

focus-trap@^7.2.0:
  version "7.2.0"
  resolved "https://registry.yarnpkg.com/focus-trap/-/focus-trap-7.2.0.tgz#25af61b5635d3c18cd2fd176087db7b60be72c6b"
  integrity sha512-v4wY6HDDYvzkBy4735kW5BUEuw6Yz9ABqMYLuTNbzAFPcBOGiGHwwcNVMvUz4G0kgSYh13wa/7TG3XwTeT4O/A==
  dependencies:
    tabbable "^6.0.1"

focus-visible@^5.2.0:
  version "5.2.0"
  resolved "https://registry.yarnpkg.com/focus-visible/-/focus-visible-5.2.0.tgz#3a9e41fccf587bd25dcc2ef045508284f0a4d6b3"
  integrity sha512-Rwix9pBtC1Nuy5wysTmKy+UjbDJpIfg8eHjw0rjZ1mX4GNLz1Bmd16uDpI3Gk1i70Fgcs8Csg2lPm8HULFg9DQ==

form-data@^3.0.0:
  version "3.0.1"
  resolved "https://registry.yarnpkg.com/form-data/-/form-data-3.0.1.tgz#ebd53791b78356a99af9a300d4282c4d5eb9755f"
  integrity sha512-RHkBKtLWUVwd7SqRIvCZMEvAMoGUp0XU+seQiZejj0COz3RI3hWP4sCv3gZWWLjJTd7rGwcsF5eKZGii0r/hbg==
  dependencies:
    asynckit "^0.4.0"
    combined-stream "^1.0.8"
    mime-types "^2.1.12"

formdata-polyfill@^4.0.10:
  version "4.0.10"
  resolved "https://registry.yarnpkg.com/formdata-polyfill/-/formdata-polyfill-4.0.10.tgz#24807c31c9d402e002ab3d8c720144ceb8848423"
  integrity sha512-buewHzMvYL29jdeQTVILecSaZKnt/RJWjoZCF5OW60Z67/GmSLBkOFM7qh1PI3zFNtJbaZL5eQu1vLfazOwj4g==
  dependencies:
    fetch-blob "^3.1.2"

fraction.js@^4.2.0:
  version "4.2.0"
  resolved "https://registry.yarnpkg.com/fraction.js/-/fraction.js-4.2.0.tgz#448e5109a313a3527f5a3ab2119ec4cf0e0e2950"
  integrity sha512-MhLuK+2gUcnZe8ZHlaaINnQLl0xRIGRfcGk2yl8xoQAfHrSsL3rYu6FCmBdkdbhc9EPlwyGHewaRsvwRMJtAlA==

fs-constants@^1.0.0:
  version "1.0.0"
  resolved "https://registry.yarnpkg.com/fs-constants/-/fs-constants-1.0.0.tgz#6be0de9be998ce16af8afc24497b9ee9b7ccd9ad"
  integrity sha512-y6OAwoSIf7FyjMIv94u+b5rdheZEjzR63GTyZJm5qh4Bi+2YgwLCcI/fPFZkL5PSixOt6ZNKm+w+Hfp/Bciwow==

fs-extra@^8.1.0:
  version "8.1.0"
  resolved "https://registry.yarnpkg.com/fs-extra/-/fs-extra-8.1.0.tgz#49d43c45a88cd9677668cb7be1b46efdb8d2e1c0"
  integrity sha512-yhlQgA6mnOJUKOsRUFsgJdQCvkKhcz8tlZG5HBQfReYZy46OwLcY+Zia0mtdHsOo9y/hP+CxMN0TU9QxoOtG4g==
  dependencies:
    graceful-fs "^4.2.0"
    jsonfile "^4.0.0"
    universalify "^0.1.0"

fs-extra@~7.0.1:
  version "7.0.1"
  resolved "https://registry.yarnpkg.com/fs-extra/-/fs-extra-7.0.1.tgz#4f189c44aa123b895f722804f55ea23eadc348e9"
  integrity sha512-YJDaCJZEnBmcbw13fvdAM9AwNOJwOzrE4pqMqBq5nFiEqXUqHwlK4B+3pUw6JNvfSPtX05xFHtYy/1ni01eGCw==
  dependencies:
    graceful-fs "^4.1.2"
    jsonfile "^4.0.0"
    universalify "^0.1.0"

fs.realpath@^1.0.0:
  version "1.0.0"
  resolved "https://registry.yarnpkg.com/fs.realpath/-/fs.realpath-1.0.0.tgz#1504ad2523158caa40db4a2787cb01411994ea4f"
  integrity sha512-OO0pH2lK6a0hZnAdau5ItzHPI6pUlvI7jMVnxUQRtw4owF2wk8lOSabtGDCTP4Ggrg2MbGnWO9X8K1t4+fGMDw==

fsevents@~2.3.2:
  version "2.3.2"
  resolved "https://registry.yarnpkg.com/fsevents/-/fsevents-2.3.2.tgz#8a526f78b8fdf4623b709e0b975c52c24c02fd1a"
  integrity sha512-xiqMQR4xAeHTuB9uWm+fFRcIOgKBMiOBP+eXiyT7jsgVCq1bkVygt00oASowB7EdtpOHaaPgKt812P9ab+DDKA==

function-bind@^1.1.1:
  version "1.1.1"
  resolved "https://registry.yarnpkg.com/function-bind/-/function-bind-1.1.1.tgz#a56899d3ea3c9bab874bb9773b7c5ede92f4895d"
  integrity sha512-yIovAzMX49sF8Yl58fSCWJ5svSLuaibPxXQJFLmBObTuCr0Mf1KiPopGM9NiFjiYBCbfaa2Fh6breQ6ANVTI0A==

function.prototype.name@^1.1.5:
  version "1.1.5"
  resolved "https://registry.yarnpkg.com/function.prototype.name/-/function.prototype.name-1.1.5.tgz#cce0505fe1ffb80503e6f9e46cc64e46a12a9621"
  integrity sha512-uN7m/BzVKQnCUF/iW8jYea67v++2u7m5UgENbHRtdDVclOUP+FMPlCNdmk0h/ysGyo2tavMJEDqJAkJdRa1vMA==
  dependencies:
    call-bind "^1.0.2"
    define-properties "^1.1.3"
    es-abstract "^1.19.0"
    functions-have-names "^1.2.2"

functions-have-names@^1.2.2:
  version "1.2.3"
  resolved "https://registry.yarnpkg.com/functions-have-names/-/functions-have-names-1.2.3.tgz#0404fe4ee2ba2f607f0e0ec3c80bae994133b834"
  integrity sha512-xckBUXyTIqT97tq2x2AMb+g163b5JFysYk0x4qxNFwbfQkmNZoiRHb6sPzI9/QV33WeuvVYBUIiD4NzNIyqaRQ==

gauge@~2.7.3:
  version "2.7.4"
  resolved "https://registry.yarnpkg.com/gauge/-/gauge-2.7.4.tgz#2c03405c7538c39d7eb37b317022e325fb018bf7"
  integrity sha512-14x4kjc6lkD3ltw589k0NrPD6cCNTD6CWoVUNpB85+DrtONoZn+Rug6xZU5RvSC4+TZPxA5AnBibQYAvZn41Hg==
  dependencies:
    aproba "^1.0.3"
    console-control-strings "^1.0.0"
    has-unicode "^2.0.0"
    object-assign "^4.1.0"
    signal-exit "^3.0.0"
    string-width "^1.0.1"
    strip-ansi "^3.0.1"
    wide-align "^1.1.0"

gensync@^1.0.0-beta.2:
  version "1.0.0-beta.2"
  resolved "https://registry.yarnpkg.com/gensync/-/gensync-1.0.0-beta.2.tgz#32a6ee76c3d7f52d46b2b1ae5d93fea8580a25e0"
  integrity sha512-3hN7NaskYvMDLQY55gnW3NQ+mesEAepTqlg+VEbj7zzqEMBVNhzcGYYeqFo/TlYz6eQiFcp1HcsCZO+nGgS8zg==

get-caller-file@^2.0.5:
  version "2.0.5"
  resolved "https://registry.yarnpkg.com/get-caller-file/-/get-caller-file-2.0.5.tgz#4f94412a82db32f36e3b0b9741f8a97feb031f7e"
  integrity sha512-DyFP3BM/3YHTQOCUL/w0OZHR0lpKeGrxotcHWcqNEdnltqFwXVfhEBQ94eIo34AfQpo0rGki4cyIiftY06h2Fg==

get-intrinsic@^1.0.2, get-intrinsic@^1.1.1, get-intrinsic@^1.1.3:
  version "1.1.3"
  resolved "https://registry.yarnpkg.com/get-intrinsic/-/get-intrinsic-1.1.3.tgz#063c84329ad93e83893c7f4f243ef63ffa351385"
  integrity sha512-QJVz1Tj7MS099PevUG5jvnt9tSkXN8K14dxQlikJuPt4uD9hHAHjLyLBiLR5zELelBdD9QNRAXZzsJx0WaDL9A==
  dependencies:
    function-bind "^1.1.1"
    has "^1.0.3"
    has-symbols "^1.0.3"

get-stream@^6.0.0:
  version "6.0.1"
  resolved "https://registry.yarnpkg.com/get-stream/-/get-stream-6.0.1.tgz#a262d8eef67aced57c2852ad6167526a43cbf7b7"
  integrity sha512-ts6Wi+2j3jQjqi70w5AlN8DFnkSwC+MqmxEzdEALB2qXZYV3X/b1CTfgPLGJNMeAWxdPfU8FO1ms3NUfaHCPYg==

get-symbol-description@^1.0.0:
  version "1.0.0"
  resolved "https://registry.yarnpkg.com/get-symbol-description/-/get-symbol-description-1.0.0.tgz#7fdb81c900101fbd564dd5f1a30af5aadc1e58d6"
  integrity sha512-2EmdH1YvIQiZpltCNgkuiUnyukzxM/R6NDJX31Ke3BG1Nq5b0S2PhX59UKi9vZpPDQVdqn+1IcaAwnzTT5vCjw==
  dependencies:
    call-bind "^1.0.2"
    get-intrinsic "^1.1.1"

get-tsconfig@^4.2.0:
  version "4.2.0"
  resolved "https://registry.yarnpkg.com/get-tsconfig/-/get-tsconfig-4.2.0.tgz#ff368dd7104dab47bf923404eb93838245c66543"
  integrity sha512-X8u8fREiYOE6S8hLbq99PeykTDoLVnxvF4DjWKJmz9xy2nNRdUcV8ZN9tniJFeKyTU3qnC9lL8n4Chd6LmVKHg==

git-up@^7.0.0:
  version "7.0.0"
  resolved "https://registry.yarnpkg.com/git-up/-/git-up-7.0.0.tgz#bace30786e36f56ea341b6f69adfd83286337467"
  integrity sha512-ONdIrbBCFusq1Oy0sC71F5azx8bVkvtZtMJAsv+a6lz5YAmbNnLD6HAB4gptHZVLPR8S2/kVN6Gab7lryq5+lQ==
  dependencies:
    is-ssh "^1.4.0"
    parse-url "^8.1.0"

git-url-parse@^13.0.0:
  version "13.1.0"
  resolved "https://registry.yarnpkg.com/git-url-parse/-/git-url-parse-13.1.0.tgz#07e136b5baa08d59fabdf0e33170de425adf07b4"
  integrity sha512-5FvPJP/70WkIprlUZ33bm4UAaFdjcLkJLpWft1BeZKqwR0uhhNGoKwlUaPtVb4LxCSQ++erHapRak9kWGj+FCA==
  dependencies:
    git-up "^7.0.0"

github-slugger@^1.0.0:
  version "1.5.0"
  resolved "https://registry.yarnpkg.com/github-slugger/-/github-slugger-1.5.0.tgz#17891bbc73232051474d68bd867a34625c955f7d"
  integrity sha512-wIh+gKBI9Nshz2o46B0B3f5k/W+WI9ZAv6y5Dn5WJ5SK1t0TnDimB4WE5rmTD05ZAIn8HALCZVmCsvj0w0v0lw==

glob-parent@^5.1.2, glob-parent@~5.1.2:
  version "5.1.2"
  resolved "https://registry.yarnpkg.com/glob-parent/-/glob-parent-5.1.2.tgz#869832c58034fe68a4093c17dc15e8340d8401c4"
  integrity sha512-AOIgSQCepiJYwP3ARnGx+5VnTu2HBYdzbGP45eLw1vr3zB3vZLeyed1sC9hnbcOc9/SrMyM5RPQrkGz4aS9Zow==
  dependencies:
    is-glob "^4.0.1"

glob-parent@^6.0.2:
  version "6.0.2"
  resolved "https://registry.yarnpkg.com/glob-parent/-/glob-parent-6.0.2.tgz#6d237d99083950c79290f24c7642a3de9a28f9e3"
  integrity sha512-XxwI8EOhVQgWp6iDL+3b0r86f4d6AX6zSU55HfB4ydCEuXLXc5FcYeOu+nnGftS4TEju/11rt4KJPTMgbfmv4A==
  dependencies:
    is-glob "^4.0.3"

glob@7.1.7:
  version "7.1.7"
  resolved "https://registry.yarnpkg.com/glob/-/glob-7.1.7.tgz#3b193e9233f01d42d0b3f78294bbeeb418f94a90"
  integrity sha512-OvD9ENzPLbegENnYP5UUfJIirTg4+XwMWGaQfQTY0JenxNvvIKP3U3/tAQSPIu/lHxXYSZmpXlUHeqAIdKzBLQ==
  dependencies:
    fs.realpath "^1.0.0"
    inflight "^1.0.4"
    inherits "2"
    minimatch "^3.0.4"
    once "^1.3.0"
    path-is-absolute "^1.0.0"

glob@^7.1.3:
  version "7.2.3"
  resolved "https://registry.yarnpkg.com/glob/-/glob-7.2.3.tgz#b8df0fb802bbfa8e89bd1d938b4e16578ed44f2b"
  integrity sha512-nFR0zLpU2YCaRxwoCJvL6UvCH2JFyFVIvwTLsIf21AuHlMskA1hhTdk+LlYJtOlYt9v6dvszD2BGRqBL+iQK9Q==
  dependencies:
    fs.realpath "^1.0.0"
    inflight "^1.0.4"
    inherits "2"
    minimatch "^3.1.1"
    once "^1.3.0"
    path-is-absolute "^1.0.0"

globals@^11.1.0:
  version "11.12.0"
  resolved "https://registry.yarnpkg.com/globals/-/globals-11.12.0.tgz#ab8795338868a0babd8525758018c2a7eb95c42e"
  integrity sha512-WOBp/EEGUiIsJSp7wcv/y6MO+lV9UoncWqxuFfm8eBwzWNgyfBd6Gz+IeKQ9jCmyhoH99g15M3T+QaVHFjizVA==

globals@^13.19.0:
  version "13.19.0"
  resolved "https://registry.yarnpkg.com/globals/-/globals-13.19.0.tgz#7a42de8e6ad4f7242fbcca27ea5b23aca367b5c8"
  integrity sha512-dkQ957uSRWHw7CFXLUtUHQI3g3aWApYhfNR2O6jn/907riyTYKVBmxYVROkBcY614FSSeSJh7Xm7SrUWCxvJMQ==
  dependencies:
    type-fest "^0.20.2"

globalyzer@0.1.0:
  version "0.1.0"
  resolved "https://registry.yarnpkg.com/globalyzer/-/globalyzer-0.1.0.tgz#cb76da79555669a1519d5a8edf093afaa0bf1465"
  integrity sha512-40oNTM9UfG6aBmuKxk/giHn5nQ8RVz/SS4Ir6zgzOv9/qC3kKZ9v4etGTcJbEl/NyVQH7FGU7d+X1egr57Md2Q==

globby@^11.0.0, globby@^11.1.0:
  version "11.1.0"
  resolved "https://registry.yarnpkg.com/globby/-/globby-11.1.0.tgz#bd4be98bb042f83d796f7e3811991fbe82a0d34b"
  integrity sha512-jhIXaOzy1sb8IyocaruWSn1TjmnBVs8Ayhcy83rmxNJ8q2uWKCAj3CnJY+KpGSXCueAPc0i05kVvVKtP1t9S3g==
  dependencies:
    array-union "^2.1.0"
    dir-glob "^3.0.1"
    fast-glob "^3.2.9"
    ignore "^5.2.0"
    merge2 "^1.4.1"
    slash "^3.0.0"

globby@^13.1.2:
  version "13.1.3"
  resolved "https://registry.yarnpkg.com/globby/-/globby-13.1.3.tgz#f62baf5720bcb2c1330c8d4ef222ee12318563ff"
  integrity sha512-8krCNHXvlCgHDpegPzleMq07yMYTO2sXKASmZmquEYWEmCx6J5UTRbp5RwMJkTJGtcQ44YpiUYUiN0b9mzy8Bw==
  dependencies:
    dir-glob "^3.0.1"
    fast-glob "^3.2.11"
    ignore "^5.2.0"
    merge2 "^1.4.1"
    slash "^4.0.0"

globrex@^0.1.2:
  version "0.1.2"
  resolved "https://registry.yarnpkg.com/globrex/-/globrex-0.1.2.tgz#dd5d9ec826232730cd6793a5e33a9302985e6098"
  integrity sha512-uHJgbwAMwNFf5mLst7IWLNg14x1CkeqglJb/K3doi4dw6q2IvAAmM/Y81kevy83wP+Sst+nutFTYOGg3d1lsxg==

gopd@^1.0.1:
  version "1.0.1"
  resolved "https://registry.yarnpkg.com/gopd/-/gopd-1.0.1.tgz#29ff76de69dac7489b7c0918a5788e56477c332c"
  integrity sha512-d65bNlIadxvpb/A2abVdlqKqV563juRnZ1Wtk6s1sIR8uNsXR70xqIzVqxVf1eTqDunwT2MkczEeaezCKTZhwA==
  dependencies:
    get-intrinsic "^1.1.3"

graceful-fs@^4.1.2, graceful-fs@^4.1.6, graceful-fs@^4.2.0, graceful-fs@^4.2.4:
  version "4.2.10"
  resolved "https://registry.yarnpkg.com/graceful-fs/-/graceful-fs-4.2.10.tgz#147d3a006da4ca3ce14728c7aefc287c367d7a6c"
  integrity sha512-9ByhssR2fPVsNZj478qUUbKfmL0+t5BDVyjShtyZZLiK7ZDAArFFfopyOTj0M05wE2tJPisA4iTnnXl2YoPvOA==

grapheme-splitter@^1.0.4:
  version "1.0.4"
  resolved "https://registry.yarnpkg.com/grapheme-splitter/-/grapheme-splitter-1.0.4.tgz#9cf3a665c6247479896834af35cf1dbb4400767e"
  integrity sha512-bzh50DW9kTPM00T8y4o8vQg89Di9oLJVLW/KaOGIXJWP/iqCN6WKYkbNOF04vFLJhwcpYUh9ydh/+5vpOqV4YQ==

gray-matter@^4.0.3:
  version "4.0.3"
  resolved "https://registry.yarnpkg.com/gray-matter/-/gray-matter-4.0.3.tgz#e893c064825de73ea1f5f7d88c7a9f7274288798"
  integrity sha512-5v6yZd4JK3eMI3FqqCouswVqwugaA9r4dNZB1wwcmrD02QkV5H0y7XBQW8QwQqEaZY1pM9aqORSORhJRdNK44Q==
  dependencies:
    js-yaml "^3.13.1"
    kind-of "^6.0.2"
    section-matter "^1.0.0"
    strip-bom-string "^1.0.0"

gzip-size@^6.0.0:
  version "6.0.0"
  resolved "https://registry.yarnpkg.com/gzip-size/-/gzip-size-6.0.0.tgz#065367fd50c239c0671cbcbad5be3e2eeb10e462"
  integrity sha512-ax7ZYomf6jqPTQ4+XCpUGyXKHk5WweS+e05MBO4/y3WJ5RkmPXNKvX+bx1behVILVwr6JSQvZAku021CHPXG3Q==
  dependencies:
    duplexer "^0.1.2"

has-bigints@^1.0.1, has-bigints@^1.0.2:
  version "1.0.2"
  resolved "https://registry.yarnpkg.com/has-bigints/-/has-bigints-1.0.2.tgz#0871bd3e3d51626f6ca0966668ba35d5602d6eaa"
  integrity sha512-tSvCKtBr9lkF0Ex0aQiP9N+OpV4zi2r/Nee5VkRDbaqv35RLYMzbwQfFSZZH0kR+Rd6302UJZ2p/bJCEoR3VoQ==

has-flag@^3.0.0:
  version "3.0.0"
  resolved "https://registry.yarnpkg.com/has-flag/-/has-flag-3.0.0.tgz#b5d454dc2199ae225699f3467e5a07f3b955bafd"
  integrity sha512-sKJf1+ceQBr4SMkvQnBDNDtf4TXpVhVGateu0t918bl30FnbE2m4vNLX+VWe/dpjlb+HugGYzW7uQXH98HPEYw==

has-flag@^4.0.0:
  version "4.0.0"
  resolved "https://registry.yarnpkg.com/has-flag/-/has-flag-4.0.0.tgz#944771fd9c81c81265c4d6941860da06bb59479b"
  integrity sha512-EykJT/Q1KjTWctppgIAgfSO0tKVuZUjhgMr17kqTumMl6Afv3EISleU7qZUzoXDFTAHTDC4NOoG/ZxU3EvlMPQ==

has-property-descriptors@^1.0.0:
  version "1.0.0"
  resolved "https://registry.yarnpkg.com/has-property-descriptors/-/has-property-descriptors-1.0.0.tgz#610708600606d36961ed04c196193b6a607fa861"
  integrity sha512-62DVLZGoiEBDHQyqG4w9xCuZ7eJEwNmJRWw2VY84Oedb7WFcA27fiEVe8oUQx9hAUJ4ekurquucTGwsyO1XGdQ==
  dependencies:
    get-intrinsic "^1.1.1"

has-symbols@^1.0.2, has-symbols@^1.0.3:
  version "1.0.3"
  resolved "https://registry.yarnpkg.com/has-symbols/-/has-symbols-1.0.3.tgz#bb7b2c4349251dce87b125f7bdf874aa7c8b39f8"
  integrity sha512-l3LCuF6MgDNwTDKkdYGEihYjt5pRPbEg46rtlmnSPlUbgmB8LOIrKJbYYFBSbnPaJexMKtiPO8hmeRjRz2Td+A==

has-tostringtag@^1.0.0:
  version "1.0.0"
  resolved "https://registry.yarnpkg.com/has-tostringtag/-/has-tostringtag-1.0.0.tgz#7e133818a7d394734f941e73c3d3f9291e658b25"
  integrity sha512-kFjcSNhnlGV1kyoGk7OXKSawH5JOb/LzUc5w9B02hOTO0dfFRjbHQKvg1d6cf3HbeUmtU9VbbV3qzZ2Teh97WQ==
  dependencies:
    has-symbols "^1.0.2"

has-unicode@^2.0.0:
  version "2.0.1"
  resolved "https://registry.yarnpkg.com/has-unicode/-/has-unicode-2.0.1.tgz#e0e6fe6a28cf51138855e086d1691e771de2a8b9"
  integrity sha512-8Rf9Y83NBReMnx0gFzA8JImQACstCYWUplepDa9xprwwtmgEZUF0h/i5xSA625zB/I37EtrswSST6OXxwaaIJQ==

has@^1.0.3:
  version "1.0.3"
  resolved "https://registry.yarnpkg.com/has/-/has-1.0.3.tgz#722d7cbfc1f6aa8241f16dd814e011e1f41e8796"
  integrity sha512-f2dvO0VU6Oej7RkWJGrehjbzMAjFp5/VKPp5tTpWIV4JHHZK1/BxbFRtf/siA2SWTe09caDmVtYYzWEIbBS4zw==
  dependencies:
    function-bind "^1.1.1"

hast-to-hyperscript@^10.0.0:
  version "10.0.1"
  resolved "https://registry.yarnpkg.com/hast-to-hyperscript/-/hast-to-hyperscript-10.0.1.tgz#3decd7cb4654bca8883f6fcbd4fb3695628c4296"
  integrity sha512-dhIVGoKCQVewFi+vz3Vt567E4ejMppS1haBRL6TEmeLeJVB1i/FJIIg/e6s1Bwn0g5qtYojHEKvyGA+OZuyifw==
  dependencies:
    "@types/unist" "^2.0.0"
    comma-separated-tokens "^2.0.0"
    property-information "^6.0.0"
    space-separated-tokens "^2.0.0"
    style-to-object "^0.3.0"
    unist-util-is "^5.0.0"
    web-namespaces "^2.0.0"

hast-util-sanitize@^4.0.0:
  version "4.0.0"
  resolved "https://registry.yarnpkg.com/hast-util-sanitize/-/hast-util-sanitize-4.0.0.tgz#71a02ca2e50d04b852a5500846418070ca364f60"
  integrity sha512-pw56+69jq+QSr/coADNvWTmBPDy+XsmwaF5KnUys4/wM1jt/fZdl7GPxhXXXYdXnz3Gj3qMkbUCH2uKjvX0MgQ==
  dependencies:
    "@types/hast" "^2.0.0"

hast-util-whitespace@^2.0.0:
  version "2.0.0"
  resolved "https://registry.yarnpkg.com/hast-util-whitespace/-/hast-util-whitespace-2.0.0.tgz#4fc1086467cc1ef5ba20673cb6b03cec3a970f1c"
  integrity sha512-Pkw+xBHuV6xFeJprJe2BBEoDV+AvQySaz3pPDRUs5PNZEMQjpXJJueqrpcHIXxnWTcAGi/UOCgVShlkY6kLoqg==

highlight.js@^11.7.0:
  version "11.7.0"
  resolved "https://registry.yarnpkg.com/highlight.js/-/highlight.js-11.7.0.tgz#3ff0165bc843f8c9bce1fd89e2fda9143d24b11e"
  integrity sha512-1rRqesRFhMO/PRF+G86evnyJkCgaZFOI+Z6kdj15TA18funfoqJXvgPCLSf0SWq3SRfg1j3HlDs8o4s3EGq1oQ==

http-https@^1.0.0:
  version "1.0.0"
  resolved "https://registry.yarnpkg.com/http-https/-/http-https-1.0.0.tgz#2f908dd5f1db4068c058cd6e6d4ce392c913389b"
  integrity sha512-o0PWwVCSp3O0wS6FvNr6xfBCHgt0m1tvPLFOCc2iFDKTRAXhB7m8klDf7ErowFH8POa6dVdGatKU5I1YYwzUyg==

human-signals@^2.1.0:
  version "2.1.0"
  resolved "https://registry.yarnpkg.com/human-signals/-/human-signals-2.1.0.tgz#dc91fcba42e4d06e4abaed33b3e7a3c02f514ea0"
  integrity sha512-B4FFZ6q/T2jhhksgkbEW3HBvWIfDW85snkQgawt07S7J5QXTk6BkNV+0yAeZrM5QpMAdYlocGoljn0sJ/WQkFw==

ieee754@^1.1.13:
  version "1.2.1"
  resolved "https://registry.yarnpkg.com/ieee754/-/ieee754-1.2.1.tgz#8eb7a10a63fff25d15a57b001586d177d1b0d352"
  integrity sha512-dcyqhDvX1C46lXZcVqCpK+FtMRQVdIMN6/Df5js2zouUsqG7I6sFxitIC+7KYK29KdXOLHdu9zL4sFnoVQnqaA==

ignore@^5.2.0:
  version "5.2.4"
  resolved "https://registry.yarnpkg.com/ignore/-/ignore-5.2.4.tgz#a291c0c6178ff1b960befe47fcdec301674a6324"
  integrity sha512-MAb38BcSbH0eHNBxn7ql2NH/kX33OkB3lZ1BNdh7ENeRChHTYsTvWrMubiIAMNS2llXEEgZ1MUOBtXChP3kaFQ==

import-cwd@^2.0.0:
  version "2.1.0"
  resolved "https://registry.yarnpkg.com/import-cwd/-/import-cwd-2.1.0.tgz#aa6cf36e722761285cb371ec6519f53e2435b0a9"
  integrity sha512-Ew5AZzJQFqrOV5BTW3EIoHAnoie1LojZLXKcCQ/yTRyVZosBhK1x1ViYjHGf5pAFOq8ZyChZp6m/fSN7pJyZtg==
  dependencies:
    import-from "^2.1.0"

import-fresh@^2.0.0:
  version "2.0.0"
  resolved "https://registry.yarnpkg.com/import-fresh/-/import-fresh-2.0.0.tgz#d81355c15612d386c61f9ddd3922d4304822a546"
  integrity sha512-eZ5H8rcgYazHbKC3PG4ClHNykCSxtAhxSSEM+2mb+7evD2CKF5V7c0dNum7AdpDh0ZdICwZY9sRSn8f+KH96sg==
  dependencies:
    caller-path "^2.0.0"
    resolve-from "^3.0.0"

import-fresh@^3.0.0, import-fresh@^3.2.1:
  version "3.3.0"
  resolved "https://registry.yarnpkg.com/import-fresh/-/import-fresh-3.3.0.tgz#37162c25fcb9ebaa2e6e53d5b4d88ce17d9e0c2b"
  integrity sha512-veYYhQa+D1QBKznvhUHxb8faxlrwUnxseDAbAp457E0wLNio2bOSKnjYDhMj+YiAq61xrMGhQk9iXVk5FzgQMw==
  dependencies:
    parent-module "^1.0.0"
    resolve-from "^4.0.0"

import-from@^2.1.0:
  version "2.1.0"
  resolved "https://registry.yarnpkg.com/import-from/-/import-from-2.1.0.tgz#335db7f2a7affd53aaa471d4b8021dee36b7f3b1"
  integrity sha512-0vdnLL2wSGnhlRmzHJAg5JHjt1l2vYhzJ7tNLGbeVg0fse56tpGaH0uzH+r9Slej+BSXXEHvBKDEnVSLLE9/+w==
  dependencies:
    resolve-from "^3.0.0"

import-lazy@~4.0.0:
  version "4.0.0"
  resolved "https://registry.yarnpkg.com/import-lazy/-/import-lazy-4.0.0.tgz#e8eb627483a0a43da3c03f3e35548be5cb0cc153"
  integrity sha512-rKtvo6a868b5Hu3heneU+L4yEQ4jYKLtjpnPeUdK7h0yzXGmyBTypknlkCvHFBqfX9YlorEiMM6Dnq/5atfHkw==

imurmurhash@^0.1.4:
  version "0.1.4"
  resolved "https://registry.yarnpkg.com/imurmurhash/-/imurmurhash-0.1.4.tgz#9218b9b2b928a238b13dc4fb6b6d576f231453ea"
  integrity sha512-JmXMZ6wuvDmLiHEml9ykzqO6lwFbof0GG4IkcGaENdCRDDmMVnny7s5HsIgHCbaq0w2MyPhDqkhTUgS2LU2PHA==

inflight@^1.0.4:
  version "1.0.6"
  resolved "https://registry.yarnpkg.com/inflight/-/inflight-1.0.6.tgz#49bd6331d7d02d0c09bc910a1075ba8165b56df9"
  integrity sha512-k92I/b08q4wvFscXCLvqfsHCrjrF7yiXsQuIVvVE7N82W3+aqpzuUdBbfhWcy/FZR3/4IgflMgKLOsvPDrGCJA==
  dependencies:
    once "^1.3.0"
    wrappy "1"

inherits@2, inherits@^2.0.3, inherits@^2.0.4, inherits@~2.0.3:
  version "2.0.4"
  resolved "https://registry.yarnpkg.com/inherits/-/inherits-2.0.4.tgz#0fa2c64f932917c3433a0ded55363aae37416b7c"
  integrity sha512-k/vGaX4/Yla3WzyMCvTQOXYeIHvqOKtnqBduzTHpzpQZzAskKMhZ2K+EnBiSM9zGSoIFeMpXKxa4dYeZIQqewQ==

inline-style-parser@0.1.1:
  version "0.1.1"
  resolved "https://registry.yarnpkg.com/inline-style-parser/-/inline-style-parser-0.1.1.tgz#ec8a3b429274e9c0a1f1c4ffa9453a7fef72cea1"
  integrity sha512-7NXolsK4CAS5+xvdj5OMMbI962hU/wvwoxk+LWR9Ek9bVtyuuYScDN6eS0rUm6TxApFpw7CX1o4uJzcd4AyD3Q==

internal-slot@^1.0.3:
  version "1.0.4"
  resolved "https://registry.yarnpkg.com/internal-slot/-/internal-slot-1.0.4.tgz#8551e7baf74a7a6ba5f749cfb16aa60722f0d6f3"
  integrity sha512-tA8URYccNzMo94s5MQZgH8NB/XTa6HsOo0MLfXTKKEnHVVdegzaQoFZ7Jp44bdvLvY2waT5dc+j5ICEswhi7UQ==
  dependencies:
    get-intrinsic "^1.1.3"
    has "^1.0.3"
    side-channel "^1.0.4"

is-arrayish@^0.2.1:
  version "0.2.1"
  resolved "https://registry.yarnpkg.com/is-arrayish/-/is-arrayish-0.2.1.tgz#77c99840527aa8ecb1a8ba697b80645a7a926a9d"
  integrity sha512-zz06S8t0ozoDXMG+ube26zeCTNXcKIPJZJi8hBrF4idCLms4CG9QtK7qBl1boi5ODzFpjswb5JPmHCbMpjaYzg==

is-arrayish@^0.3.1:
  version "0.3.2"
  resolved "https://registry.yarnpkg.com/is-arrayish/-/is-arrayish-0.3.2.tgz#4574a2ae56f7ab206896fb431eaeed066fdf8f03"
  integrity sha512-eVRqCvVlZbuw3GrM63ovNSNAeA1K16kaR/LRY/92w0zxQ5/1YzwblUX652i4Xs9RwAGjW9d9y6X88t8OaAJfWQ==

is-bigint@^1.0.1:
  version "1.0.4"
  resolved "https://registry.yarnpkg.com/is-bigint/-/is-bigint-1.0.4.tgz#08147a1875bc2b32005d41ccd8291dffc6691df3"
  integrity sha512-zB9CruMamjym81i2JZ3UMn54PKGsQzsJeo6xvN3HJJ4CAsQNB6iRutp2To77OfCNuoxspsIhzaPoO1zyCEhFOg==
  dependencies:
    has-bigints "^1.0.1"

is-binary-path@~2.1.0:
  version "2.1.0"
  resolved "https://registry.yarnpkg.com/is-binary-path/-/is-binary-path-2.1.0.tgz#ea1f7f3b80f064236e83470f86c09c254fb45b09"
  integrity sha512-ZMERYes6pDydyuGidse7OsHxtbI7WVeUEozgR/g7rd0xUimYNlvZRE/K2MgZTjWy725IfelLeVcEM97mmtRGXw==
  dependencies:
    binary-extensions "^2.0.0"

is-boolean-object@^1.1.0:
  version "1.1.2"
  resolved "https://registry.yarnpkg.com/is-boolean-object/-/is-boolean-object-1.1.2.tgz#5c6dc200246dd9321ae4b885a114bb1f75f63719"
  integrity sha512-gDYaKHJmnj4aWxyj6YHyXVpdQawtVLHU5cb+eztPGczf6cjuTdwve5ZIEfgXqH4e57An1D1AKf8CZ3kYrQRqYA==
  dependencies:
    call-bind "^1.0.2"
    has-tostringtag "^1.0.0"

is-buffer@^2.0.0:
  version "2.0.5"
  resolved "https://registry.yarnpkg.com/is-buffer/-/is-buffer-2.0.5.tgz#ebc252e400d22ff8d77fa09888821a24a658c191"
  integrity sha512-i2R6zNFDwgEHJyQUtJEk0XFi1i0dPFn/oqjK3/vPCcDeJvW5NQ83V8QbicfF1SupOaB0h8ntgBC2YiE7dfyctQ==

is-callable@^1.1.4, is-callable@^1.2.7:
  version "1.2.7"
  resolved "https://registry.yarnpkg.com/is-callable/-/is-callable-1.2.7.tgz#3bc2a85ea742d9e36205dcacdd72ca1fdc51b055"
  integrity sha512-1BC0BVFhS/p0qtw6enp8e+8OD0UrK0oFLztSjNzhcKA3WDuJxxAPXzPuPtKkjEY9UUoEWlX/8fgKeu2S8i9JTA==

is-core-module@^2.10.0, is-core-module@^2.8.1, is-core-module@^2.9.0:
  version "2.11.0"
  resolved "https://registry.yarnpkg.com/is-core-module/-/is-core-module-2.11.0.tgz#ad4cb3e3863e814523c96f3f58d26cc570ff0144"
  integrity sha512-RRjxlvLDkD1YJwDbroBHMb+cukurkDWNyHx7D3oNB5x9rb5ogcksMC5wHCadcXoo67gVr/+3GFySh3134zi6rw==
  dependencies:
    has "^1.0.3"

is-date-object@^1.0.1:
  version "1.0.5"
  resolved "https://registry.yarnpkg.com/is-date-object/-/is-date-object-1.0.5.tgz#0841d5536e724c25597bf6ea62e1bd38298df31f"
  integrity sha512-9YQaSxsAiSwcvS33MBk3wTCVnWK+HhF8VZR2jRxehM16QcVOdHqPn4VPHmRK4lSr38n9JriurInLcP90xsYNfQ==
  dependencies:
    has-tostringtag "^1.0.0"

is-directory@^0.3.1:
  version "0.3.1"
  resolved "https://registry.yarnpkg.com/is-directory/-/is-directory-0.3.1.tgz#61339b6f2475fc772fd9c9d83f5c8575dc154ae1"
  integrity sha512-yVChGzahRFvbkscn2MlwGismPO12i9+znNruC5gVEntG3qu0xQMzsGg/JFbrsqDOHtHFPci+V5aP5T9I+yeKqw==

is-docker@^2.0.0, is-docker@^2.1.1:
  version "2.2.1"
  resolved "https://registry.yarnpkg.com/is-docker/-/is-docker-2.2.1.tgz#33eeabe23cfe86f14bde4408a02c0cfb853acdaa"
  integrity sha512-F+i2BKsFrH66iaUFc0woD8sLy8getkwTwtOBjvs56Cx4CgJDeKQeqfz8wAYiSb8JOprWhHH5p77PbmYCvvUuXQ==

is-extendable@^0.1.0:
  version "0.1.1"
  resolved "https://registry.yarnpkg.com/is-extendable/-/is-extendable-0.1.1.tgz#62b110e289a471418e3ec36a617d472e301dfc89"
  integrity sha512-5BMULNob1vgFX6EjQw5izWDxrecWK9AM72rugNr0TFldMOi0fj6Jk+zeKIt0xGj4cEfQIJth4w3OKWOJ4f+AFw==

is-extglob@^2.1.1:
  version "2.1.1"
  resolved "https://registry.yarnpkg.com/is-extglob/-/is-extglob-2.1.1.tgz#a88c02535791f02ed37c76a1b9ea9773c833f8c2"
  integrity sha512-SbKbANkN603Vi4jEZv49LeVJMn4yGwsbzZworEoyEiutsN3nJYdbO36zfhGJ6QEDpOZIFkDtnq5JRxmvl3jsoQ==

is-fullwidth-code-point@^1.0.0:
  version "1.0.0"
  resolved "https://registry.yarnpkg.com/is-fullwidth-code-point/-/is-fullwidth-code-point-1.0.0.tgz#ef9e31386f031a7f0d643af82fde50c457ef00cb"
  integrity sha512-1pqUqRjkhPJ9miNq9SwMfdvi6lBJcd6eFxvfaivQhaH3SgisfiuudvFntdKOmxuee/77l+FPjKrQjWvmPjWrRw==
  dependencies:
    number-is-nan "^1.0.0"

is-fullwidth-code-point@^3.0.0:
  version "3.0.0"
  resolved "https://registry.yarnpkg.com/is-fullwidth-code-point/-/is-fullwidth-code-point-3.0.0.tgz#f116f8064fe90b3f7844a38997c0b75051269f1d"
  integrity sha512-zymm5+u+sCsSWyD9qNaejV3DFvhCKclKdizYaJUuHA83RLjb7nSuGnddCHGv0hk+KY7BMAlsWeK4Ueg6EV6XQg==

is-glob@^4.0.0, is-glob@^4.0.1, is-glob@^4.0.3, is-glob@~4.0.1:
  version "4.0.3"
  resolved "https://registry.yarnpkg.com/is-glob/-/is-glob-4.0.3.tgz#64f61e42cbbb2eec2071a9dac0b28ba1e65d5084"
  integrity sha512-xelSayHH36ZgE7ZWhli7pW34hNbNl8Ojv5KVmkJD4hBdD3th8Tfk9vYasLM+mXWOZhFkgZfxhLSnrwRr4elSSg==
  dependencies:
    is-extglob "^2.1.1"

is-negative-zero@^2.0.2:
  version "2.0.2"
  resolved "https://registry.yarnpkg.com/is-negative-zero/-/is-negative-zero-2.0.2.tgz#7bf6f03a28003b8b3965de3ac26f664d765f3150"
  integrity sha512-dqJvarLawXsFbNDeJW7zAz8ItJ9cd28YufuuFzh0G8pNHjJMnY08Dv7sYX2uF5UpQOwieAeOExEYAWWfu7ZZUA==

is-number-object@^1.0.4:
  version "1.0.7"
  resolved "https://registry.yarnpkg.com/is-number-object/-/is-number-object-1.0.7.tgz#59d50ada4c45251784e9904f5246c742f07a42fc"
  integrity sha512-k1U0IRzLMo7ZlYIfzRu23Oh6MiIFasgpb9X76eqfFZAqwH44UI4KTBvBYIZ1dSL9ZzChTB9ShHfLkR4pdW5krQ==
  dependencies:
    has-tostringtag "^1.0.0"

is-number@^7.0.0:
  version "7.0.0"
  resolved "https://registry.yarnpkg.com/is-number/-/is-number-7.0.0.tgz#7535345b896734d5f80c4d06c50955527a14f12b"
  integrity sha512-41Cifkg6e8TylSpdtTpeLVMqvSBEVzTttHvERD741+pnZ8ANv0004MRL43QKPDlK9cGvNp6NZWZUBlbGXYxxng==

is-path-inside@^3.0.3:
  version "3.0.3"
  resolved "https://registry.yarnpkg.com/is-path-inside/-/is-path-inside-3.0.3.tgz#d231362e53a07ff2b0e0ea7fed049161ffd16283"
  integrity sha512-Fd4gABb+ycGAmKou8eMftCupSir5lRxqf4aD/vd0cD2qc4HL07OjCeuHMr8Ro4CoMaeCKDB0/ECBOVWjTwUvPQ==

is-plain-obj@^4.0.0:
  version "4.1.0"
  resolved "https://registry.yarnpkg.com/is-plain-obj/-/is-plain-obj-4.1.0.tgz#d65025edec3657ce032fd7db63c97883eaed71f0"
  integrity sha512-+Pgi+vMuUNkJyExiMBt5IlFoMyKnr5zhJ4Uspz58WOhBF5QoIZkFyNHIbBAtHwzVAgk5RtndVNsDRN61/mmDqg==

is-regex@^1.1.4:
  version "1.1.4"
  resolved "https://registry.yarnpkg.com/is-regex/-/is-regex-1.1.4.tgz#eef5663cd59fa4c0ae339505323df6854bb15958"
  integrity sha512-kvRdxDsxZjhzUX07ZnLydzS1TU/TJlTUHHY4YLL87e37oUA49DfkLqgy+VjFocowy29cKvcSiu+kIv728jTTVg==
  dependencies:
    call-bind "^1.0.2"
    has-tostringtag "^1.0.0"

is-shared-array-buffer@^1.0.2:
  version "1.0.2"
  resolved "https://registry.yarnpkg.com/is-shared-array-buffer/-/is-shared-array-buffer-1.0.2.tgz#8f259c573b60b6a32d4058a1a07430c0a7344c79"
  integrity sha512-sqN2UDu1/0y6uvXyStCOzyhAjCSlHceFoMKJW8W9EU9cvic/QdsZ0kEU93HEy3IUEFZIiH/3w+AH/UQbPHNdhA==
  dependencies:
    call-bind "^1.0.2"

is-ssh@^1.4.0:
  version "1.4.0"
  resolved "https://registry.yarnpkg.com/is-ssh/-/is-ssh-1.4.0.tgz#4f8220601d2839d8fa624b3106f8e8884f01b8b2"
  integrity sha512-x7+VxdxOdlV3CYpjvRLBv5Lo9OJerlYanjwFrPR9fuGPjCiNiCzFgAWpiLAohSbsnH4ZAys3SBh+hq5rJosxUQ==
  dependencies:
    protocols "^2.0.1"

is-stream@^2.0.0:
  version "2.0.1"
  resolved "https://registry.yarnpkg.com/is-stream/-/is-stream-2.0.1.tgz#fac1e3d53b97ad5a9d0ae9cef2389f5810a5c077"
  integrity sha512-hFoiJiTl63nn+kstHGBtewWSKnQLpyb155KHheA1l39uvtO9nWIop1p3udqPcUd/xbF1VLMO4n7OI6p7RbngDg==

is-string@^1.0.5, is-string@^1.0.7:
  version "1.0.7"
  resolved "https://registry.yarnpkg.com/is-string/-/is-string-1.0.7.tgz#0dd12bf2006f255bb58f695110eff7491eebc0fd"
  integrity sha512-tE2UXzivje6ofPW7l23cjDOMa09gb7xlAqG6jG5ej6uPV32TlWP3NKPigtaGeHNu9fohccRYvIiZMfOOnOYUtg==
  dependencies:
    has-tostringtag "^1.0.0"

is-symbol@^1.0.2, is-symbol@^1.0.3:
  version "1.0.4"
  resolved "https://registry.yarnpkg.com/is-symbol/-/is-symbol-1.0.4.tgz#a6dac93b635b063ca6872236de88910a57af139c"
  integrity sha512-C/CPBqKWnvdcxqIARxyOh4v1UUEOCHpgDa0WYgpKDFMszcrPcffg5uhwSgPCLD2WWxmq6isisz87tzT01tuGhg==
  dependencies:
    has-symbols "^1.0.2"

is-url@^1.2.4:
  version "1.2.4"
  resolved "https://registry.yarnpkg.com/is-url/-/is-url-1.2.4.tgz#04a4df46d28c4cff3d73d01ff06abeb318a1aa52"
  integrity sha512-ITvGim8FhRiYe4IQ5uHSkj7pVaPDrCTkNd3yq3cV7iZAcJdHTUMPMEHcqSOy9xZ9qFenQCvi+2wjH9a1nXqHww==

is-weakref@^1.0.2:
  version "1.0.2"
  resolved "https://registry.yarnpkg.com/is-weakref/-/is-weakref-1.0.2.tgz#9529f383a9338205e89765e0392efc2f100f06f2"
  integrity sha512-qctsuLZmIQ0+vSSMfoVvyFe2+GSEvnmZ2ezTup1SBse9+twCCeial6EEi3Nc2KFcf6+qz2FBPnjXsk8xhKSaPQ==
  dependencies:
    call-bind "^1.0.2"

is-wsl@^2.2.0:
  version "2.2.0"
  resolved "https://registry.yarnpkg.com/is-wsl/-/is-wsl-2.2.0.tgz#74a4c76e77ca9fd3f932f290c17ea326cd157271"
  integrity sha512-fKzAra0rGJUUBwGBgNkHZuToZcn+TtXHpeCgmkMJMMYx1sQDYaCSyjJBSCa2nH1DGm7s3n1oBnohoVTBaN7Lww==
  dependencies:
    is-docker "^2.0.0"

isarray@~1.0.0:
  version "1.0.0"
  resolved "https://registry.yarnpkg.com/isarray/-/isarray-1.0.0.tgz#bb935d48582cba168c06834957a54a3e07124f11"
  integrity sha512-VLghIWNM6ELQzo7zwmcg0NmTVyWKYjvIeM83yjp0wRDTmUnrM678fQbcKBo6n2CJEF0szoG//ytg+TKla89ALQ==

isexe@^2.0.0:
  version "2.0.0"
  resolved "https://registry.yarnpkg.com/isexe/-/isexe-2.0.0.tgz#e8fbf374dc556ff8947a10dcb0572d633f2cfa10"
  integrity sha512-RHxMLp9lnKHGHRng9QFhRCMbYAcVpn69smSGcq3f36xjgVVWThj4qqLbTLlq7Ssj8B+fIQ1EuCEGI2lKsyQeIw==

javascript-stringify@^2.0.1:
  version "2.1.0"
  resolved "https://registry.yarnpkg.com/javascript-stringify/-/javascript-stringify-2.1.0.tgz#27c76539be14d8bd128219a2d731b09337904e79"
  integrity sha512-JVAfqNPTvNq3sB/VHQJAFxN/sPgKnsKrCwyRt15zwNCdrMMJDdcEOdubuy+DuJYYdm0ox1J4uzEuYKkN+9yhVg==

jju@^1.4.0, jju@~1.4.0:
  version "1.4.0"
  resolved "https://registry.yarnpkg.com/jju/-/jju-1.4.0.tgz#a3abe2718af241a2b2904f84a625970f389ae32a"
  integrity sha512-8wb9Yw966OSxApiCt0K3yNJL8pnNeIv+OEq2YMidz4FKP6nonSRoOXc80iXY4JaN2FC11B9qsNmDsm+ZOfMROA==

js-sdsl@^4.1.4:
  version "4.2.0"
  resolved "https://registry.yarnpkg.com/js-sdsl/-/js-sdsl-4.2.0.tgz#278e98b7bea589b8baaf048c20aeb19eb7ad09d0"
  integrity sha512-dyBIzQBDkCqCu+0upx25Y2jGdbTGxE9fshMsCdK0ViOongpV+n5tXRcZY9v7CaVQ79AGS9KA1KHtojxiM7aXSQ==

"js-tokens@^3.0.0 || ^4.0.0", js-tokens@^4.0.0:
  version "4.0.0"
  resolved "https://registry.yarnpkg.com/js-tokens/-/js-tokens-4.0.0.tgz#19203fb59991df98e3a287050d4647cdeaf32499"
  integrity sha512-RdJUflcE3cUzKiMqQgsCu06FPu9UdIJO0beYbPhHN4k6apgJtifcoCtT9bcxOpYBtpD2kCM6Sbzg4CausW/PKQ==

js-yaml@^3.13.1:
  version "3.14.1"
  resolved "https://registry.yarnpkg.com/js-yaml/-/js-yaml-3.14.1.tgz#dae812fdb3825fa306609a8717383c50c36a0537"
  integrity sha512-okMH7OXXJ7YrN9Ok3/SXrnu4iX9yOk+25nqX4imS2npuvTYDmo/QEZoqwZkYaIDk3jVvBOTOIEgEhaLOynBS9g==
  dependencies:
    argparse "^1.0.7"
    esprima "^4.0.0"

js-yaml@^4.1.0:
  version "4.1.0"
  resolved "https://registry.yarnpkg.com/js-yaml/-/js-yaml-4.1.0.tgz#c1fb65f8f5017901cdd2c951864ba18458a10602"
  integrity sha512-wpxZs9NoxZaJESJGIZTyDEaYpl0FKSA+FB9aJiyemKhMwkxQg63h4T1KJgUGHpTqPDNRcmmYLugrRjJlBtWvRA==
  dependencies:
    argparse "^2.0.1"

jsesc@^2.5.1:
  version "2.5.2"
  resolved "https://registry.yarnpkg.com/jsesc/-/jsesc-2.5.2.tgz#80564d2e483dacf6e8ef209650a67df3f0c283a4"
  integrity sha512-OYu7XEzjkCQ3C5Ps3QIZsQfNpqoJyZZA99wd9aWd05NCtC5pWOkShK2mkL6HXQR6/Cy2lbNdPlZBpuQHXE63gA==

jsesc@~0.5.0:
  version "0.5.0"
  resolved "https://registry.yarnpkg.com/jsesc/-/jsesc-0.5.0.tgz#e7dee66e35d6fc16f710fe91d5cf69f70f08911d"
  integrity sha512-uZz5UnB7u4T9LvwmFqXii7pZSouaRPorGs5who1Ip7VO0wxanFvBL7GkM6dTHlgX+jhBApRetaWpnDabOeTcnA==

json-parse-better-errors@^1.0.1:
  version "1.0.2"
  resolved "https://registry.yarnpkg.com/json-parse-better-errors/-/json-parse-better-errors-1.0.2.tgz#bb867cfb3450e69107c131d1c514bab3dc8bcaa9"
  integrity sha512-mrqyZKfX5EhL7hvqcV6WG1yYjnjeuYDzDhhcAAUrq8Po85NBQBJP+ZDUT75qZQ98IkUoBqdkExkukOU7Ts2wrw==

json-parse-even-better-errors@^2.3.0:
  version "2.3.1"
  resolved "https://registry.yarnpkg.com/json-parse-even-better-errors/-/json-parse-even-better-errors-2.3.1.tgz#7c47805a94319928e05777405dc12e1f7a4ee02d"
  integrity sha512-xyFwyhro/JEof6Ghe2iz2NcXoj2sloNsWr/XsERDK/oiPCfaNhl5ONfp+jQdAZRQQ0IJWNzH9zIZF7li91kh2w==

json-schema-traverse@^0.4.1:
  version "0.4.1"
  resolved "https://registry.yarnpkg.com/json-schema-traverse/-/json-schema-traverse-0.4.1.tgz#69f6a87d9513ab8bb8fe63bdb0979c448e684660"
  integrity sha512-xbbCH5dCYU5T8LcEhhuh7HJ88HXuW3qsI3Y0zOZFKfZEHcpWiHU/Jxzk629Brsab/mMiHQti9wMP+845RPe3Vg==

json-stable-stringify-without-jsonify@^1.0.1:
  version "1.0.1"
  resolved "https://registry.yarnpkg.com/json-stable-stringify-without-jsonify/-/json-stable-stringify-without-jsonify-1.0.1.tgz#9db7b59496ad3f3cfef30a75142d2d930ad72651"
  integrity sha512-Bdboy+l7tA3OGW6FjyFHWkP5LuByj1Tk33Ljyq0axyzdk9//JSi2u3fP1QSmd1KNwq6VOKYGlAu87CisVir6Pw==

json5@^1.0.1, json5@^2.1.2, json5@^2.2.1, json5@^2.2.2:
  version "2.2.3"
  resolved "https://registry.yarnpkg.com/json5/-/json5-2.2.3.tgz#78cd6f1a19bdc12b73db5ad0c61efd66c1e29283"
  integrity sha512-XmOWe7eyHYH14cLdVPoyg+GOH3rYX++KpzrylJwSW98t3Nk+U8XOl8FWKOgwtzdb8lXGf6zYwDUzeHMWfxasyg==

jsonfile@^4.0.0:
  version "4.0.0"
  resolved "https://registry.yarnpkg.com/jsonfile/-/jsonfile-4.0.0.tgz#8771aae0799b64076b76640fca058f9c10e33ecb"
  integrity sha512-m6F1R3z8jjlf2imQHS2Qez5sjKWQzbuuhuJ/FKYFRZvPE3PuHcSMVZzfsLhGVOkfd20obL5SWEBew5ShlquNxg==
  optionalDependencies:
    graceful-fs "^4.1.6"

"jsx-ast-utils@^2.4.1 || ^3.0.0", jsx-ast-utils@^3.3.2:
  version "3.3.3"
  resolved "https://registry.yarnpkg.com/jsx-ast-utils/-/jsx-ast-utils-3.3.3.tgz#76b3e6e6cece5c69d49a5792c3d01bd1a0cdc7ea"
  integrity sha512-fYQHZTZ8jSfmWZ0iyzfwiU4WDX4HpHbMCZ3gPlWYiCl3BoeOTsqKBqnTVfH2rYT7eP5c3sVbeSPHnnJOaTrWiw==
  dependencies:
    array-includes "^3.1.5"
    object.assign "^4.1.3"

katex@^0.16.4:
  version "0.16.4"
  resolved "https://registry.yarnpkg.com/katex/-/katex-0.16.4.tgz#87021bc3bbd80586ef715aeb476794cba6a49ad4"
  integrity sha512-WudRKUj8yyBeVDI4aYMNxhx5Vhh2PjpzQw1GRu/LVGqL4m1AxwD1GcUp0IMbdJaf5zsjtj8ghP0DOQRYhroNkw==
  dependencies:
    commander "^8.0.0"

kind-of@^6.0.0, kind-of@^6.0.2:
  version "6.0.3"
  resolved "https://registry.yarnpkg.com/kind-of/-/kind-of-6.0.3.tgz#07c05034a6c349fa06e24fa35aa76db4580ce4dd"
  integrity sha512-dcS1ul+9tmeD95T+x28/ehLgd9mENa3LsvDTtzm3vyBEO7RPptvAD+t44WVXaUjTBRcrpFeFlC8WCruUR456hw==

kleur@^4.0.3:
  version "4.1.5"
  resolved "https://registry.yarnpkg.com/kleur/-/kleur-4.1.5.tgz#95106101795f7050c6c650f350c683febddb1780"
  integrity sha512-o+NO+8WrRiQEE4/7nwRJhN1HWpVmJm511pBHUxPLtp0BUISzlBplORYSmTclCnJvQq2tKu/sgl3xVpkc7ZWuQQ==

lage@^1.9.6:
  version "1.9.6"
  resolved "https://registry.yarnpkg.com/lage/-/lage-1.9.6.tgz#8c4cf0ef05d5e8416fcdd25f16501a11c45fff83"
  integrity sha512-pTVolv+UPl8t3Go/KD5MolbC7gwRtWQSIQY68rOcVxi7O+je5mDDpP9Uoy2h7yUiWbua+OBFu5gWgUKhMZKRvw==
  dependencies:
    "@xmldom/xmldom" "^0.8.0"
    abort-controller "^3.0.0"
    backfill "^6.1.21"
    backfill-cache "^5.6.1"
    backfill-config "^6.3.0"
    backfill-logger "^5.1.3"
    chalk "^4.0.0"
    cosmiconfig "^7.0.0"
    execa "5.1.1"
    fast-glob "^3.2.11"
    npmlog "^4.1.2"
    p-graph "^1.1.1"
    p-profiler "^0.2.1"
    workspace-tools "^0.29.0"
    yargs-parser "^18.1.3"

language-subtag-registry@^0.3.20:
  version "0.3.22"
  resolved "https://registry.yarnpkg.com/language-subtag-registry/-/language-subtag-registry-0.3.22.tgz#2e1500861b2e457eba7e7ae86877cbd08fa1fd1d"
  integrity sha512-tN0MCzyWnoz/4nHS6uxdlFWoUZT7ABptwKPQ52Ea7URk6vll88bWBVhodtnlfEuCcKWNGoc+uGbw1cwa9IKh/w==

language-tags@^1.0.5:
  version "1.0.7"
  resolved "https://registry.yarnpkg.com/language-tags/-/language-tags-1.0.7.tgz#41cc248730f3f12a452c2e2efe32bc0bbce67967"
  integrity sha512-bSytju1/657hFjgUzPAPqszxH62ouE8nQFoFaVlIQfne4wO/wXC9A4+m8jYve7YBBvi59eq0SUpcshvG8h5Usw==
  dependencies:
    language-subtag-registry "^0.3.20"

levn@^0.4.1:
  version "0.4.1"
  resolved "https://registry.yarnpkg.com/levn/-/levn-0.4.1.tgz#ae4562c007473b932a6200d403268dd2fffc6ade"
  integrity sha512-+bT2uH4E5LGE7h/n3evcS/sQlJXCpIp6ym8OWJ5eV6+67Dsql/LaaT7qJBAt2rzfoa/5QBGBhxDix1dMt2kQKQ==
  dependencies:
    prelude-ls "^1.2.1"
    type-check "~0.4.0"

lilconfig@^2.0.5, lilconfig@^2.0.6:
  version "2.0.6"
  resolved "https://registry.yarnpkg.com/lilconfig/-/lilconfig-2.0.6.tgz#32a384558bd58af3d4c6e077dd1ad1d397bc69d4"
  integrity sha512-9JROoBW7pobfsx+Sq2JsASvCo6Pfo6WWoUW79HuB1BCoBXD4PLWJPqDF6fNj67pqBYTbAHkE57M1kS/+L1neOg==

lines-and-columns@^1.1.6:
  version "1.2.4"
  resolved "https://registry.yarnpkg.com/lines-and-columns/-/lines-and-columns-1.2.4.tgz#eca284f75d2965079309dc0ad9255abb2ebc1632"
  integrity sha512-7ylylesZQ/PV29jhEDl3Ufjo6ZX7gCqJr5F7PKrqc93v7fzSymt1BpwEU8nAUXs8qzzvqhbjhK5QZg6Mt/HkBg==

linkify-it@^4.0.1:
  version "4.0.1"
  resolved "https://registry.yarnpkg.com/linkify-it/-/linkify-it-4.0.1.tgz#01f1d5e508190d06669982ba31a7d9f56a5751ec"
  integrity sha512-C7bfi1UZmoj8+PQx22XyeXCuBlokoyWQL5pWSP+EI6nzRylyThouddufc2c1NDIcP9k5agmN9fLpA7VNJfIiqw==
  dependencies:
    uc.micro "^1.0.1"

loader-utils@^2.0.0:
  version "2.0.4"
  resolved "https://registry.yarnpkg.com/loader-utils/-/loader-utils-2.0.4.tgz#8b5cb38b5c34a9a018ee1fc0e6a066d1dfcc528c"
  integrity sha512-xXqpXoINfFhgua9xiqD8fPFHgkoq1mmmpE92WlDbm9rNRd/EbRb+Gqf908T2DMfuHjjJlksiK2RbHVOdD/MqSw==
  dependencies:
    big.js "^5.2.2"
    emojis-list "^3.0.0"
    json5 "^2.1.2"

locate-path@^5.0.0:
  version "5.0.0"
  resolved "https://registry.yarnpkg.com/locate-path/-/locate-path-5.0.0.tgz#1afba396afd676a6d42504d0a67a3a7eb9f62aa0"
  integrity sha512-t7hw9pI+WvuwNJXwk5zVHpyhIqzg2qTlklJOf0mVxGSbe3Fp2VieZcduNYjaLDoy6p9uGpQEGWG87WpMKlNq8g==
  dependencies:
    p-locate "^4.1.0"

locate-path@^6.0.0:
  version "6.0.0"
  resolved "https://registry.yarnpkg.com/locate-path/-/locate-path-6.0.0.tgz#55321eb309febbc59c4801d931a72452a681d286"
  integrity sha512-iPZK6eYjbxRu3uB4/WZ3EsEIMJFMqAoopl3R+zuq0UjcAm/MO6KCweDgPfP3elTztoKP3KtnVHxTn2NHBSDVUw==
  dependencies:
    p-locate "^5.0.0"

lodash.assign@^4.2.0:
  version "4.2.0"
  resolved "https://registry.yarnpkg.com/lodash.assign/-/lodash.assign-4.2.0.tgz#0d99f3ccd7a6d261d19bdaeb9245005d285808e7"
  integrity sha512-hFuH8TY+Yji7Eja3mGiuAxBqLagejScbG8GbG0j6o9vzn0YL14My+ktnqtZgFTosKymC9/44wP6s7xyuLfnClw==

lodash.debounce@^4.0.8:
  version "4.0.8"
  resolved "https://registry.yarnpkg.com/lodash.debounce/-/lodash.debounce-4.0.8.tgz#82d79bff30a67c4005ffd5e2515300ad9ca4d7af"
  integrity sha512-FT1yDzDYEoYWhnSGnpE/4Kj1fLZkDFyqRb7fNt6FdYOSxlUWAtp42Eh6Wb0rGIv/m9Bgo7x4GhQbm5Ys4SG5ow==

lodash.get@^4.4.2:
  version "4.4.2"
  resolved "https://registry.yarnpkg.com/lodash.get/-/lodash.get-4.4.2.tgz#2d177f652fa31e939b4438d5341499dfa3825e99"
  integrity sha512-z+Uw/vLuy6gQe8cfaFWD7p0wVv8fJl3mbzXh33RS+0oW2wvUqiRXiQ69gLWSLpgB5/6sU+r6BlQR0MBILadqTQ==

lodash.isequal@^4.5.0:
  version "4.5.0"
  resolved "https://registry.yarnpkg.com/lodash.isequal/-/lodash.isequal-4.5.0.tgz#415c4478f2bcc30120c22ce10ed3226f7d3e18e0"
  integrity sha512-pDo3lu8Jhfjqls6GkMgpahsF9kCyayhgykjyLMNFTKWrpVdAQtYyB4muAMWozBB4ig/dtWAmsMxLEI8wuz+DYQ==

lodash.kebabcase@^4.1.1:
  version "4.1.1"
  resolved "https://registry.yarnpkg.com/lodash.kebabcase/-/lodash.kebabcase-4.1.1.tgz#8489b1cb0d29ff88195cceca448ff6d6cc295c36"
  integrity sha512-N8XRTIMMqqDgSy4VLKPnJ/+hpGZN+PHQiJnSenYqPaVV/NCqEogTnAdZLQiGKhxX+JCs8waWq2t1XHWKOmlY8g==

lodash.merge@^4.6.2:
  version "4.6.2"
  resolved "https://registry.yarnpkg.com/lodash.merge/-/lodash.merge-4.6.2.tgz#558aa53b43b661e1925a0afdfa36a9a1085fe57a"
  integrity sha512-0KpjqXRVvrYyCsX1swR/XTK0va6VQkQM6MNo7PqW77ByjAhoARA8EfrP1N4+KlKj8YS0ZUCtRT/YUuhyYDujIQ==

lodash.trim@^4.5.1:
  version "4.5.1"
  resolved "https://registry.yarnpkg.com/lodash.trim/-/lodash.trim-4.5.1.tgz#36425e7ee90be4aa5e27bcebb85b7d11ea47aa57"
  integrity sha512-nJAlRl/K+eiOehWKDzoBVrSMhK0K3A3YQsUNXHQa5yIrKBAhsZgSu3KoAFoFT+mEgiyBHddZ0pRk1ITpIp90Wg==

lodash@^4.17.20:
  version "4.17.21"
  resolved "https://registry.yarnpkg.com/lodash/-/lodash-4.17.21.tgz#679591c564c3bffaae8454cf0b3df370c3d6911c"
  integrity sha512-v2kDEe57lecTulaDIuNTPy3Ry4gLGJ6Z1O3vE1krgXZNrsQ+LFTGHVxVjcXPs17LhbZVGedAJv8XZ1tvj5FvSg==

longest-streak@^3.0.0:
  version "3.1.0"
  resolved "https://registry.yarnpkg.com/longest-streak/-/longest-streak-3.1.0.tgz#62fa67cd958742a1574af9f39866364102d90cd4"
  integrity sha512-9Ri+o0JYgehTaVBBDoMqIl8GXtbWg711O3srftcHhZ0dqnETqLaoIK0x17fUw9rFSlK/0NlsKe0Ahhyl5pXE2g==

loose-envify@^1.1.0, loose-envify@^1.4.0:
  version "1.4.0"
  resolved "https://registry.yarnpkg.com/loose-envify/-/loose-envify-1.4.0.tgz#71ee51fa7be4caec1a63839f7e682d8132d30caf"
  integrity sha512-lyuxPGr/Wfhrlem2CL/UcnUc1zcqKAImBDzukY7Y5F/yQiNdko6+fRLevlw1HgMySw7f611UIY408EtxRSoK3Q==
  dependencies:
    js-tokens "^3.0.0 || ^4.0.0"

lru-cache@^5.1.1:
  version "5.1.1"
  resolved "https://registry.yarnpkg.com/lru-cache/-/lru-cache-5.1.1.tgz#1da27e6710271947695daf6848e847f01d84b920"
  integrity sha512-KpNARQA3Iwv+jTA0utUVVbrh+Jlrr1Fv0e56GGzAFOXN7dk/FviaDW8LHmK52DlcH4WP2n6gI8vN1aesBFgo9w==
  dependencies:
    yallist "^3.0.2"

lru-cache@^6.0.0:
  version "6.0.0"
  resolved "https://registry.yarnpkg.com/lru-cache/-/lru-cache-6.0.0.tgz#6d6fe6570ebd96aaf90fcad1dafa3b2566db3a94"
  integrity sha512-Jo6dJ04CmSjuznwJSS3pUeWmd/H0ffTlkXXgwZi+eq1UCmqQwCh+eLsYOYCwY991i2Fah4h1BEMCx4qThGbsiA==
  dependencies:
    yallist "^4.0.0"

make-dir@~3.1.0:
  version "3.1.0"
  resolved "https://registry.yarnpkg.com/make-dir/-/make-dir-3.1.0.tgz#415e967046b3a7f1d185277d84aa58203726a13f"
  integrity sha512-g3FeP20LNwhALb/6Cz6Dd4F2ngze0jz7tbzrD2wAV+o9FeNHe4rL+yK2md0J/fiSf1sa1ADhXqi5+oVwOM/eGw==
  dependencies:
    semver "^6.0.0"

markdown-it-front-matter@^0.2.3:
  version "0.2.3"
  resolved "https://registry.yarnpkg.com/markdown-it-front-matter/-/markdown-it-front-matter-0.2.3.tgz#d6fa0f4b362e02086dd4ce8219fadf3f4c9cfa37"
  integrity sha512-s9+rcClLmZsZc3YL8Awjg/YO/VdphlE20LJ9Bx5a8RAFLI5a1vq6Mll8kOzG6w/wy8yhFLBupaa6Mfd60GATkA==

markdown-it@^13.0.1:
  version "13.0.1"
  resolved "https://registry.yarnpkg.com/markdown-it/-/markdown-it-13.0.1.tgz#c6ecc431cacf1a5da531423fc6a42807814af430"
  integrity sha512-lTlxriVoy2criHP0JKRhO2VDG9c2ypWCsT237eDiLqi09rmbKoUetyGHq2uOIRoRS//kfoJckS0eUzzkDR+k2Q==
  dependencies:
    argparse "^2.0.1"
    entities "~3.0.1"
    linkify-it "^4.0.1"
    mdurl "^1.0.1"
    uc.micro "^1.0.5"

markdown-table@^3.0.0:
  version "3.0.3"
  resolved "https://registry.yarnpkg.com/markdown-table/-/markdown-table-3.0.3.tgz#e6331d30e493127e031dd385488b5bd326e4a6bd"
  integrity sha512-Z1NL3Tb1M9wH4XESsCDEksWoKTdlUafKc4pt0GRwjUyXaCFZ+dc3g2erqB6zm3szA2IUSi7VnPI+o/9jnxh9hw==

mathjax-full@^3.2.2:
  version "3.2.2"
  resolved "https://registry.yarnpkg.com/mathjax-full/-/mathjax-full-3.2.2.tgz#43f02e55219db393030985d2b6537ceae82f1fa7"
  integrity sha512-+LfG9Fik+OuI8SLwsiR02IVdjcnRCy5MufYLi0C3TdMT56L/pjB0alMVGgoWJF8pN9Rc7FESycZB9BMNWIid5w==
  dependencies:
    esm "^3.2.25"
    mhchemparser "^4.1.0"
    mj-context-menu "^0.6.1"
    speech-rule-engine "^4.0.6"

mdast-util-definitions@^5.0.0:
  version "5.1.1"
  resolved "https://registry.yarnpkg.com/mdast-util-definitions/-/mdast-util-definitions-5.1.1.tgz#2c1d684b28e53f84938bb06317944bee8efa79db"
  integrity sha512-rQ+Gv7mHttxHOBx2dkF4HWTg+EE+UR78ptQWDylzPKaQuVGdG4HIoY3SrS/pCp80nZ04greFvXbVFHT+uf0JVQ==
  dependencies:
    "@types/mdast" "^3.0.0"
    "@types/unist" "^2.0.0"
    unist-util-visit "^4.0.0"

mdast-util-find-and-replace@^2.0.0:
  version "2.2.1"
  resolved "https://registry.yarnpkg.com/mdast-util-find-and-replace/-/mdast-util-find-and-replace-2.2.1.tgz#249901ef43c5f41d6e8a8d446b3b63b17e592d7c"
  integrity sha512-SobxkQXFAdd4b5WmEakmkVoh18icjQRxGy5OWTCzgsLRm1Fu/KCtwD1HIQSsmq5ZRjVH0Ehwg6/Fn3xIUk+nKw==
  dependencies:
    escape-string-regexp "^5.0.0"
    unist-util-is "^5.0.0"
    unist-util-visit-parents "^5.0.0"

mdast-util-from-markdown@^1.0.0:
  version "1.2.0"
  resolved "https://registry.yarnpkg.com/mdast-util-from-markdown/-/mdast-util-from-markdown-1.2.0.tgz#84df2924ccc6c995dec1e2368b2b208ad0a76268"
  integrity sha512-iZJyyvKD1+K7QX1b5jXdE7Sc5dtoTry1vzV28UZZe8Z1xVnB/czKntJ7ZAkG0tANqRnBF6p3p7GpU1y19DTf2Q==
  dependencies:
    "@types/mdast" "^3.0.0"
    "@types/unist" "^2.0.0"
    decode-named-character-reference "^1.0.0"
    mdast-util-to-string "^3.1.0"
    micromark "^3.0.0"
    micromark-util-decode-numeric-character-reference "^1.0.0"
    micromark-util-decode-string "^1.0.0"
    micromark-util-normalize-identifier "^1.0.0"
    micromark-util-symbol "^1.0.0"
    micromark-util-types "^1.0.0"
    unist-util-stringify-position "^3.0.0"
    uvu "^0.5.0"

mdast-util-gfm-autolink-literal@^1.0.0:
  version "1.0.2"
  resolved "https://registry.yarnpkg.com/mdast-util-gfm-autolink-literal/-/mdast-util-gfm-autolink-literal-1.0.2.tgz#4032dcbaddaef7d4f2f3768ed830475bb22d3970"
  integrity sha512-FzopkOd4xTTBeGXhXSBU0OCDDh5lUj2rd+HQqG92Ld+jL4lpUfgX2AT2OHAVP9aEeDKp7G92fuooSZcYJA3cRg==
  dependencies:
    "@types/mdast" "^3.0.0"
    ccount "^2.0.0"
    mdast-util-find-and-replace "^2.0.0"
    micromark-util-character "^1.0.0"

mdast-util-gfm-footnote@^1.0.0:
  version "1.0.1"
  resolved "https://registry.yarnpkg.com/mdast-util-gfm-footnote/-/mdast-util-gfm-footnote-1.0.1.tgz#11d2d40a1a673a399c459e467fa85e00223191fe"
  integrity sha512-p+PrYlkw9DeCRkTVw1duWqPRHX6Ywh2BNKJQcZbCwAuP/59B0Lk9kakuAd7KbQprVO4GzdW8eS5++A9PUSqIyw==
  dependencies:
    "@types/mdast" "^3.0.0"
    mdast-util-to-markdown "^1.3.0"
    micromark-util-normalize-identifier "^1.0.0"

mdast-util-gfm-strikethrough@^1.0.0:
  version "1.0.2"
  resolved "https://registry.yarnpkg.com/mdast-util-gfm-strikethrough/-/mdast-util-gfm-strikethrough-1.0.2.tgz#6b4fa4ae37d449ccb988192ac0afbb2710ffcefd"
  integrity sha512-T/4DVHXcujH6jx1yqpcAYYwd+z5lAYMw4Ls6yhTfbMMtCt0PHY4gEfhW9+lKsLBtyhUGKRIzcUA2FATVqnvPDA==
  dependencies:
    "@types/mdast" "^3.0.0"
    mdast-util-to-markdown "^1.3.0"

mdast-util-gfm-table@^1.0.0:
  version "1.0.6"
  resolved "https://registry.yarnpkg.com/mdast-util-gfm-table/-/mdast-util-gfm-table-1.0.6.tgz#184e900979fe790745fc3dabf77a4114595fcd7f"
  integrity sha512-uHR+fqFq3IvB3Rd4+kzXW8dmpxUhvgCQZep6KdjsLK4O6meK5dYZEayLtIxNus1XO3gfjfcIFe8a7L0HZRGgag==
  dependencies:
    "@types/mdast" "^3.0.0"
    markdown-table "^3.0.0"
    mdast-util-from-markdown "^1.0.0"
    mdast-util-to-markdown "^1.3.0"

mdast-util-gfm-task-list-item@^1.0.0:
  version "1.0.1"
  resolved "https://registry.yarnpkg.com/mdast-util-gfm-task-list-item/-/mdast-util-gfm-task-list-item-1.0.1.tgz#6f35f09c6e2bcbe88af62fdea02ac199cc802c5c"
  integrity sha512-KZ4KLmPdABXOsfnM6JHUIjxEvcx2ulk656Z/4Balw071/5qgnhz+H1uGtf2zIGnrnvDC8xR4Fj9uKbjAFGNIeA==
  dependencies:
    "@types/mdast" "^3.0.0"
    mdast-util-to-markdown "^1.3.0"

mdast-util-gfm@^2.0.0:
  version "2.0.1"
  resolved "https://registry.yarnpkg.com/mdast-util-gfm/-/mdast-util-gfm-2.0.1.tgz#16fcf70110ae689a06d77e8f4e346223b64a0ea6"
  integrity sha512-42yHBbfWIFisaAfV1eixlabbsa6q7vHeSPY+cg+BBjX51M8xhgMacqH9g6TftB/9+YkcI0ooV4ncfrJslzm/RQ==
  dependencies:
    mdast-util-from-markdown "^1.0.0"
    mdast-util-gfm-autolink-literal "^1.0.0"
    mdast-util-gfm-footnote "^1.0.0"
    mdast-util-gfm-strikethrough "^1.0.0"
    mdast-util-gfm-table "^1.0.0"
    mdast-util-gfm-task-list-item "^1.0.0"
    mdast-util-to-markdown "^1.0.0"

mdast-util-to-hast@^11.0.0:
  version "11.3.0"
  resolved "https://registry.yarnpkg.com/mdast-util-to-hast/-/mdast-util-to-hast-11.3.0.tgz#ea9220617a710e80aa5cc3ac7cc9d4bb0440ae7a"
  integrity sha512-4o3Cli3hXPmm1LhB+6rqhfsIUBjnKFlIUZvudaermXB+4/KONdd/W4saWWkC+LBLbPMqhFSSTSRgafHsT5fVJw==
  dependencies:
    "@types/hast" "^2.0.0"
    "@types/mdast" "^3.0.0"
    "@types/mdurl" "^1.0.0"
    mdast-util-definitions "^5.0.0"
    mdurl "^1.0.0"
    unist-builder "^3.0.0"
    unist-util-generated "^2.0.0"
    unist-util-position "^4.0.0"
    unist-util-visit "^4.0.0"

mdast-util-to-markdown@^1.0.0, mdast-util-to-markdown@^1.3.0:
  version "1.4.0"
  resolved "https://registry.yarnpkg.com/mdast-util-to-markdown/-/mdast-util-to-markdown-1.4.0.tgz#bb0153a865dbc022975f403a156fb6399c494ddf"
  integrity sha512-IjXARf/O8VGx/pc5SZ7syfydq1DYL9vd92orsG5U0b4GNCmAvXzu+n7sbzfIKrXwB0AVrYk3NV2kXl0AIi9LCA==
  dependencies:
    "@types/mdast" "^3.0.0"
    "@types/unist" "^2.0.0"
    longest-streak "^3.0.0"
    mdast-util-to-string "^3.0.0"
    micromark-util-decode-string "^1.0.0"
    unist-util-visit "^4.0.0"
    zwitch "^2.0.0"

mdast-util-to-string@^3.0.0, mdast-util-to-string@^3.1.0:
  version "3.1.0"
  resolved "https://registry.yarnpkg.com/mdast-util-to-string/-/mdast-util-to-string-3.1.0.tgz#56c506d065fbf769515235e577b5a261552d56e9"
  integrity sha512-n4Vypz/DZgwo0iMHLQL49dJzlp7YtAJP+N07MZHpjPf/5XJuHUWstviF4Mn2jEiR/GNmtnRRqnwsXExk3igfFA==

mdn-data@2.0.14:
  version "2.0.14"
  resolved "https://registry.yarnpkg.com/mdn-data/-/mdn-data-2.0.14.tgz#7113fc4281917d63ce29b43446f701e68c25ba50"
  integrity sha512-dn6wd0uw5GsdswPFfsgMp5NSB0/aDe6fK94YJV/AJDYXL6HVLWBsxeq7js7Ad+mU2K9LAlwpk6kN2D5mwCPVow==

mdurl@^1.0.0, mdurl@^1.0.1:
  version "1.0.1"
  resolved "https://registry.yarnpkg.com/mdurl/-/mdurl-1.0.1.tgz#fe85b2ec75a59037f2adfec100fd6c601761152e"
  integrity sha512-/sKlQJCBYVY9Ers9hqzKou4H6V5UWc/M59TH2dvkt+84itfnq7uFOMLpOiOS4ujvHP4etln18fmIxA5R5fll0g==

merge-stream@^2.0.0:
  version "2.0.0"
  resolved "https://registry.yarnpkg.com/merge-stream/-/merge-stream-2.0.0.tgz#52823629a14dd00c9770fb6ad47dc6310f2c1f60"
  integrity sha512-abv/qOcuPfk3URPfDzmZU1LKmuw8kT+0nIHvKrKgFrwifol/doWcdA4ZqsWQ8ENrFKkd67Mfpo/LovbIUsbt3w==

merge2@^1.3.0, merge2@^1.4.1:
  version "1.4.1"
  resolved "https://registry.yarnpkg.com/merge2/-/merge2-1.4.1.tgz#4368892f885e907455a6fd7dc55c0c9d404990ae"
  integrity sha512-8q7VEgMJW4J8tcfVPy8g09NcQwZdbwFEqhe/WZkoIzjn/3TGDwtOCYtXGxA3O8tPzpczCCDgv+P2P5y00ZJOOg==

mhchemparser@^4.1.0:
  version "4.1.1"
  resolved "https://registry.yarnpkg.com/mhchemparser/-/mhchemparser-4.1.1.tgz#a2142fdab37a02ec8d1b48a445059287790becd5"
  integrity sha512-R75CUN6O6e1t8bgailrF1qPq+HhVeFTM3XQ0uzI+mXTybmphy3b6h4NbLOYhemViQ3lUs+6CKRkC3Ws1TlYREA==

micromark-core-commonmark@^1.0.0, micromark-core-commonmark@^1.0.1:
  version "1.0.6"
  resolved "https://registry.yarnpkg.com/micromark-core-commonmark/-/micromark-core-commonmark-1.0.6.tgz#edff4c72e5993d93724a3c206970f5a15b0585ad"
  integrity sha512-K+PkJTxqjFfSNkfAhp4GB+cZPfQd6dxtTXnf+RjZOV7T4EEXnvgzOcnp+eSTmpGk9d1S9sL6/lqrgSNn/s0HZA==
  dependencies:
    decode-named-character-reference "^1.0.0"
    micromark-factory-destination "^1.0.0"
    micromark-factory-label "^1.0.0"
    micromark-factory-space "^1.0.0"
    micromark-factory-title "^1.0.0"
    micromark-factory-whitespace "^1.0.0"
    micromark-util-character "^1.0.0"
    micromark-util-chunked "^1.0.0"
    micromark-util-classify-character "^1.0.0"
    micromark-util-html-tag-name "^1.0.0"
    micromark-util-normalize-identifier "^1.0.0"
    micromark-util-resolve-all "^1.0.0"
    micromark-util-subtokenize "^1.0.0"
    micromark-util-symbol "^1.0.0"
    micromark-util-types "^1.0.1"
    uvu "^0.5.0"

micromark-extension-gfm-autolink-literal@^1.0.0:
  version "1.0.3"
  resolved "https://registry.yarnpkg.com/micromark-extension-gfm-autolink-literal/-/micromark-extension-gfm-autolink-literal-1.0.3.tgz#dc589f9c37eaff31a175bab49f12290edcf96058"
  integrity sha512-i3dmvU0htawfWED8aHMMAzAVp/F0Z+0bPh3YrbTPPL1v4YAlCZpy5rBO5p0LPYiZo0zFVkoYh7vDU7yQSiCMjg==
  dependencies:
    micromark-util-character "^1.0.0"
    micromark-util-sanitize-uri "^1.0.0"
    micromark-util-symbol "^1.0.0"
    micromark-util-types "^1.0.0"
    uvu "^0.5.0"

micromark-extension-gfm-footnote@^1.0.0:
  version "1.0.4"
  resolved "https://registry.yarnpkg.com/micromark-extension-gfm-footnote/-/micromark-extension-gfm-footnote-1.0.4.tgz#cbfd8873b983e820c494498c6dac0105920818d5"
  integrity sha512-E/fmPmDqLiMUP8mLJ8NbJWJ4bTw6tS+FEQS8CcuDtZpILuOb2kjLqPEeAePF1djXROHXChM/wPJw0iS4kHCcIg==
  dependencies:
    micromark-core-commonmark "^1.0.0"
    micromark-factory-space "^1.0.0"
    micromark-util-character "^1.0.0"
    micromark-util-normalize-identifier "^1.0.0"
    micromark-util-sanitize-uri "^1.0.0"
    micromark-util-symbol "^1.0.0"
    micromark-util-types "^1.0.0"
    uvu "^0.5.0"

micromark-extension-gfm-strikethrough@^1.0.0:
  version "1.0.4"
  resolved "https://registry.yarnpkg.com/micromark-extension-gfm-strikethrough/-/micromark-extension-gfm-strikethrough-1.0.4.tgz#162232c284ffbedd8c74e59c1525bda217295e18"
  integrity sha512-/vjHU/lalmjZCT5xt7CcHVJGq8sYRm80z24qAKXzaHzem/xsDYb2yLL+NNVbYvmpLx3O7SYPuGL5pzusL9CLIQ==
  dependencies:
    micromark-util-chunked "^1.0.0"
    micromark-util-classify-character "^1.0.0"
    micromark-util-resolve-all "^1.0.0"
    micromark-util-symbol "^1.0.0"
    micromark-util-types "^1.0.0"
    uvu "^0.5.0"

micromark-extension-gfm-table@^1.0.0:
  version "1.0.5"
  resolved "https://registry.yarnpkg.com/micromark-extension-gfm-table/-/micromark-extension-gfm-table-1.0.5.tgz#7b708b728f8dc4d95d486b9e7a2262f9cddbcbb4"
  integrity sha512-xAZ8J1X9W9K3JTJTUL7G6wSKhp2ZYHrFk5qJgY/4B33scJzE2kpfRL6oiw/veJTbt7jiM/1rngLlOKPWr1G+vg==
  dependencies:
    micromark-factory-space "^1.0.0"
    micromark-util-character "^1.0.0"
    micromark-util-symbol "^1.0.0"
    micromark-util-types "^1.0.0"
    uvu "^0.5.0"

micromark-extension-gfm-tagfilter@^1.0.0:
  version "1.0.1"
  resolved "https://registry.yarnpkg.com/micromark-extension-gfm-tagfilter/-/micromark-extension-gfm-tagfilter-1.0.1.tgz#fb2e303f7daf616db428bb6a26e18fda14a90a4d"
  integrity sha512-Ty6psLAcAjboRa/UKUbbUcwjVAv5plxmpUTy2XC/3nJFL37eHej8jrHrRzkqcpipJliuBH30DTs7+3wqNcQUVA==
  dependencies:
    micromark-util-types "^1.0.0"

micromark-extension-gfm-task-list-item@^1.0.0:
  version "1.0.3"
  resolved "https://registry.yarnpkg.com/micromark-extension-gfm-task-list-item/-/micromark-extension-gfm-task-list-item-1.0.3.tgz#7683641df5d4a09795f353574d7f7f66e47b7fc4"
  integrity sha512-PpysK2S1Q/5VXi72IIapbi/jliaiOFzv7THH4amwXeYXLq3l1uo8/2Be0Ac1rEwK20MQEsGH2ltAZLNY2KI/0Q==
  dependencies:
    micromark-factory-space "^1.0.0"
    micromark-util-character "^1.0.0"
    micromark-util-symbol "^1.0.0"
    micromark-util-types "^1.0.0"
    uvu "^0.5.0"

micromark-extension-gfm@^2.0.0:
  version "2.0.1"
  resolved "https://registry.yarnpkg.com/micromark-extension-gfm/-/micromark-extension-gfm-2.0.1.tgz#40f3209216127a96297c54c67f5edc7ef2d1a2a2"
  integrity sha512-p2sGjajLa0iYiGQdT0oelahRYtMWvLjy8J9LOCxzIQsllMCGLbsLW+Nc+N4vi02jcRJvedVJ68cjelKIO6bpDA==
  dependencies:
    micromark-extension-gfm-autolink-literal "^1.0.0"
    micromark-extension-gfm-footnote "^1.0.0"
    micromark-extension-gfm-strikethrough "^1.0.0"
    micromark-extension-gfm-table "^1.0.0"
    micromark-extension-gfm-tagfilter "^1.0.0"
    micromark-extension-gfm-task-list-item "^1.0.0"
    micromark-util-combine-extensions "^1.0.0"
    micromark-util-types "^1.0.0"

micromark-factory-destination@^1.0.0:
  version "1.0.0"
  resolved "https://registry.yarnpkg.com/micromark-factory-destination/-/micromark-factory-destination-1.0.0.tgz#fef1cb59ad4997c496f887b6977aa3034a5a277e"
  integrity sha512-eUBA7Rs1/xtTVun9TmV3gjfPz2wEwgK5R5xcbIM5ZYAtvGF6JkyaDsj0agx8urXnO31tEO6Ug83iVH3tdedLnw==
  dependencies:
    micromark-util-character "^1.0.0"
    micromark-util-symbol "^1.0.0"
    micromark-util-types "^1.0.0"

micromark-factory-label@^1.0.0:
  version "1.0.2"
  resolved "https://registry.yarnpkg.com/micromark-factory-label/-/micromark-factory-label-1.0.2.tgz#6be2551fa8d13542fcbbac478258fb7a20047137"
  integrity sha512-CTIwxlOnU7dEshXDQ+dsr2n+yxpP0+fn271pu0bwDIS8uqfFcumXpj5mLn3hSC8iw2MUr6Gx8EcKng1dD7i6hg==
  dependencies:
    micromark-util-character "^1.0.0"
    micromark-util-symbol "^1.0.0"
    micromark-util-types "^1.0.0"
    uvu "^0.5.0"

micromark-factory-space@^1.0.0:
  version "1.0.0"
  resolved "https://registry.yarnpkg.com/micromark-factory-space/-/micromark-factory-space-1.0.0.tgz#cebff49968f2b9616c0fcb239e96685cb9497633"
  integrity sha512-qUmqs4kj9a5yBnk3JMLyjtWYN6Mzfcx8uJfi5XAveBniDevmZasdGBba5b4QsvRcAkmvGo5ACmSUmyGiKTLZew==
  dependencies:
    micromark-util-character "^1.0.0"
    micromark-util-types "^1.0.0"

micromark-factory-title@^1.0.0:
  version "1.0.2"
  resolved "https://registry.yarnpkg.com/micromark-factory-title/-/micromark-factory-title-1.0.2.tgz#7e09287c3748ff1693930f176e1c4a328382494f"
  integrity sha512-zily+Nr4yFqgMGRKLpTVsNl5L4PMu485fGFDOQJQBl2NFpjGte1e86zC0da93wf97jrc4+2G2GQudFMHn3IX+A==
  dependencies:
    micromark-factory-space "^1.0.0"
    micromark-util-character "^1.0.0"
    micromark-util-symbol "^1.0.0"
    micromark-util-types "^1.0.0"
    uvu "^0.5.0"

micromark-factory-whitespace@^1.0.0:
  version "1.0.0"
  resolved "https://registry.yarnpkg.com/micromark-factory-whitespace/-/micromark-factory-whitespace-1.0.0.tgz#e991e043ad376c1ba52f4e49858ce0794678621c"
  integrity sha512-Qx7uEyahU1lt1RnsECBiuEbfr9INjQTGa6Err+gF3g0Tx4YEviPbqqGKNv/NrBaE7dVHdn1bVZKM/n5I/Bak7A==
  dependencies:
    micromark-factory-space "^1.0.0"
    micromark-util-character "^1.0.0"
    micromark-util-symbol "^1.0.0"
    micromark-util-types "^1.0.0"

micromark-util-character@^1.0.0:
  version "1.1.0"
  resolved "https://registry.yarnpkg.com/micromark-util-character/-/micromark-util-character-1.1.0.tgz#d97c54d5742a0d9611a68ca0cd4124331f264d86"
  integrity sha512-agJ5B3unGNJ9rJvADMJ5ZiYjBRyDpzKAOk01Kpi1TKhlT1APx3XZk6eN7RtSz1erbWHC2L8T3xLZ81wdtGRZzg==
  dependencies:
    micromark-util-symbol "^1.0.0"
    micromark-util-types "^1.0.0"

micromark-util-chunked@^1.0.0:
  version "1.0.0"
  resolved "https://registry.yarnpkg.com/micromark-util-chunked/-/micromark-util-chunked-1.0.0.tgz#5b40d83f3d53b84c4c6bce30ed4257e9a4c79d06"
  integrity sha512-5e8xTis5tEZKgesfbQMKRCyzvffRRUX+lK/y+DvsMFdabAicPkkZV6gO+FEWi9RfuKKoxxPwNL+dFF0SMImc1g==
  dependencies:
    micromark-util-symbol "^1.0.0"

micromark-util-classify-character@^1.0.0:
  version "1.0.0"
  resolved "https://registry.yarnpkg.com/micromark-util-classify-character/-/micromark-util-classify-character-1.0.0.tgz#cbd7b447cb79ee6997dd274a46fc4eb806460a20"
  integrity sha512-F8oW2KKrQRb3vS5ud5HIqBVkCqQi224Nm55o5wYLzY/9PwHGXC01tr3d7+TqHHz6zrKQ72Okwtvm/xQm6OVNZA==
  dependencies:
    micromark-util-character "^1.0.0"
    micromark-util-symbol "^1.0.0"
    micromark-util-types "^1.0.0"

micromark-util-combine-extensions@^1.0.0:
  version "1.0.0"
  resolved "https://registry.yarnpkg.com/micromark-util-combine-extensions/-/micromark-util-combine-extensions-1.0.0.tgz#91418e1e74fb893e3628b8d496085639124ff3d5"
  integrity sha512-J8H058vFBdo/6+AsjHp2NF7AJ02SZtWaVUjsayNFeAiydTxUwViQPxN0Hf8dp4FmCQi0UUFovFsEyRSUmFH3MA==
  dependencies:
    micromark-util-chunked "^1.0.0"
    micromark-util-types "^1.0.0"

micromark-util-decode-numeric-character-reference@^1.0.0:
  version "1.0.0"
  resolved "https://registry.yarnpkg.com/micromark-util-decode-numeric-character-reference/-/micromark-util-decode-numeric-character-reference-1.0.0.tgz#dcc85f13b5bd93ff8d2868c3dba28039d490b946"
  integrity sha512-OzO9AI5VUtrTD7KSdagf4MWgHMtET17Ua1fIpXTpuhclCqD8egFWo85GxSGvxgkGS74bEahvtM0WP0HjvV0e4w==
  dependencies:
    micromark-util-symbol "^1.0.0"

micromark-util-decode-string@^1.0.0:
  version "1.0.2"
  resolved "https://registry.yarnpkg.com/micromark-util-decode-string/-/micromark-util-decode-string-1.0.2.tgz#942252ab7a76dec2dbf089cc32505ee2bc3acf02"
  integrity sha512-DLT5Ho02qr6QWVNYbRZ3RYOSSWWFuH3tJexd3dgN1odEuPNxCngTCXJum7+ViRAd9BbdxCvMToPOD/IvVhzG6Q==
  dependencies:
    decode-named-character-reference "^1.0.0"
    micromark-util-character "^1.0.0"
    micromark-util-decode-numeric-character-reference "^1.0.0"
    micromark-util-symbol "^1.0.0"

micromark-util-encode@^1.0.0:
  version "1.0.1"
  resolved "https://registry.yarnpkg.com/micromark-util-encode/-/micromark-util-encode-1.0.1.tgz#2c1c22d3800870ad770ece5686ebca5920353383"
  integrity sha512-U2s5YdnAYexjKDel31SVMPbfi+eF8y1U4pfiRW/Y8EFVCy/vgxk/2wWTxzcqE71LHtCuCzlBDRU2a5CQ5j+mQA==

micromark-util-html-tag-name@^1.0.0:
  version "1.1.0"
  resolved "https://registry.yarnpkg.com/micromark-util-html-tag-name/-/micromark-util-html-tag-name-1.1.0.tgz#eb227118befd51f48858e879b7a419fc0df20497"
  integrity sha512-BKlClMmYROy9UiV03SwNmckkjn8QHVaWkqoAqzivabvdGcwNGMMMH/5szAnywmsTBUzDsU57/mFi0sp4BQO6dA==

micromark-util-normalize-identifier@^1.0.0:
  version "1.0.0"
  resolved "https://registry.yarnpkg.com/micromark-util-normalize-identifier/-/micromark-util-normalize-identifier-1.0.0.tgz#4a3539cb8db954bbec5203952bfe8cedadae7828"
  integrity sha512-yg+zrL14bBTFrQ7n35CmByWUTFsgst5JhA4gJYoty4Dqzj4Z4Fr/DHekSS5aLfH9bdlfnSvKAWsAgJhIbogyBg==
  dependencies:
    micromark-util-symbol "^1.0.0"

micromark-util-resolve-all@^1.0.0:
  version "1.0.0"
  resolved "https://registry.yarnpkg.com/micromark-util-resolve-all/-/micromark-util-resolve-all-1.0.0.tgz#a7c363f49a0162e931960c44f3127ab58f031d88"
  integrity sha512-CB/AGk98u50k42kvgaMM94wzBqozSzDDaonKU7P7jwQIuH2RU0TeBqGYJz2WY1UdihhjweivStrJ2JdkdEmcfw==
  dependencies:
    micromark-util-types "^1.0.0"

micromark-util-sanitize-uri@^1.0.0:
  version "1.1.0"
  resolved "https://registry.yarnpkg.com/micromark-util-sanitize-uri/-/micromark-util-sanitize-uri-1.1.0.tgz#f12e07a85106b902645e0364feb07cf253a85aee"
  integrity sha512-RoxtuSCX6sUNtxhbmsEFQfWzs8VN7cTctmBPvYivo98xb/kDEoTCtJQX5wyzIYEmk/lvNFTat4hL8oW0KndFpg==
  dependencies:
    micromark-util-character "^1.0.0"
    micromark-util-encode "^1.0.0"
    micromark-util-symbol "^1.0.0"

micromark-util-subtokenize@^1.0.0:
  version "1.0.2"
  resolved "https://registry.yarnpkg.com/micromark-util-subtokenize/-/micromark-util-subtokenize-1.0.2.tgz#ff6f1af6ac836f8bfdbf9b02f40431760ad89105"
  integrity sha512-d90uqCnXp/cy4G881Ub4psE57Sf8YD0pim9QdjCRNjfas2M1u6Lbt+XZK9gnHL2XFhnozZiEdCa9CNfXSfQ6xA==
  dependencies:
    micromark-util-chunked "^1.0.0"
    micromark-util-symbol "^1.0.0"
    micromark-util-types "^1.0.0"
    uvu "^0.5.0"

micromark-util-symbol@^1.0.0:
  version "1.0.1"
  resolved "https://registry.yarnpkg.com/micromark-util-symbol/-/micromark-util-symbol-1.0.1.tgz#b90344db62042ce454f351cf0bebcc0a6da4920e"
  integrity sha512-oKDEMK2u5qqAptasDAwWDXq0tG9AssVwAx3E9bBF3t/shRIGsWIRG+cGafs2p/SnDSOecnt6hZPCE2o6lHfFmQ==

micromark-util-types@^1.0.0, micromark-util-types@^1.0.1:
  version "1.0.2"
  resolved "https://registry.yarnpkg.com/micromark-util-types/-/micromark-util-types-1.0.2.tgz#f4220fdb319205812f99c40f8c87a9be83eded20"
  integrity sha512-DCfg/T8fcrhrRKTPjRrw/5LLvdGV7BHySf/1LOZx7TzWZdYRjogNtyNq885z3nNallwr3QUKARjqvHqX1/7t+w==

micromark@^3.0.0:
  version "3.1.0"
  resolved "https://registry.yarnpkg.com/micromark/-/micromark-3.1.0.tgz#eeba0fe0ac1c9aaef675157b52c166f125e89f62"
  integrity sha512-6Mj0yHLdUZjHnOPgr5xfWIMqMWS12zDN6iws9SLuSz76W8jTtAv24MN4/CL7gJrl5vtxGInkkqDv/JIoRsQOvA==
  dependencies:
    "@types/debug" "^4.0.0"
    debug "^4.0.0"
    decode-named-character-reference "^1.0.0"
    micromark-core-commonmark "^1.0.1"
    micromark-factory-space "^1.0.0"
    micromark-util-character "^1.0.0"
    micromark-util-chunked "^1.0.0"
    micromark-util-combine-extensions "^1.0.0"
    micromark-util-decode-numeric-character-reference "^1.0.0"
    micromark-util-encode "^1.0.0"
    micromark-util-normalize-identifier "^1.0.0"
    micromark-util-resolve-all "^1.0.0"
    micromark-util-sanitize-uri "^1.0.0"
    micromark-util-subtokenize "^1.0.0"
    micromark-util-symbol "^1.0.0"
    micromark-util-types "^1.0.1"
    uvu "^0.5.0"

micromatch@^4.0.0, micromatch@^4.0.4, micromatch@^4.0.5:
  version "4.0.5"
  resolved "https://registry.yarnpkg.com/micromatch/-/micromatch-4.0.5.tgz#bc8999a7cbbf77cdc89f132f6e467051b49090c6"
  integrity sha512-DMy+ERcEW2q8Z2Po+WNXuw3c5YaUSFjAO5GsJqfEl7UjvtIuFKO6ZrKvcItdy98dwFI2N1tg3zNIdKaQT+aNdA==
  dependencies:
    braces "^3.0.2"
    picomatch "^2.3.1"

mime-db@1.52.0:
  version "1.52.0"
  resolved "https://registry.yarnpkg.com/mime-db/-/mime-db-1.52.0.tgz#bbabcdc02859f4987301c856e3387ce5ec43bf70"
  integrity sha512-sPU4uV7dYlvtWJxwwxHD0PuihVNiE7TyAbQ5SWxDCB9mUYvOgroQOwYQQOKPJ8CIbE+1ETVlOoK1UC2nU3gYvg==

mime-types@^2.1.12:
  version "2.1.35"
  resolved "https://registry.yarnpkg.com/mime-types/-/mime-types-2.1.35.tgz#381a871b62a734450660ae3deee44813f70d959a"
  integrity sha512-ZDY+bPm5zTTF+YpCrAU9nK0UgICYPT0QtT1NZWFv4s++TNkcgVaT0g6+4R2uI4MjQjzysHB1zxuWL50hzaeXiw==
  dependencies:
    mime-db "1.52.0"

mime@~2.5.2:
  version "2.5.2"
  resolved "https://registry.yarnpkg.com/mime/-/mime-2.5.2.tgz#6e3dc6cc2b9510643830e5f19d5cb753da5eeabe"
  integrity sha512-tqkh47FzKeCPD2PUiPB6pkbMzsCasjxAfC62/Wap5qrUWcb+sFasXUC5I3gYM5iBM8v/Qpn4UK0x+j0iHyFPDg==

mimic-fn@^2.1.0:
  version "2.1.0"
  resolved "https://registry.yarnpkg.com/mimic-fn/-/mimic-fn-2.1.0.tgz#7ed2c2ccccaf84d3ffcb7a69b57711fc2083401b"
  integrity sha512-OqbOk5oEQeAZ8WXWydlu9HJjz9WVdEIvamMCcXmuqUYjTknH/sqsWvhQ3vgwKFRR1HpjvNBKQ37nbJgYzGqGcg==

minimatch@^3.0.4, minimatch@^3.0.5, minimatch@^3.1.1, minimatch@^3.1.2:
  version "3.1.2"
  resolved "https://registry.yarnpkg.com/minimatch/-/minimatch-3.1.2.tgz#19cd194bfd3e428f049a70817c038d89ab4be35b"
  integrity sha512-J7p63hRiAjw1NDEww1W7i37+ByIrOWO5XQQAzZ3VOcL0PNybwpfmV/N05zFAzwQ9USyEcX6t3UO+K5aqBQOIHw==
  dependencies:
    brace-expansion "^1.1.7"

minimatch@~3.0.4:
  version "3.0.8"
  resolved "https://registry.yarnpkg.com/minimatch/-/minimatch-3.0.8.tgz#5e6a59bd11e2ab0de1cfb843eb2d82e546c321c1"
  integrity sha512-6FsRAQsxQ61mw+qP1ZzbL9Bc78x2p5OqNgNpnoAFLTrX8n5Kxph0CsnhmKKNXTWjXqU5L0pGPR7hYk+XWZr60Q==
  dependencies:
    brace-expansion "^1.1.7"

minimist@^1.2.6:
  version "1.2.7"
  resolved "https://registry.yarnpkg.com/minimist/-/minimist-1.2.7.tgz#daa1c4d91f507390437c6a8bc01078e7000c4d18"
  integrity sha512-bzfL1YUZsP41gmu/qjrEk0Q6i2ix/cVeAhbCbqH9u3zYutS1cLg00qhrD0M2MVdCcx4Sc0UpP2eBWo9rotpq6g==

mj-context-menu@^0.6.1:
  version "0.6.1"
  resolved "https://registry.yarnpkg.com/mj-context-menu/-/mj-context-menu-0.6.1.tgz#a043c5282bf7e1cf3821de07b13525ca6f85aa69"
  integrity sha512-7NO5s6n10TIV96d4g2uDpG7ZDpIhMh0QNfGdJw/W47JswFcosz457wqz/b5sAKvl12sxINGFCn80NZHKwxQEXA==

mkdirp-classic@^0.5.2:
  version "0.5.3"
  resolved "https://registry.yarnpkg.com/mkdirp-classic/-/mkdirp-classic-0.5.3.tgz#fa10c9115cc6d8865be221ba47ee9bed78601113"
  integrity sha512-gKLcREMhtuZRwRAfqP3RFW+TK4JqApVBtOIftVgjuABpAtpxhPGaDcfvbhNvD0B8iD1oUr/txX35NjcaY6Ns/A==

mri@^1.1.0:
  version "1.2.0"
  resolved "https://registry.yarnpkg.com/mri/-/mri-1.2.0.tgz#6721480fec2a11a4889861115a48b6cbe7cc8f0b"
  integrity sha512-tzzskb3bG8LvYGFF/mDTpq3jpI6Q9wc3LEmBaghu+DdCssd1FakN7Bc0hVNmEyGq1bq3RgfkCb3cmQLpNPOroA==

mrmime@^1.0.0:
  version "1.0.1"
  resolved "https://registry.yarnpkg.com/mrmime/-/mrmime-1.0.1.tgz#5f90c825fad4bdd41dc914eff5d1a8cfdaf24f27"
  integrity sha512-hzzEagAgDyoU1Q6yg5uI+AorQgdvMCur3FcKf7NhMKWsaYg+RnbTyHRa/9IlLF9rf455MOCtcqqrQQ83pPP7Uw==

ms@2.0.0:
  version "2.0.0"
  resolved "https://registry.yarnpkg.com/ms/-/ms-2.0.0.tgz#5608aeadfc00be6c2901df5f9861788de0d597c8"
  integrity sha512-Tpp60P6IUJDTuOq/5Z8cdskzJujfwqfOTkrwIwj7IRISpnkJnT6SyJ4PCPnGMoFjC9ddhal5KVIYtAt97ix05A==

ms@2.1.2:
  version "2.1.2"
  resolved "https://registry.yarnpkg.com/ms/-/ms-2.1.2.tgz#d09d1f357b443f493382a8eb3ccd183872ae6009"
  integrity sha512-sGkPx+VjMtmA6MX27oA4FBFELFCZZ4S4XqeGOXCv68tT+jb3vk/RyaKWP0PTKyWtmLSM0b+adUTEvbs1PEaH2w==

ms@^2.1.1:
  version "2.1.3"
  resolved "https://registry.yarnpkg.com/ms/-/ms-2.1.3.tgz#574c8138ce1d2b5861f0b44579dbadd60c6615b2"
  integrity sha512-6FlzubTLZG3J2a/NVCAleEhjzq5oxgHyaCU9yYXvcLsvoVaHJq/s5xXI6/XXP6tz7R9xAOtHnSO/tXtF3WRTlA==

nanoid@^3.3.4:
  version "3.3.4"
  resolved "https://registry.yarnpkg.com/nanoid/-/nanoid-3.3.4.tgz#730b67e3cd09e2deacf03c027c81c9d9dbc5e8ab"
  integrity sha512-MqBkQh/OHTS2egovRtLk45wEyNXwF+cokD+1YPf9u5VfJiRdAiRwB2froX5Co9Rh20xs4siNPm8naNotSD6RBw==

nanoid@^3.3.6:
  version "3.3.6"
  resolved "https://registry.yarnpkg.com/nanoid/-/nanoid-3.3.6.tgz#443380c856d6e9f9824267d960b4236ad583ea4c"
  integrity sha512-BGcqMMJuToF7i1rt+2PWSNVnWIkGCU78jBG3RxO/bZlnZPK2Cmi2QaffxGO/2RvWi9sL+FAiRiXMgsyxQ1DIDA==

natural-compare-lite@^1.4.0:
  version "1.4.0"
  resolved "https://registry.yarnpkg.com/natural-compare-lite/-/natural-compare-lite-1.4.0.tgz#17b09581988979fddafe0201e931ba933c96cbb4"
  integrity sha512-Tj+HTDSJJKaZnfiuw+iaF9skdPpTo2GtEly5JHnWV/hfv2Qj/9RKsGISQtLh2ox3l5EAGw487hnBee0sIJ6v2g==

natural-compare@^1.4.0:
  version "1.4.0"
  resolved "https://registry.yarnpkg.com/natural-compare/-/natural-compare-1.4.0.tgz#4abebfeed7541f2c27acfb29bdbbd15c8d5ba4f7"
  integrity sha512-OWND8ei3VtNC9h7V60qff3SVobHr996CTwgxubgyQYEpg290h9J0buyECNNJexkFm5sOajh5G116RYA1c8ZMSw==

next@^13.1.1:
  version "13.1.1"
  resolved "https://registry.yarnpkg.com/next/-/next-13.1.1.tgz#42b825f650410649aff1017d203a088d77c80b5b"
  integrity sha512-R5eBAaIa3X7LJeYvv1bMdGnAVF4fVToEjim7MkflceFPuANY3YyvFxXee/A+acrSYwYPvOvf7f6v/BM/48ea5w==
  dependencies:
    "@next/env" "13.1.1"
    "@swc/helpers" "0.4.14"
    caniuse-lite "^1.0.30001406"
    postcss "8.4.14"
    styled-jsx "5.1.1"
  optionalDependencies:
    "@next/swc-android-arm-eabi" "13.1.1"
    "@next/swc-android-arm64" "13.1.1"
    "@next/swc-darwin-arm64" "13.1.1"
    "@next/swc-darwin-x64" "13.1.1"
    "@next/swc-freebsd-x64" "13.1.1"
    "@next/swc-linux-arm-gnueabihf" "13.1.1"
    "@next/swc-linux-arm64-gnu" "13.1.1"
    "@next/swc-linux-arm64-musl" "13.1.1"
    "@next/swc-linux-x64-gnu" "13.1.1"
    "@next/swc-linux-x64-musl" "13.1.1"
    "@next/swc-win32-arm64-msvc" "13.1.1"
    "@next/swc-win32-ia32-msvc" "13.1.1"
    "@next/swc-win32-x64-msvc" "13.1.1"

node-domexception@^1.0.0:
  version "1.0.0"
  resolved "https://registry.yarnpkg.com/node-domexception/-/node-domexception-1.0.0.tgz#6888db46a1f71c0b76b3f7555016b63fe64766e5"
  integrity sha512-/jKZoMpw0F8GRwl4/eLROPA3cfcXtLApP0QzLmUT/HuPCZWyB7IY9ZrMeKw2O/nFIqPQB3PVM9aYm0F312AXDQ==

node-fetch@^2.6.0:
  version "2.6.7"
  resolved "https://registry.yarnpkg.com/node-fetch/-/node-fetch-2.6.7.tgz#24de9fba827e3b4ae44dc8b20256a379160052ad"
  integrity sha512-ZjMPFEfVx5j+y2yF35Kzx5sF7kDzxuDj6ziH4FFbOp87zKDZNx8yExJIb05OGF4Nlt9IHFIMBkRl41VdvcNdbQ==
  dependencies:
    whatwg-url "^5.0.0"

node-fetch@^3.3.0:
  version "3.3.0"
  resolved "https://registry.yarnpkg.com/node-fetch/-/node-fetch-3.3.0.tgz#37e71db4ecc257057af828d523a7243d651d91e4"
  integrity sha512-BKwRP/O0UvoMKp7GNdwPlObhYGB5DQqwhEDQlNKuoqwVYSxkSZCSbHjnFFmUEtwSKRPU4kNK8PbDYYitwaE3QA==
  dependencies:
    data-uri-to-buffer "^4.0.0"
    fetch-blob "^3.1.4"
    formdata-polyfill "^4.0.10"

node-releases@^2.0.6:
  version "2.0.8"
  resolved "https://registry.yarnpkg.com/node-releases/-/node-releases-2.0.8.tgz#0f349cdc8fcfa39a92ac0be9bc48b7706292b9ae"
  integrity sha512-dFSmB8fFHEH/s81Xi+Y/15DQY6VHW81nXRj86EMSL3lmuTmK1e+aT4wrFCkTbm+gSwkw4KpX+rT/pMM2c1mF+A==

normalize-path@^3.0.0, normalize-path@~3.0.0:
  version "3.0.0"
  resolved "https://registry.yarnpkg.com/normalize-path/-/normalize-path-3.0.0.tgz#0dcd69ff23a1c9b11fd0978316644a0388216a65"
  integrity sha512-6eZs5Ls3WtCisHWp9S2GUy8dqkpGi4BVSz3GaqiE6ezub0512ESztXUwUB6C6IKbQkY2Pnb/mD4WYojCRwcwLA==

normalize-range@^0.1.2:
  version "0.1.2"
  resolved "https://registry.yarnpkg.com/normalize-range/-/normalize-range-0.1.2.tgz#2d10c06bdfd312ea9777695a4d28439456b75942"
  integrity sha512-bdok/XvKII3nUpklnV6P2hxtMNrCboOjAcyBuQnWEhO665FwrSNRxU+AqpsyvO6LgGYPspN+lu5CLtw4jPRKNA==

npm-run-path@^4.0.1:
  version "4.0.1"
  resolved "https://registry.yarnpkg.com/npm-run-path/-/npm-run-path-4.0.1.tgz#b7ecd1e5ed53da8e37a55e1c2269e0b97ed748ea"
  integrity sha512-S48WzZW777zhNIrn7gxOlISNAqi9ZC/uQFnRdbeIHhZhCA6UqpkOT8T1G7BvfdgP4Er8gF4sUbaS0i7QvIfCWw==
  dependencies:
    path-key "^3.0.0"

npmlog@^4.1.2:
  version "4.1.2"
  resolved "https://registry.yarnpkg.com/npmlog/-/npmlog-4.1.2.tgz#08a7f2a8bf734604779a9efa4ad5cc717abb954b"
  integrity sha512-2uUqazuKlTaSI/dC8AzicUck7+IrEaOnN/e0jd3Xtt1KcGpwx30v50mL7oPyr/h9bL3E4aZccVwpwP+5W9Vjkg==
  dependencies:
    are-we-there-yet "~1.1.2"
    console-control-strings "~1.1.0"
    gauge "~2.7.3"
    set-blocking "~2.0.0"

nprogress@^0.2.0:
  version "0.2.0"
  resolved "https://registry.yarnpkg.com/nprogress/-/nprogress-0.2.0.tgz#cb8f34c53213d895723fcbab907e9422adbcafb1"
  integrity sha512-I19aIingLgR1fmhftnbWWO3dXc0hSxqHQHQb3H8m+K3TnEn/iSeTZZOyvKXWqQESMwuUVnatlCnZdLBZZt2VSA==

nth-check@^2.0.1:
  version "2.1.1"
  resolved "https://registry.yarnpkg.com/nth-check/-/nth-check-2.1.1.tgz#c9eab428effce36cd6b92c924bdb000ef1f1ed1d"
  integrity sha512-lqjrjmaOoAnWfMmBPL+XNnynZh2+swxiX3WUE0s4yEHI6m+AwrK2UZOimIRl3X/4QctVqS8AiZjFqyOGrMXb/w==
  dependencies:
    boolbase "^1.0.0"

null-loader@^4.0.1:
  version "4.0.1"
  resolved "https://registry.yarnpkg.com/null-loader/-/null-loader-4.0.1.tgz#8e63bd3a2dd3c64236a4679428632edd0a6dbc6a"
  integrity sha512-pxqVbi4U6N26lq+LmgIbB5XATP0VdZKOG25DhHi8btMmJJefGArFyDg1yc4U3hWCJbMqSrw0qyrz1UQX+qYXqg==
  dependencies:
    loader-utils "^2.0.0"
    schema-utils "^3.0.0"

number-is-nan@^1.0.0:
  version "1.0.1"
  resolved "https://registry.yarnpkg.com/number-is-nan/-/number-is-nan-1.0.1.tgz#097b602b53422a522c1afb8790318336941a011d"
  integrity sha512-4jbtZXNAsfZbAHiiqjLPBiCl16dES1zI4Hpzzxw61Tk+loF+sBDBKx1ICKKKwIqQ7M0mFn1TmkN7euSncWgHiQ==

object-assign@^4.1.0, object-assign@^4.1.1:
  version "4.1.1"
  resolved "https://registry.yarnpkg.com/object-assign/-/object-assign-4.1.1.tgz#2109adc7965887cfc05cbbd442cac8bfbb360863"
  integrity sha512-rJgTQnkUnH1sFw8yT6VSU3zD3sWmu6sZhIseY8VX+GRu3P6F7Fu+JNDoXfklElbLJSnc3FUQHVe4cU5hj+BcUg==

object-hash@^3.0.0:
  version "3.0.0"
  resolved "https://registry.yarnpkg.com/object-hash/-/object-hash-3.0.0.tgz#73f97f753e7baffc0e2cc9d6e079079744ac82e9"
  integrity sha512-RSn9F68PjH9HqtltsSnqYC1XXoWe9Bju5+213R98cNGttag9q9yAOTzdbsqvIa7aNm5WffBZFpWYr2aWrklWAw==

object-inspect@^1.12.2, object-inspect@^1.9.0:
  version "1.12.2"
  resolved "https://registry.yarnpkg.com/object-inspect/-/object-inspect-1.12.2.tgz#c0641f26394532f28ab8d796ab954e43c009a8ea"
  integrity sha512-z+cPxW0QGUp0mcqcsgQyLVRDoXFQbXOwBaqyF7VIgI4TWNQsDHrBpUQslRmIfAoYWdYzs6UlKJtB2XJpTaNSpQ==

object-keys@^1.1.1:
  version "1.1.1"
  resolved "https://registry.yarnpkg.com/object-keys/-/object-keys-1.1.1.tgz#1c47f272df277f3b1daf061677d9c82e2322c60e"
  integrity sha512-NuAESUOUMrlIXOfHKzD6bpPu3tYt3xvjNdRIQ+FeT0lNb4K8WR70CaDxhuNguS2XG+GjkyMwOzsN5ZktImfhLA==

object.assign@^4.1.3, object.assign@^4.1.4:
  version "4.1.4"
  resolved "https://registry.yarnpkg.com/object.assign/-/object.assign-4.1.4.tgz#9673c7c7c351ab8c4d0b516f4343ebf4dfb7799f"
  integrity sha512-1mxKf0e58bvyjSCtKYY4sRe9itRk3PJpquJOjeIkz885CczcI4IvJJDLPS72oowuSh+pBxUFROpX+TU++hxhZQ==
  dependencies:
    call-bind "^1.0.2"
    define-properties "^1.1.4"
    has-symbols "^1.0.3"
    object-keys "^1.1.1"

object.entries@^1.1.6:
  version "1.1.6"
  resolved "https://registry.yarnpkg.com/object.entries/-/object.entries-1.1.6.tgz#9737d0e5b8291edd340a3e3264bb8a3b00d5fa23"
  integrity sha512-leTPzo4Zvg3pmbQ3rDK69Rl8GQvIqMWubrkxONG9/ojtFE2rD9fjMKfSI5BxW3osRH1m6VdzmqK8oAY9aT4x5w==
  dependencies:
    call-bind "^1.0.2"
    define-properties "^1.1.4"
    es-abstract "^1.20.4"

object.fromentries@^2.0.6:
  version "2.0.6"
  resolved "https://registry.yarnpkg.com/object.fromentries/-/object.fromentries-2.0.6.tgz#cdb04da08c539cffa912dcd368b886e0904bfa73"
  integrity sha512-VciD13dswC4j1Xt5394WR4MzmAQmlgN72phd/riNp9vtD7tp4QQWJ0R4wvclXcafgcYK8veHRed2W6XeGBvcfg==
  dependencies:
    call-bind "^1.0.2"
    define-properties "^1.1.4"
    es-abstract "^1.20.4"

object.hasown@^1.1.2:
  version "1.1.2"
  resolved "https://registry.yarnpkg.com/object.hasown/-/object.hasown-1.1.2.tgz#f919e21fad4eb38a57bc6345b3afd496515c3f92"
  integrity sha512-B5UIT3J1W+WuWIU55h0mjlwaqxiE5vYENJXIXZ4VFe05pNYrkKuK0U/6aFcb0pKywYJh7IhfoqUfKVmrJJHZHw==
  dependencies:
    define-properties "^1.1.4"
    es-abstract "^1.20.4"

object.values@^1.1.5, object.values@^1.1.6:
  version "1.1.6"
  resolved "https://registry.yarnpkg.com/object.values/-/object.values-1.1.6.tgz#4abbaa71eba47d63589d402856f908243eea9b1d"
  integrity sha512-FVVTkD1vENCsAcwNs9k6jea2uHC/X0+JcjG8YA60FN5CMaJmG95wT9jek/xX9nornqGRrBkKtzuAu2wuHpKqvw==
  dependencies:
    call-bind "^1.0.2"
    define-properties "^1.1.4"
    es-abstract "^1.20.4"

once@^1.3.0, once@^1.3.1, once@^1.4.0:
  version "1.4.0"
  resolved "https://registry.yarnpkg.com/once/-/once-1.4.0.tgz#583b1aa775961d4b113ac17d9c50baef9dd76bd1"
  integrity sha512-lNaJgI+2Q5URQBkccEKHTQOPaXdUxnZZElQTZY0MFUAuaEqe1E+Nyvgdz/aIyNi6Z9MzO5dv1H8n58/GELp3+w==
  dependencies:
    wrappy "1"

onetime@^5.1.2:
  version "5.1.2"
  resolved "https://registry.yarnpkg.com/onetime/-/onetime-5.1.2.tgz#d0e96ebb56b07476df1dd9c4806e5237985ca45e"
  integrity sha512-kbpaSSGJTWdAY5KPVeMOKXSrPtr8C8C7wodJbcsd51jRnmD+GZu8Y0VoU6Dm5Z4vWr0Ig/1NKuWRKf7j5aaYSg==
  dependencies:
    mimic-fn "^2.1.0"

open@^8.4.0:
  version "8.4.0"
  resolved "https://registry.yarnpkg.com/open/-/open-8.4.0.tgz#345321ae18f8138f82565a910fdc6b39e8c244f8"
  integrity sha512-XgFPPM+B28FtCCgSb9I+s9szOC1vZRSwgWsRUA5ylIxRTgKozqjOCrVOqGsYABPYK5qnfqClxZTFBa8PKt2v6Q==
  dependencies:
    define-lazy-prop "^2.0.0"
    is-docker "^2.1.1"
    is-wsl "^2.2.0"

opener@^1.5.2:
  version "1.5.2"
  resolved "https://registry.yarnpkg.com/opener/-/opener-1.5.2.tgz#5d37e1f35077b9dcac4301372271afdeb2a13598"
  integrity sha512-ur5UIdyw5Y7yEj9wLzhqXiy6GZ3Mwx0yGI+5sMn2r0N0v3cKJvUmFH5yPP+WXh9e0xfyzyJX95D8l088DNFj7A==

optionator@^0.9.1:
  version "0.9.1"
  resolved "https://registry.yarnpkg.com/optionator/-/optionator-0.9.1.tgz#4f236a6373dae0566a6d43e1326674f50c291499"
  integrity sha512-74RlY5FCnhq4jRxVUPKDaRwrVNXMqsGsiW6AJw4XK8hmtm10wC0ypZBLw5IIp85NZMr91+qd1RvvENwg7jjRFw==
  dependencies:
    deep-is "^0.1.3"
    fast-levenshtein "^2.0.6"
    levn "^0.4.1"
    prelude-ls "^1.2.1"
    type-check "^0.4.0"
    word-wrap "^1.2.3"

p-graph@^1.1.1:
  version "1.1.2"
  resolved "https://registry.yarnpkg.com/p-graph/-/p-graph-1.1.2.tgz#594010591e258ebc013f275f414ef6c5bfc25d51"
  integrity sha512-GnEEHrOMozk0hCjXBm011oYb3zpaOolxHgqL2s7Od2niGAJKyk/4FZ2VRUAgjqqqoQnZQtwkF6fjGDJkIQTjDQ==

p-limit@^2.2.0:
  version "2.3.0"
  resolved "https://registry.yarnpkg.com/p-limit/-/p-limit-2.3.0.tgz#3dd33c647a214fdfffd835933eb086da0dc21db1"
  integrity sha512-//88mFWSJx8lxCzwdAABTJL2MyWB12+eIY7MDL2SqLmAkeKU9qxRvWuSyTjm3FUmpBEMuFfckAIqEaVGUDxb6w==
  dependencies:
    p-try "^2.0.0"

p-limit@^3.0.0, p-limit@^3.0.2:
  version "3.1.0"
  resolved "https://registry.yarnpkg.com/p-limit/-/p-limit-3.1.0.tgz#e1daccbe78d0d1388ca18c64fea38e3e57e3706b"
  integrity sha512-TYOanM3wGwNGsZN2cVTYPArw454xnXj5qmWF1bEoAc4+cU/ol7GVh7odevjp1FNHduHc3KZMcFduxU5Xc6uJRQ==
  dependencies:
    yocto-queue "^0.1.0"

p-locate@^4.1.0:
  version "4.1.0"
  resolved "https://registry.yarnpkg.com/p-locate/-/p-locate-4.1.0.tgz#a3428bb7088b3a60292f66919278b7c297ad4f07"
  integrity sha512-R79ZZ/0wAxKGu3oYMlz8jy/kbhsNrS7SKZ7PxEHBgJ5+F2mtFW2fK2cOtBh1cHYkQsbzFV7I+EoRKe6Yt0oK7A==
  dependencies:
    p-limit "^2.2.0"

p-locate@^5.0.0:
  version "5.0.0"
  resolved "https://registry.yarnpkg.com/p-locate/-/p-locate-5.0.0.tgz#83c8315c6785005e3bd021839411c9e110e6d834"
  integrity sha512-LaNjtRWUBY++zB5nE/NwcaoMylSPk+S+ZHNB1TzdbMJMny6dynpAGt7X/tl/QYq3TIeE6nxHppbo2LGymrG5Pw==
  dependencies:
    p-limit "^3.0.2"

p-profiler@^0.2.1:
  version "0.2.1"
  resolved "https://registry.yarnpkg.com/p-profiler/-/p-profiler-0.2.1.tgz#853b5e6b482c5d376e5e2bb1e94bd09c0e715983"
  integrity sha512-/XDER5u19OrAJ283ofIgw9hsLSoyQnjzki+tmn42vdppHOfo8PgivSSZfwaiyRAzLC2h02+Q+MKiIuuSve+7nw==

p-try@^2.0.0:
  version "2.2.0"
  resolved "https://registry.yarnpkg.com/p-try/-/p-try-2.2.0.tgz#cb2868540e313d61de58fafbe35ce9004d5540e6"
  integrity sha512-R4nPAVTAU0B9D35/Gk3uJf/7XYbQcyohSKdvAxIRSNghFl4e71hVoGnBNQz9cWaXxO2I10KTC+3jMdvvoKw6dQ==

parent-module@^1.0.0:
  version "1.0.1"
  resolved "https://registry.yarnpkg.com/parent-module/-/parent-module-1.0.1.tgz#691d2709e78c79fae3a156622452d00762caaaa2"
  integrity sha512-GQ2EWRpQV8/o+Aw8YqtfZZPfNRWZYkbidE9k5rpl/hC3vtHHBfGm2Ifi6qWV+coDGkrUKZAxE3Lot5kcsRlh+g==
  dependencies:
    callsites "^3.0.0"

parse-json@^4.0.0:
  version "4.0.0"
  resolved "https://registry.yarnpkg.com/parse-json/-/parse-json-4.0.0.tgz#be35f5425be1f7f6c747184f98a788cb99477ee0"
  integrity sha512-aOIos8bujGN93/8Ox/jPLh7RwVnPEysynVFE+fQZyg6jKELEHwzgKdLRFHUgXJL6kylijVSBC4BvN9OmsB48Rw==
  dependencies:
    error-ex "^1.3.1"
    json-parse-better-errors "^1.0.1"

parse-json@^5.0.0:
  version "5.2.0"
  resolved "https://registry.yarnpkg.com/parse-json/-/parse-json-5.2.0.tgz#c76fc66dee54231c962b22bcc8a72cf2f99753cd"
  integrity sha512-ayCKvm/phCGxOkYRSCM82iDwct8/EonSEgCSxWxD7ve6jHggsFl4fZVQBPRNgQoKiuV/odhFrGzQXZwbifC8Rg==
  dependencies:
    "@babel/code-frame" "^7.0.0"
    error-ex "^1.3.1"
    json-parse-even-better-errors "^2.3.0"
    lines-and-columns "^1.1.6"

parse-path@^7.0.0:
  version "7.0.0"
  resolved "https://registry.yarnpkg.com/parse-path/-/parse-path-7.0.0.tgz#605a2d58d0a749c8594405d8cc3a2bf76d16099b"
  integrity sha512-Euf9GG8WT9CdqwuWJGdf3RkUcTBArppHABkO7Lm8IzRQp0e2r/kkFnmhu4TSK30Wcu5rVAZLmfPKSBBi9tWFog==
  dependencies:
    protocols "^2.0.0"

parse-url@^8.1.0:
  version "8.1.0"
  resolved "https://registry.yarnpkg.com/parse-url/-/parse-url-8.1.0.tgz#972e0827ed4b57fc85f0ea6b0d839f0d8a57a57d"
  integrity sha512-xDvOoLU5XRrcOZvnI6b8zA6n9O9ejNk/GExuz1yBuWUGn9KA97GI6HTs6u02wKara1CeVmZhH+0TZFdWScR89w==
  dependencies:
    parse-path "^7.0.0"

path-exists@^4.0.0:
  version "4.0.0"
  resolved "https://registry.yarnpkg.com/path-exists/-/path-exists-4.0.0.tgz#513bdbe2d3b95d7762e8c1137efa195c6c61b5b3"
  integrity sha512-ak9Qy5Q7jYb2Wwcey5Fpvg2KoAc/ZIhLSLOSBmRmygPsGwkVVt0fZa0qrtMz+m6tJTAHfZQ8FnmB4MG4LWy7/w==

path-is-absolute@^1.0.0:
  version "1.0.1"
  resolved "https://registry.yarnpkg.com/path-is-absolute/-/path-is-absolute-1.0.1.tgz#174b9268735534ffbc7ace6bf53a5a9e1b5c5f5f"
  integrity sha512-AVbw3UJ2e9bq64vSaS9Am0fje1Pa8pbGqTTsmXfaIiMpnr5DlDhfJOuLj9Sf95ZPVDAUerDfEk88MPmPe7UCQg==

path-key@^3.0.0, path-key@^3.1.0:
  version "3.1.1"
  resolved "https://registry.yarnpkg.com/path-key/-/path-key-3.1.1.tgz#581f6ade658cbba65a0d3380de7753295054f375"
  integrity sha512-ojmeN0qd+y0jszEtoY48r0Peq5dwMEkIlCOu6Q5f41lfkswXuKtYrhgoTpLnyIcHm24Uhqx+5Tqm2InSwLhE6Q==

path-parse@^1.0.6, path-parse@^1.0.7:
  version "1.0.7"
  resolved "https://registry.yarnpkg.com/path-parse/-/path-parse-1.0.7.tgz#fbc114b60ca42b30d9daf5858e4bd68bbedb6735"
  integrity sha512-LDJzPVEEEPR+y48z93A0Ed0yXb8pAByGWo/k5YYdYgpY2/2EsOsksJrq7lOHxryrVOn1ejG6oAp8ahvOIQD8sw==

path-type@^4.0.0:
  version "4.0.0"
  resolved "https://registry.yarnpkg.com/path-type/-/path-type-4.0.0.tgz#84ed01c0a7ba380afe09d90a8c180dcd9d03043b"
  integrity sha512-gDKb8aZMDeD/tZWs9P6+q0J9Mwkdl6xMV8TjnGP3qJVJ06bdMgkbBlLU8IdfOsIsFz2BW1rNVT3XuNEl8zPAvw==

picocolors@^1.0.0:
  version "1.0.0"
  resolved "https://registry.yarnpkg.com/picocolors/-/picocolors-1.0.0.tgz#cb5bdc74ff3f51892236eaf79d68bc44564ab81c"
  integrity sha512-1fygroTLlHu66zi26VoTDv8yRgm0Fccecssto+MhsZ0D/DGW2sm8E8AjW7NU5VVTRt5GxbeZ5qBuJr+HyLYkjQ==

picomatch@^2.0.4, picomatch@^2.2.1, picomatch@^2.3.1:
  version "2.3.1"
  resolved "https://registry.yarnpkg.com/picomatch/-/picomatch-2.3.1.tgz#3ba3833733646d9d3e4995946c1365a67fb07a42"
  integrity sha512-JU3teHTNjmE2VCGFzuY8EXzCDVwEqB2a8fsIvwaStHhAWJEeVd1o1QD80CU6+ZdEXXSLbSsuLwJjkCBWqRQUVA==

pify@^2.3.0:
  version "2.3.0"
  resolved "https://registry.yarnpkg.com/pify/-/pify-2.3.0.tgz#ed141a6ac043a849ea588498e7dca8b15330e90c"
  integrity sha512-udgsAY+fTnvv7kI7aaxbqwWNb0AHiB0qBO89PZKPkoTmGOgdbrHDKD+0B2X4uTfJ/FT1R09r9gTsjUjNJotuog==

pkg-dir@^4.2.0:
  version "4.2.0"
  resolved "https://registry.yarnpkg.com/pkg-dir/-/pkg-dir-4.2.0.tgz#f099133df7ede422e81d1d8448270eeb3e4261f3"
  integrity sha512-HRDzbaKjC+AOWVXxAU/x54COGeIv9eb+6CkDSQoNTt4XyWoIJvuPsXizxu/Fr23EiekbtZwmh1IcIG/l/a10GQ==
  dependencies:
    find-up "^4.0.0"

postcss-attribute-case-insensitive@^5.0.2:
  version "5.0.2"
  resolved "https://registry.yarnpkg.com/postcss-attribute-case-insensitive/-/postcss-attribute-case-insensitive-5.0.2.tgz#03d761b24afc04c09e757e92ff53716ae8ea2741"
  integrity sha512-XIidXV8fDr0kKt28vqki84fRK8VW8eTuIa4PChv2MqKuT6C9UjmSKzen6KaWhWEoYvwxFCa7n/tC1SZ3tyq4SQ==
  dependencies:
    postcss-selector-parser "^6.0.10"

postcss-clamp@^4.1.0:
  version "4.1.0"
  resolved "https://registry.yarnpkg.com/postcss-clamp/-/postcss-clamp-4.1.0.tgz#7263e95abadd8c2ba1bd911b0b5a5c9c93e02363"
  integrity sha512-ry4b1Llo/9zz+PKC+030KUnPITTJAHeOwjfAyyB60eT0AorGLdzp52s31OsPRHRf8NchkgFoG2y6fCfn1IV1Ow==
  dependencies:
    postcss-value-parser "^4.2.0"

postcss-color-functional-notation@^4.2.4:
  version "4.2.4"
  resolved "https://registry.yarnpkg.com/postcss-color-functional-notation/-/postcss-color-functional-notation-4.2.4.tgz#21a909e8d7454d3612d1659e471ce4696f28caec"
  integrity sha512-2yrTAUZUab9s6CpxkxC4rVgFEVaR6/2Pipvi6qcgvnYiVqZcbDHEoBDhrXzyb7Efh2CCfHQNtcqWcIruDTIUeg==
  dependencies:
    postcss-value-parser "^4.2.0"

postcss-color-hex-alpha@^8.0.4:
  version "8.0.4"
  resolved "https://registry.yarnpkg.com/postcss-color-hex-alpha/-/postcss-color-hex-alpha-8.0.4.tgz#c66e2980f2fbc1a63f5b079663340ce8b55f25a5"
  integrity sha512-nLo2DCRC9eE4w2JmuKgVA3fGL3d01kGq752pVALF68qpGLmx2Qrk91QTKkdUqqp45T1K1XV8IhQpcu1hoAQflQ==
  dependencies:
    postcss-value-parser "^4.2.0"

postcss-color-rebeccapurple@^7.1.1:
  version "7.1.1"
  resolved "https://registry.yarnpkg.com/postcss-color-rebeccapurple/-/postcss-color-rebeccapurple-7.1.1.tgz#63fdab91d878ebc4dd4b7c02619a0c3d6a56ced0"
  integrity sha512-pGxkuVEInwLHgkNxUc4sdg4g3py7zUeCQ9sMfwyHAT+Ezk8a4OaaVZ8lIY5+oNqA/BXXgLyXv0+5wHP68R79hg==
  dependencies:
    postcss-value-parser "^4.2.0"

postcss-custom-media@^8.0.2:
  version "8.0.2"
  resolved "https://registry.yarnpkg.com/postcss-custom-media/-/postcss-custom-media-8.0.2.tgz#c8f9637edf45fef761b014c024cee013f80529ea"
  integrity sha512-7yi25vDAoHAkbhAzX9dHx2yc6ntS4jQvejrNcC+csQJAXjj15e7VcWfMgLqBNAbOvqi5uIa9huOVwdHbf+sKqg==
  dependencies:
    postcss-value-parser "^4.2.0"

postcss-custom-properties@^12.1.10:
  version "12.1.11"
  resolved "https://registry.yarnpkg.com/postcss-custom-properties/-/postcss-custom-properties-12.1.11.tgz#d14bb9b3989ac4d40aaa0e110b43be67ac7845cf"
  integrity sha512-0IDJYhgU8xDv1KY6+VgUwuQkVtmYzRwu+dMjnmdMafXYv86SWqfxkc7qdDvWS38vsjaEtv8e0vGOUQrAiMBLpQ==
  dependencies:
    postcss-value-parser "^4.2.0"

postcss-custom-selectors@^6.0.3:
  version "6.0.3"
  resolved "https://registry.yarnpkg.com/postcss-custom-selectors/-/postcss-custom-selectors-6.0.3.tgz#1ab4684d65f30fed175520f82d223db0337239d9"
  integrity sha512-fgVkmyiWDwmD3JbpCmB45SvvlCD6z9CG6Ie6Iere22W5aHea6oWa7EM2bpnv2Fj3I94L3VbtvX9KqwSi5aFzSg==
  dependencies:
    postcss-selector-parser "^6.0.4"

postcss-dir-pseudo-class@^6.0.5:
  version "6.0.5"
  resolved "https://registry.yarnpkg.com/postcss-dir-pseudo-class/-/postcss-dir-pseudo-class-6.0.5.tgz#2bf31de5de76added44e0a25ecf60ae9f7c7c26c"
  integrity sha512-eqn4m70P031PF7ZQIvSgy9RSJ5uI2171O/OO/zcRNYpJbvaeKFUlar1aJ7rmgiQtbm0FSPsRewjpdS0Oew7MPA==
  dependencies:
    postcss-selector-parser "^6.0.10"

postcss-double-position-gradients@^3.1.2:
  version "3.1.2"
  resolved "https://registry.yarnpkg.com/postcss-double-position-gradients/-/postcss-double-position-gradients-3.1.2.tgz#b96318fdb477be95997e86edd29c6e3557a49b91"
  integrity sha512-GX+FuE/uBR6eskOK+4vkXgT6pDkexLokPaz/AbJna9s5Kzp/yl488pKPjhy0obB475ovfT1Wv8ho7U/cHNaRgQ==
  dependencies:
    "@csstools/postcss-progressive-custom-properties" "^1.1.0"
    postcss-value-parser "^4.2.0"

postcss-env-function@^4.0.6:
  version "4.0.6"
  resolved "https://registry.yarnpkg.com/postcss-env-function/-/postcss-env-function-4.0.6.tgz#7b2d24c812f540ed6eda4c81f6090416722a8e7a"
  integrity sha512-kpA6FsLra+NqcFnL81TnsU+Z7orGtDTxcOhl6pwXeEq1yFPpRMkCDpHhrz8CFQDr/Wfm0jLiNQ1OsGGPjlqPwA==
  dependencies:
    postcss-value-parser "^4.2.0"

postcss-flexbugs-fixes@^5.0.2:
  version "5.0.2"
  resolved "https://registry.yarnpkg.com/postcss-flexbugs-fixes/-/postcss-flexbugs-fixes-5.0.2.tgz#2028e145313074fc9abe276cb7ca14e5401eb49d"
  integrity sha512-18f9voByak7bTktR2QgDveglpn9DTbBWPUzSOe9g0N4WR/2eSt6Vrcbf0hmspvMI6YWGywz6B9f7jzpFNJJgnQ==

postcss-focus-visible@^6.0.4:
  version "6.0.4"
  resolved "https://registry.yarnpkg.com/postcss-focus-visible/-/postcss-focus-visible-6.0.4.tgz#50c9ea9afa0ee657fb75635fabad25e18d76bf9e"
  integrity sha512-QcKuUU/dgNsstIK6HELFRT5Y3lbrMLEOwG+A4s5cA+fx3A3y/JTq3X9LaOj3OC3ALH0XqyrgQIgey/MIZ8Wczw==
  dependencies:
    postcss-selector-parser "^6.0.9"

postcss-focus-within@^5.0.4:
  version "5.0.4"
  resolved "https://registry.yarnpkg.com/postcss-focus-within/-/postcss-focus-within-5.0.4.tgz#5b1d2ec603195f3344b716c0b75f61e44e8d2e20"
  integrity sha512-vvjDN++C0mu8jz4af5d52CB184ogg/sSxAFS+oUJQq2SuCe7T5U2iIsVJtsCp2d6R4j0jr5+q3rPkBVZkXD9fQ==
  dependencies:
    postcss-selector-parser "^6.0.9"

postcss-font-variant@^5.0.0:
  version "5.0.0"
  resolved "https://registry.yarnpkg.com/postcss-font-variant/-/postcss-font-variant-5.0.0.tgz#efd59b4b7ea8bb06127f2d031bfbb7f24d32fa66"
  integrity sha512-1fmkBaCALD72CK2a9i468mA/+tr9/1cBxRRMXOUaZqO43oWPR5imcyPjXwuv7PXbCid4ndlP5zWhidQVVa3hmA==

postcss-gap-properties@^3.0.5:
  version "3.0.5"
  resolved "https://registry.yarnpkg.com/postcss-gap-properties/-/postcss-gap-properties-3.0.5.tgz#f7e3cddcf73ee19e94ccf7cb77773f9560aa2fff"
  integrity sha512-IuE6gKSdoUNcvkGIqdtjtcMtZIFyXZhmFd5RUlg97iVEvp1BZKV5ngsAjCjrVy+14uhGBQl9tzmi1Qwq4kqVOg==

postcss-image-set-function@^4.0.7:
  version "4.0.7"
  resolved "https://registry.yarnpkg.com/postcss-image-set-function/-/postcss-image-set-function-4.0.7.tgz#08353bd756f1cbfb3b6e93182c7829879114481f"
  integrity sha512-9T2r9rsvYzm5ndsBE8WgtrMlIT7VbtTfE7b3BQnudUqnBcBo7L758oc+o+pdj/dUV0l5wjwSdjeOH2DZtfv8qw==
  dependencies:
    postcss-value-parser "^4.2.0"

postcss-import-url@^7.2.0:
  version "7.2.0"
  resolved "https://registry.yarnpkg.com/postcss-import-url/-/postcss-import-url-7.2.0.tgz#f936220b6318e9616dbf677fe38f8bede17ff358"
  integrity sha512-El61K/5+Rv753G9mBiHyQlOIN2mBfN0YHPMXLlgIo/m1+tPDLM32wd97WoUjc8FHUnC6EyyfVA8RDuKoyuVl0Q==
  dependencies:
    http-https "^1.0.0"
    is-url "^1.2.4"
    lodash.assign "^4.2.0"
    lodash.trim "^4.5.1"
    resolve-relative-url "^1.0.0"

postcss-import@^14.1.0:
  version "14.1.0"
  resolved "https://registry.yarnpkg.com/postcss-import/-/postcss-import-14.1.0.tgz#a7333ffe32f0b8795303ee9e40215dac922781f0"
  integrity sha512-flwI+Vgm4SElObFVPpTIT7SU7R3qk2L7PyduMcokiaVKuWv9d/U+Gm/QAd8NDLuykTWTkcrjOeD2Pp1rMeBTGw==
  dependencies:
    postcss-value-parser "^4.0.0"
    read-cache "^1.0.0"
    resolve "^1.1.7"

postcss-initial@^4.0.1:
  version "4.0.1"
  resolved "https://registry.yarnpkg.com/postcss-initial/-/postcss-initial-4.0.1.tgz#529f735f72c5724a0fb30527df6fb7ac54d7de42"
  integrity sha512-0ueD7rPqX8Pn1xJIjay0AZeIuDoF+V+VvMt/uOnn+4ezUKhZM/NokDeP6DwMNyIoYByuN/94IQnt5FEkaN59xQ==

postcss-js@^4.0.0:
  version "4.0.0"
  resolved "https://registry.yarnpkg.com/postcss-js/-/postcss-js-4.0.0.tgz#31db79889531b80dc7bc9b0ad283e418dce0ac00"
  integrity sha512-77QESFBwgX4irogGVPgQ5s07vLvFqWr228qZY+w6lW599cRlK/HmnlivnnVUxkjHnCu4J16PDMHcH+e+2HbvTQ==
  dependencies:
    camelcase-css "^2.0.1"

postcss-lab-function@^4.2.1:
  version "4.2.1"
  resolved "https://registry.yarnpkg.com/postcss-lab-function/-/postcss-lab-function-4.2.1.tgz#6fe4c015102ff7cd27d1bd5385582f67ebdbdc98"
  integrity sha512-xuXll4isR03CrQsmxyz92LJB2xX9n+pZJ5jE9JgcnmsCammLyKdlzrBin+25dy6wIjfhJpKBAN80gsTlCgRk2w==
  dependencies:
    "@csstools/postcss-progressive-custom-properties" "^1.1.0"
    postcss-value-parser "^4.2.0"

postcss-load-config@^2.1.2:
  version "2.1.2"
  resolved "https://registry.yarnpkg.com/postcss-load-config/-/postcss-load-config-2.1.2.tgz#c5ea504f2c4aef33c7359a34de3573772ad7502a"
  integrity sha512-/rDeGV6vMUo3mwJZmeHfEDvwnTKKqQ0S7OHUi/kJvvtx3aWtyWG2/0ZWnzCt2keEclwN6Tf0DST2v9kITdOKYw==
  dependencies:
    cosmiconfig "^5.0.0"
    import-cwd "^2.0.0"

postcss-load-config@^3.1.4:
  version "3.1.4"
  resolved "https://registry.yarnpkg.com/postcss-load-config/-/postcss-load-config-3.1.4.tgz#1ab2571faf84bb078877e1d07905eabe9ebda855"
  integrity sha512-6DiM4E7v4coTE4uzA8U//WhtPwyhiim3eyjEMFCnUpzbrkK9wJHgKDT2mR+HbtSrd/NubVaYTOpSpjUl8NQeRg==
  dependencies:
    lilconfig "^2.0.5"
    yaml "^1.10.2"

postcss-logical@^5.0.4:
  version "5.0.4"
  resolved "https://registry.yarnpkg.com/postcss-logical/-/postcss-logical-5.0.4.tgz#ec75b1ee54421acc04d5921576b7d8db6b0e6f73"
  integrity sha512-RHXxplCeLh9VjinvMrZONq7im4wjWGlRJAqmAVLXyZaXwfDWP73/oq4NdIp+OZwhQUMj0zjqDfM5Fj7qby+B4g==

postcss-media-minmax@^5.0.0:
  version "5.0.0"
  resolved "https://registry.yarnpkg.com/postcss-media-minmax/-/postcss-media-minmax-5.0.0.tgz#7140bddec173e2d6d657edbd8554a55794e2a5b5"
  integrity sha512-yDUvFf9QdFZTuCUg0g0uNSHVlJ5X1lSzDZjPSFaiCWvjgsvu8vEVxtahPrLMinIDEEGnx6cBe6iqdx5YWz08wQ==

postcss-nested@6.0.0:
  version "6.0.0"
  resolved "https://registry.yarnpkg.com/postcss-nested/-/postcss-nested-6.0.0.tgz#1572f1984736578f360cffc7eb7dca69e30d1735"
  integrity sha512-0DkamqrPcmkBDsLn+vQDIrtkSbNkv5AD/M322ySo9kqFkCIYklym2xEmWkwo+Y3/qZo34tzEPNUw4y7yMCdv5w==
  dependencies:
    postcss-selector-parser "^6.0.10"

postcss-nesting@^10.2.0:
  version "10.2.0"
  resolved "https://registry.yarnpkg.com/postcss-nesting/-/postcss-nesting-10.2.0.tgz#0b12ce0db8edfd2d8ae0aaf86427370b898890be"
  integrity sha512-EwMkYchxiDiKUhlJGzWsD9b2zvq/r2SSubcRrgP+jujMXFzqvANLt16lJANC+5uZ6hjI7lpRmI6O8JIl+8l1KA==
  dependencies:
    "@csstools/selector-specificity" "^2.0.0"
    postcss-selector-parser "^6.0.10"

postcss-opacity-percentage@^1.1.2:
  version "1.1.3"
  resolved "https://registry.yarnpkg.com/postcss-opacity-percentage/-/postcss-opacity-percentage-1.1.3.tgz#5b89b35551a556e20c5d23eb5260fbfcf5245da6"
  integrity sha512-An6Ba4pHBiDtyVpSLymUUERMo2cU7s+Obz6BTrS+gxkbnSBNKSuD0AVUc+CpBMrpVPKKfoVz0WQCX+Tnst0i4A==

postcss-overflow-shorthand@^3.0.4:
  version "3.0.4"
  resolved "https://registry.yarnpkg.com/postcss-overflow-shorthand/-/postcss-overflow-shorthand-3.0.4.tgz#7ed6486fec44b76f0eab15aa4866cda5d55d893e"
  integrity sha512-otYl/ylHK8Y9bcBnPLo3foYFLL6a6Ak+3EQBPOTR7luMYCOsiVTUk1iLvNf6tVPNGXcoL9Hoz37kpfriRIFb4A==
  dependencies:
    postcss-value-parser "^4.2.0"

postcss-page-break@^3.0.4:
  version "3.0.4"
  resolved "https://registry.yarnpkg.com/postcss-page-break/-/postcss-page-break-3.0.4.tgz#7fbf741c233621622b68d435babfb70dd8c1ee5f"
  integrity sha512-1JGu8oCjVXLa9q9rFTo4MbeeA5FMe00/9C7lN4va606Rdb+HkxXtXsmEDrIraQ11fGz/WvKWa8gMuCKkrXpTsQ==

postcss-place@^7.0.5:
  version "7.0.5"
  resolved "https://registry.yarnpkg.com/postcss-place/-/postcss-place-7.0.5.tgz#95dbf85fd9656a3a6e60e832b5809914236986c4"
  integrity sha512-wR8igaZROA6Z4pv0d+bvVrvGY4GVHihBCBQieXFY3kuSuMyOmEnnfFzHl/tQuqHZkfkIVBEbDvYcFfHmpSet9g==
  dependencies:
    postcss-value-parser "^4.2.0"

postcss-preset-env@^7.8.3:
  version "7.8.3"
  resolved "https://registry.yarnpkg.com/postcss-preset-env/-/postcss-preset-env-7.8.3.tgz#2a50f5e612c3149cc7af75634e202a5b2ad4f1e2"
  integrity sha512-T1LgRm5uEVFSEF83vHZJV2z19lHg4yJuZ6gXZZkqVsqv63nlr6zabMH3l4Pc01FQCyfWVrh2GaUeCVy9Po+Aag==
  dependencies:
    "@csstools/postcss-cascade-layers" "^1.1.1"
    "@csstools/postcss-color-function" "^1.1.1"
    "@csstools/postcss-font-format-keywords" "^1.0.1"
    "@csstools/postcss-hwb-function" "^1.0.2"
    "@csstools/postcss-ic-unit" "^1.0.1"
    "@csstools/postcss-is-pseudo-class" "^2.0.7"
    "@csstools/postcss-nested-calc" "^1.0.0"
    "@csstools/postcss-normalize-display-values" "^1.0.1"
    "@csstools/postcss-oklab-function" "^1.1.1"
    "@csstools/postcss-progressive-custom-properties" "^1.3.0"
    "@csstools/postcss-stepped-value-functions" "^1.0.1"
    "@csstools/postcss-text-decoration-shorthand" "^1.0.0"
    "@csstools/postcss-trigonometric-functions" "^1.0.2"
    "@csstools/postcss-unset-value" "^1.0.2"
    autoprefixer "^10.4.13"
    browserslist "^4.21.4"
    css-blank-pseudo "^3.0.3"
    css-has-pseudo "^3.0.4"
    css-prefers-color-scheme "^6.0.3"
    cssdb "^7.1.0"
    postcss-attribute-case-insensitive "^5.0.2"
    postcss-clamp "^4.1.0"
    postcss-color-functional-notation "^4.2.4"
    postcss-color-hex-alpha "^8.0.4"
    postcss-color-rebeccapurple "^7.1.1"
    postcss-custom-media "^8.0.2"
    postcss-custom-properties "^12.1.10"
    postcss-custom-selectors "^6.0.3"
    postcss-dir-pseudo-class "^6.0.5"
    postcss-double-position-gradients "^3.1.2"
    postcss-env-function "^4.0.6"
    postcss-focus-visible "^6.0.4"
    postcss-focus-within "^5.0.4"
    postcss-font-variant "^5.0.0"
    postcss-gap-properties "^3.0.5"
    postcss-image-set-function "^4.0.7"
    postcss-initial "^4.0.1"
    postcss-lab-function "^4.2.1"
    postcss-logical "^5.0.4"
    postcss-media-minmax "^5.0.0"
    postcss-nesting "^10.2.0"
    postcss-opacity-percentage "^1.1.2"
    postcss-overflow-shorthand "^3.0.4"
    postcss-page-break "^3.0.4"
    postcss-place "^7.0.5"
    postcss-pseudo-class-any-link "^7.1.6"
    postcss-replace-overflow-wrap "^4.0.0"
    postcss-selector-not "^6.0.1"
    postcss-value-parser "^4.2.0"

postcss-pseudo-class-any-link@^7.1.6:
  version "7.1.6"
  resolved "https://registry.yarnpkg.com/postcss-pseudo-class-any-link/-/postcss-pseudo-class-any-link-7.1.6.tgz#2693b221902da772c278def85a4d9a64b6e617ab"
  integrity sha512-9sCtZkO6f/5ML9WcTLcIyV1yz9D1rf0tWc+ulKcvV30s0iZKS/ONyETvoWsr6vnrmW+X+KmuK3gV/w5EWnT37w==
  dependencies:
    postcss-selector-parser "^6.0.10"

postcss-replace-overflow-wrap@^4.0.0:
  version "4.0.0"
  resolved "https://registry.yarnpkg.com/postcss-replace-overflow-wrap/-/postcss-replace-overflow-wrap-4.0.0.tgz#d2df6bed10b477bf9c52fab28c568b4b29ca4319"
  integrity sha512-KmF7SBPphT4gPPcKZc7aDkweHiKEEO8cla/GjcBK+ckKxiZslIu3C4GCRW3DNfL0o7yW7kMQu9xlZ1kXRXLXtw==

postcss-selector-not@^6.0.1:
  version "6.0.1"
  resolved "https://registry.yarnpkg.com/postcss-selector-not/-/postcss-selector-not-6.0.1.tgz#8f0a709bf7d4b45222793fc34409be407537556d"
  integrity sha512-1i9affjAe9xu/y9uqWH+tD4r6/hDaXJruk8xn2x1vzxC2U3J3LKO3zJW4CyxlNhA56pADJ/djpEwpH1RClI2rQ==
  dependencies:
    postcss-selector-parser "^6.0.10"

postcss-selector-parser@^6.0.10, postcss-selector-parser@^6.0.11, postcss-selector-parser@^6.0.4, postcss-selector-parser@^6.0.9:
  version "6.0.11"
  resolved "https://registry.yarnpkg.com/postcss-selector-parser/-/postcss-selector-parser-6.0.11.tgz#2e41dc39b7ad74046e1615185185cd0b17d0c8dc"
  integrity sha512-zbARubNdogI9j7WY4nQJBiNqQf3sLS3wCP4WfOidu+p28LofJqDH1tcXypGrcmMHhDk2t9wGhCsYe/+szLTy1g==
  dependencies:
    cssesc "^3.0.0"
    util-deprecate "^1.0.2"

postcss-url@^10.1.3:
  version "10.1.3"
  resolved "https://registry.yarnpkg.com/postcss-url/-/postcss-url-10.1.3.tgz#54120cc910309e2475ec05c2cfa8f8a2deafdf1e"
  integrity sha512-FUzyxfI5l2tKmXdYc6VTu3TWZsInayEKPbiyW+P6vmmIrrb4I6CGX0BFoewgYHLK+oIL5FECEK02REYRpBvUCw==
  dependencies:
    make-dir "~3.1.0"
    mime "~2.5.2"
    minimatch "~3.0.4"
    xxhashjs "~0.2.2"

postcss-value-parser@^4.0.0, postcss-value-parser@^4.2.0:
  version "4.2.0"
  resolved "https://registry.yarnpkg.com/postcss-value-parser/-/postcss-value-parser-4.2.0.tgz#723c09920836ba6d3e5af019f92bc0971c02e514"
  integrity sha512-1NNCs6uurfkVbeXG4S8JFT9t19m45ICnif8zWLd5oPSZ50QnwMfK+H3jv408d4jw/7Bttv5axS5IiHoLaVNHeQ==

postcss@8.4.14:
  version "8.4.14"
  resolved "https://registry.yarnpkg.com/postcss/-/postcss-8.4.14.tgz#ee9274d5622b4858c1007a74d76e42e56fd21caf"
  integrity sha512-E398TUmfAYFPBSdzgeieK2Y1+1cpdxJx8yXbK/m57nRhKSmk1GB2tO4lbLBtlkfPQTDKfe4Xqv1ASWPpayPEig==
  dependencies:
    nanoid "^3.3.4"
    picocolors "^1.0.0"
    source-map-js "^1.0.2"

postcss@^8.4.18, postcss@^8.4.20, postcss@^8.4.21:
  version "8.4.21"
  resolved "https://registry.yarnpkg.com/postcss/-/postcss-8.4.21.tgz#c639b719a57efc3187b13a1d765675485f4134f4"
  integrity sha512-tP7u/Sn/dVxK2NnruI4H9BG+x+Wxz6oeZ1cJ8P6G/PZY0IKk4k/63TDsQf2kQq3+qoJeLm2kIBUNlZe3zgb4Zg==
  dependencies:
    nanoid "^3.3.4"
    picocolors "^1.0.0"
    source-map-js "^1.0.2"

postcss@^8.4.24:
  version "8.4.24"
  resolved "https://registry.yarnpkg.com/postcss/-/postcss-8.4.24.tgz#f714dba9b2284be3cc07dbd2fc57ee4dc972d2df"
  integrity sha512-M0RzbcI0sO/XJNucsGjvWU9ERWxb/ytp1w6dKtxTKgixdtQDq4rmx/g8W1hnaheq9jgwL/oyEdH5Bc4WwJKMqg==
  dependencies:
    nanoid "^3.3.6"
    picocolors "^1.0.0"
    source-map-js "^1.0.2"

prelude-ls@^1.2.1:
  version "1.2.1"
  resolved "https://registry.yarnpkg.com/prelude-ls/-/prelude-ls-1.2.1.tgz#debc6489d7a6e6b0e7611888cec880337d316396"
  integrity sha512-vkcDPrRZo1QZLbn5RLGPpg/WmIQ65qoWWhcGKf/b5eplkkarX0m9z8ppCat4mlOqUsWpyNuYgO3VRyrYHSzX5g==

prettier-plugin-tailwindcss@^0.2.1:
  version "0.2.1"
  resolved "https://registry.yarnpkg.com/prettier-plugin-tailwindcss/-/prettier-plugin-tailwindcss-0.2.1.tgz#989b35afd86c550cb671da69891aba4f4a051159"
  integrity sha512-aIO8IguumORyRsmT+E7JfJ3A9FEoyhqZR7Au7TBOege3VZkgMvHJMkufeYp4zjnDK2iq4ktkvGMNOQR9T8lisQ==

prettier@^2.8.1:
  version "2.8.1"
  resolved "https://registry.yarnpkg.com/prettier/-/prettier-2.8.1.tgz#4e1fd11c34e2421bc1da9aea9bd8127cd0a35efc"
  integrity sha512-lqGoSJBQNJidqCHE80vqZJHWHRFoNYsSpP9AjFhlhi9ODCJA541svILes/+/1GM3VaL/abZi7cpFzOpdR9UPKg==

prism-react-renderer@^1.3.5:
  version "1.3.5"
  resolved "https://registry.yarnpkg.com/prism-react-renderer/-/prism-react-renderer-1.3.5.tgz#786bb69aa6f73c32ba1ee813fbe17a0115435085"
  integrity sha512-IJ+MSwBWKG+SM3b2SUfdrhC+gu01QkV2KmRQgREThBfSQRoufqRfxfHUxpG1WcaFjP+kojcFyO9Qqtpgt3qLCg==

process-nextick-args@~2.0.0:
  version "2.0.1"
  resolved "https://registry.yarnpkg.com/process-nextick-args/-/process-nextick-args-2.0.1.tgz#7820d9b16120cc55ca9ae7792680ae7dba6d7fe2"
  integrity sha512-3ouUOpQhtgrbOa17J7+uxOTpITYWaGP7/AhoR3+A+/1e9skrzelGi/dXzEYyvbxubEF6Wn2ypscTKiKJFFn1ag==

process@^0.11.10:
  version "0.11.10"
  resolved "https://registry.yarnpkg.com/process/-/process-0.11.10.tgz#7332300e840161bda3e69a1d1d91a7d4bc16f182"
  integrity sha512-cdGef/drWFoydD1JsMzuFf8100nZl+GT+yacc2bEced5f9Rjk4z+WtFUTBu9PhOi9j/jfmBPu0mMEY4wIdAF8A==

prop-types@^15.8.1:
  version "15.8.1"
  resolved "https://registry.yarnpkg.com/prop-types/-/prop-types-15.8.1.tgz#67d87bf1a694f48435cf332c24af10214a3140b5"
  integrity sha512-oj87CgZICdulUohogVAR7AjlC0327U4el4L6eAvOqCeudMDVU0NThNaV+b9Df4dXgSP1gXMTnPdhfe/2qDH5cg==
  dependencies:
    loose-envify "^1.4.0"
    object-assign "^4.1.1"
    react-is "^16.13.1"

property-information@^6.0.0:
  version "6.2.0"
  resolved "https://registry.yarnpkg.com/property-information/-/property-information-6.2.0.tgz#b74f522c31c097b5149e3c3cb8d7f3defd986a1d"
  integrity sha512-kma4U7AFCTwpqq5twzC1YVIDXSqg6qQK6JN0smOw8fgRy1OkMi0CYSzFmsy6dnqSenamAtj0CyXMUJ1Mf6oROg==

protocols@^2.0.0, protocols@^2.0.1:
  version "2.0.1"
  resolved "https://registry.yarnpkg.com/protocols/-/protocols-2.0.1.tgz#8f155da3fc0f32644e83c5782c8e8212ccf70a86"
  integrity sha512-/XJ368cyBJ7fzLMwLKv1e4vLxOju2MNAIokcr7meSaNcVbWz/CPcW22cP04mwxOErdA5mwjA8Q6w/cdAQxVn7Q==

psl@^1.1.33:
  version "1.9.0"
  resolved "https://registry.yarnpkg.com/psl/-/psl-1.9.0.tgz#d0df2a137f00794565fcaf3b2c00cd09f8d5a5a7"
  integrity sha512-E/ZsdU4HLs/68gYzgGTkMicWTLPdAftJLfJFlLUAAKZGkStNU72sZjT66SnMDVOfOWY/YAoiD7Jxa9iHvngcag==

pump@^3.0.0:
  version "3.0.0"
  resolved "https://registry.yarnpkg.com/pump/-/pump-3.0.0.tgz#b4a2116815bde2f4e1ea602354e8c75565107a64"
  integrity sha512-LwZy+p3SFs1Pytd/jYct4wpv49HiYCqd9Rlc5ZVdk0V+8Yzv6jR5Blk3TRmPL1ft69TxP0IMZGJ+WPFU2BFhww==
  dependencies:
    end-of-stream "^1.1.0"
    once "^1.3.1"

punycode@1.3.2:
  version "1.3.2"
  resolved "https://registry.yarnpkg.com/punycode/-/punycode-1.3.2.tgz#9653a036fb7c1ee42342f2325cceefea3926c48d"
  integrity sha512-RofWgt/7fL5wP1Y7fxE7/EmTLzQVnB0ycyibJ0OOHIlJqTNzglYFxVwETOcIoJqJmpDXJ9xImDv+Fq34F/d4Dw==

punycode@^2.1.0, punycode@^2.1.1:
  version "2.1.1"
  resolved "https://registry.yarnpkg.com/punycode/-/punycode-2.1.1.tgz#b58b010ac40c22c5657616c8d2c2c02c7bf479ec"
  integrity sha512-XRsRjdf+j5ml+y/6GKHPZbrF/8p2Yga0JPtdqTIY2Xe5ohJPD9saDJJLPvp9+NSBprVvevdXZybnj2cv8OEd0A==

querystring@0.2.0:
  version "0.2.0"
  resolved "https://registry.yarnpkg.com/querystring/-/querystring-0.2.0.tgz#b209849203bb25df820da756e747005878521620"
  integrity sha512-X/xY82scca2tau62i9mDyU9K+I+djTMUsvwf7xnUX5GLvVzgJybOJf4Y6o9Zx3oJK/LSXg5tTZBjwzqVPaPO2g==

querystringify@^2.1.1:
  version "2.2.0"
  resolved "https://registry.yarnpkg.com/querystringify/-/querystringify-2.2.0.tgz#3345941b4153cb9d082d8eee4cda2016a9aef7f6"
  integrity sha512-FIqgj2EUvTa7R50u0rGsyTftzjYmv/a3hO345bZNrqabNqjtgiDMgmo4mkUjd+nzU5oF3dClKqFIPUKybUyqoQ==

queue-microtask@^1.2.2:
  version "1.2.3"
  resolved "https://registry.yarnpkg.com/queue-microtask/-/queue-microtask-1.2.3.tgz#4929228bbc724dfac43e0efb058caf7b6cfb6243"
  integrity sha512-NuaNSa6flKT5JaSYQzJok04JzTL1CA6aGhv5rfLW3PgqA+M2ChpZQnAC8h8i4ZFkBS8X5RqkDBHA7r4hej3K9A==

quick-lru@^5.1.1:
  version "5.1.1"
  resolved "https://registry.yarnpkg.com/quick-lru/-/quick-lru-5.1.1.tgz#366493e6b3e42a3a6885e2e99d18f80fb7a8c932"
  integrity sha512-WuyALRjWPDGtt/wzJiadO5AXY+8hZ80hVpe6MyivgraREW751X3SbhRvG3eLKOYN+8VEvqLcf3wdnt44Z4S4SA==

react-dom@^18.2.0:
  version "18.2.0"
  resolved "https://registry.yarnpkg.com/react-dom/-/react-dom-18.2.0.tgz#22aaf38708db2674ed9ada224ca4aa708d821e3d"
  integrity sha512-6IMTriUmvsjHUjNtEDudZfuDQUoWXVxKHhlEGSk81n4YFS+r/Kl99wXiwlVXtPBtJenozv2P+hxDsw9eA7Xo6g==
  dependencies:
    loose-envify "^1.1.0"
    scheduler "^0.23.0"

react-is@^16.13.1:
  version "16.13.1"
  resolved "https://registry.yarnpkg.com/react-is/-/react-is-16.13.1.tgz#789729a4dc36de2999dc156dd6c1d9c18cea56a4"
  integrity sha512-24e6ynE2H+OKt4kqsOvNd8kBpV65zoxbA4BVsEOB3ARVWQki/DHzaUoC5KuON/BiccDaCCTZBuOcfZs70kR8bQ==

react@^18.2.0:
  version "18.2.0"
  resolved "https://registry.yarnpkg.com/react/-/react-18.2.0.tgz#555bd98592883255fa00de14f1151a917b5d77d5"
  integrity sha512-/3IjMdb2L9QbBdWiW5e3P2/npwMBaU9mHCSCUzNln0ZCYbcfTsGbTJrU/kGemdH2IWmB2ioZ+zkxtmq6g09fGQ==
  dependencies:
    loose-envify "^1.1.0"

read-cache@^1.0.0:
  version "1.0.0"
  resolved "https://registry.yarnpkg.com/read-cache/-/read-cache-1.0.0.tgz#e664ef31161166c9751cdbe8dbcf86b5fb58f774"
  integrity sha512-Owdv/Ft7IjOgm/i0xvNDZ1LrRANRfew4b2prF3OWMQLxLfu3bS8FVhCsrSCMK4lR56Y9ya+AThoTpDCTxCmpRA==
  dependencies:
    pify "^2.3.0"

readable-stream@^2.0.6:
  version "2.3.7"
  resolved "https://registry.yarnpkg.com/readable-stream/-/readable-stream-2.3.7.tgz#1eca1cf711aef814c04f62252a36a62f6cb23b57"
  integrity sha512-Ebho8K4jIbHAxnuxi7o42OrZgF/ZTNcsZj6nRKyUmkhLFq8CHItp/fy6hQZuZmP/n3yZ9VBUbp4zz/mX8hmYPw==
  dependencies:
    core-util-is "~1.0.0"
    inherits "~2.0.3"
    isarray "~1.0.0"
    process-nextick-args "~2.0.0"
    safe-buffer "~5.1.1"
    string_decoder "~1.1.1"
    util-deprecate "~1.0.1"

readable-stream@^3.1.1, readable-stream@^3.4.0:
  version "3.6.0"
  resolved "https://registry.yarnpkg.com/readable-stream/-/readable-stream-3.6.0.tgz#337bbda3adc0706bd3e024426a286d4b4b2c9198"
  integrity sha512-BViHy7LKeTz4oNnkcLJ+lVSL6vpiFeX6/d3oSH8zCW7UxP2onchk+vTGB143xuFjHS3deTgkKoXXymXqymiIdA==
  dependencies:
    inherits "^2.0.3"
    string_decoder "^1.1.1"
    util-deprecate "^1.0.1"

readdirp@~3.6.0:
  version "3.6.0"
  resolved "https://registry.yarnpkg.com/readdirp/-/readdirp-3.6.0.tgz#74a370bd857116e245b29cc97340cd431a02a6c7"
  integrity sha512-hOS089on8RduqdbhvQ5Z37A0ESjsqz6qnRcffsMU3495FuTdqSm+7bhJ29JvIOsBDEEnan5DPu9t3To9VRlMzA==
  dependencies:
    picomatch "^2.2.1"

regenerate-unicode-properties@^10.1.0:
  version "10.1.0"
  resolved "https://registry.yarnpkg.com/regenerate-unicode-properties/-/regenerate-unicode-properties-10.1.0.tgz#7c3192cab6dd24e21cb4461e5ddd7dd24fa8374c"
  integrity sha512-d1VudCLoIGitcU/hEg2QqvyGZQmdC0Lf8BqdOMXGFSvJP4bNV1+XqbPQeHHLD51Jh4QJJ225dlIFvY4Ly6MXmQ==
  dependencies:
    regenerate "^1.4.2"

regenerate@^1.4.2:
  version "1.4.2"
  resolved "https://registry.yarnpkg.com/regenerate/-/regenerate-1.4.2.tgz#b9346d8827e8f5a32f7ba29637d398b69014848a"
  integrity sha512-zrceR/XhGYU/d/opr2EKO7aRHUeiBI8qjtfHqADTwZd6Szfy16la6kqD0MIUs5z5hx6AaKa+PixpPrR289+I0A==

regenerator-runtime@^0.13.11:
  version "0.13.11"
  resolved "https://registry.yarnpkg.com/regenerator-runtime/-/regenerator-runtime-0.13.11.tgz#f6dca3e7ceec20590d07ada785636a90cdca17f9"
  integrity sha512-kY1AZVr2Ra+t+piVaJ4gxaFaReZVH40AKNo7UCX6W+dEwBo/2oZJzqfuN1qLq1oL45o56cPaTXELwrTh8Fpggg==

regenerator-transform@^0.15.1:
  version "0.15.1"
  resolved "https://registry.yarnpkg.com/regenerator-transform/-/regenerator-transform-0.15.1.tgz#f6c4e99fc1b4591f780db2586328e4d9a9d8dc56"
  integrity sha512-knzmNAcuyxV+gQCufkYcvOqX/qIIfHLv0u5x79kRxuGojfYVky1f15TzZEu2Avte8QGepvUNTnLskf8E6X6Vyg==
  dependencies:
    "@babel/runtime" "^7.8.4"

regexp.prototype.flags@^1.4.3:
  version "1.4.3"
  resolved "https://registry.yarnpkg.com/regexp.prototype.flags/-/regexp.prototype.flags-1.4.3.tgz#87cab30f80f66660181a3bb7bf5981a872b367ac"
  integrity sha512-fjggEOO3slI6Wvgjwflkc4NFRCTZAu5CnNfBd5qOMYhWdn67nJBBu34/TkD++eeFmd8C9r9jfXJ27+nSiRkSUA==
  dependencies:
    call-bind "^1.0.2"
    define-properties "^1.1.3"
    functions-have-names "^1.2.2"

regexpp@^3.2.0:
  version "3.2.0"
  resolved "https://registry.yarnpkg.com/regexpp/-/regexpp-3.2.0.tgz#0425a2768d8f23bad70ca4b90461fa2f1213e1b2"
  integrity sha512-pq2bWo9mVD43nbts2wGv17XLiNLya+GklZ8kaDLV2Z08gDCsGpnKn9BFMepvWuHCbyVvY7J5o5+BVvoQbmlJLg==

regexpu-core@^5.2.1:
  version "5.2.2"
  resolved "https://registry.yarnpkg.com/regexpu-core/-/regexpu-core-5.2.2.tgz#3e4e5d12103b64748711c3aad69934d7718e75fc"
  integrity sha512-T0+1Zp2wjF/juXMrMxHxidqGYn8U4R+zleSJhX9tQ1PUsS8a9UtYfbsF9LdiVgNX3kiX8RNaKM42nfSgvFJjmw==
  dependencies:
    regenerate "^1.4.2"
    regenerate-unicode-properties "^10.1.0"
    regjsgen "^0.7.1"
    regjsparser "^0.9.1"
    unicode-match-property-ecmascript "^2.0.0"
    unicode-match-property-value-ecmascript "^2.1.0"

regjsgen@^0.7.1:
  version "0.7.1"
  resolved "https://registry.yarnpkg.com/regjsgen/-/regjsgen-0.7.1.tgz#ee5ef30e18d3f09b7c369b76e7c2373ed25546f6"
  integrity sha512-RAt+8H2ZEzHeYWxZ3H2z6tF18zyyOnlcdaafLrm21Bguj7uZy6ULibiAFdXEtKQY4Sy7wDTwDiOazasMLc4KPA==

regjsparser@^0.9.1:
  version "0.9.1"
  resolved "https://registry.yarnpkg.com/regjsparser/-/regjsparser-0.9.1.tgz#272d05aa10c7c1f67095b1ff0addae8442fc5709"
  integrity sha512-dQUtn90WanSNl+7mQKcXAgZxvUe7Z0SqXlgzv0za4LwiUhyzBC58yQO3liFoUgu8GiJVInAhJjkj1N0EtQ5nkQ==
  dependencies:
    jsesc "~0.5.0"

remark-gfm@^3.0.0:
  version "3.0.1"
  resolved "https://registry.yarnpkg.com/remark-gfm/-/remark-gfm-3.0.1.tgz#0b180f095e3036545e9dddac0e8df3fa5cfee54f"
  integrity sha512-lEFDoi2PICJyNrACFOfDD3JlLkuSbOa5Wd8EPt06HUdptv8Gn0bxYTdbU/XXQ3swAPkEaGxxPN9cbnMHvVu1Ig==
  dependencies:
    "@types/mdast" "^3.0.0"
    mdast-util-gfm "^2.0.0"
    micromark-extension-gfm "^2.0.0"
    unified "^10.0.0"

remark-parse@^10.0.0:
  version "10.0.1"
  resolved "https://registry.yarnpkg.com/remark-parse/-/remark-parse-10.0.1.tgz#6f60ae53edbf0cf38ea223fe643db64d112e0775"
  integrity sha512-1fUyHr2jLsVOkhbvPRBJ5zTKZZyD6yZzYaWCS6BPBdQ8vEMBCH+9zNCDA6tET/zHCi/jLqjCWtlJZUPk+DbnFw==
  dependencies:
    "@types/mdast" "^3.0.0"
    mdast-util-from-markdown "^1.0.0"
    unified "^10.0.0"

remark-react@^9.0.1:
  version "9.0.1"
  resolved "https://registry.yarnpkg.com/remark-react/-/remark-react-9.0.1.tgz#6412116737a7547bc572eedc56f93c48c320b5e1"
  integrity sha512-NtpTMfUIreelaRdUVUtgSizTOSwV6JQvGAPn2gWNoWF+Etd0D8YUdDDFEV3vVOiMIoiNR2bQ0etMb/9uaWhjAw==
  dependencies:
    "@mapbox/hast-util-table-cell-style" "^0.2.0"
    "@types/mdast" "^3.0.0"
    "@types/react" "^17.0.0"
    hast-to-hyperscript "^10.0.0"
    hast-util-sanitize "^4.0.0"
    mdast-util-to-hast "^11.0.0"
    unified "^10.0.0"

remark-slug@^7.0.0:
  version "7.0.1"
  resolved "https://registry.yarnpkg.com/remark-slug/-/remark-slug-7.0.1.tgz#9827ce6d6ee81ca82b79891b0e5931a8123ce63b"
  integrity sha512-NRvYePr69LdeCkEGwL4KYAmq7kdWG5rEavCXMzUR4qndLoXHJAOLSUmPY6Qm4NJfKix7/EmgObyVaYivONAFhg==
  dependencies:
    "@types/hast" "^2.3.2"
    "@types/mdast" "^3.0.0"
    github-slugger "^1.0.0"
    mdast-util-to-string "^3.0.0"
    unified "^10.0.0"
    unist-util-visit "^4.0.0"

require-directory@^2.1.1:
  version "2.1.1"
  resolved "https://registry.yarnpkg.com/require-directory/-/require-directory-2.1.1.tgz#8c64ad5fd30dab1c976e2344ffe7f792a6a6df42"
  integrity sha512-fGxEI7+wsG9xrvdjsrlmL22OMTTiHRwAMroiEeMgq8gzoLC/PQr7RsRDSTLUg/bZAZtF+TVIkHc6/4RIKrui+Q==

requires-port@^1.0.0:
  version "1.0.0"
  resolved "https://registry.yarnpkg.com/requires-port/-/requires-port-1.0.0.tgz#925d2601d39ac485e091cf0da5c6e694dc3dcaff"
  integrity sha512-KigOCHcocU3XODJxsu8i/j8T9tzT4adHiecwORRQ0ZZFcp7ahwXuRU1m+yuO90C5ZUyGeGfocHDI14M3L3yDAQ==

resolve-from@^3.0.0:
  version "3.0.0"
  resolved "https://registry.yarnpkg.com/resolve-from/-/resolve-from-3.0.0.tgz#b22c7af7d9d6881bc8b6e653335eebcb0a188748"
  integrity sha512-GnlH6vxLymXJNMBo7XP1fJIzBFbdYt49CuTwmB/6N53t+kMPRMFKz783LlQ4tv28XoQfMWinAJX6WCGf2IlaIw==

resolve-from@^4.0.0:
  version "4.0.0"
  resolved "https://registry.yarnpkg.com/resolve-from/-/resolve-from-4.0.0.tgz#4abcd852ad32dd7baabfe9b40e00a36db5f392e6"
  integrity sha512-pb/MYmXstAkysRFx8piNI1tGFNQIFA3vkE3Gq4EuA1dF6gHp/+vgZqsCGJapvy8N3Q+4o7FwvquPJcnZ7RYy4g==

resolve-relative-url@^1.0.0:
  version "1.0.0"
  resolved "https://registry.yarnpkg.com/resolve-relative-url/-/resolve-relative-url-1.0.0.tgz#d896e9555e0aee9d2e0180f406014bde3c9157c9"
  integrity sha512-zpcelQBAmrwckiyRmym9os1goECU3EzuTU/UrYkGzXV0i14n8FkyGUvwkOYA5klqVLq1Hz/EiFZMS7bZQdd+EA==
  dependencies:
    url "0.10.x"

resolve@^1.1.7, resolve@^1.14.2, resolve@^1.20.0, resolve@^1.22.0, resolve@^1.22.1:
  version "1.22.1"
  resolved "https://registry.yarnpkg.com/resolve/-/resolve-1.22.1.tgz#27cb2ebb53f91abb49470a928bba7558066ac177"
  integrity sha512-nBpuuYuY5jFsli/JIs1oldw6fOQCBioohqWZg/2hiaOybXOft4lonv85uDOKXdf8rhyK159cxU5cDcK/NKk8zw==
  dependencies:
    is-core-module "^2.9.0"
    path-parse "^1.0.7"
    supports-preserve-symlinks-flag "^1.0.0"

resolve@^2.0.0-next.3:
  version "2.0.0-next.4"
  resolved "https://registry.yarnpkg.com/resolve/-/resolve-2.0.0-next.4.tgz#3d37a113d6429f496ec4752d2a2e58efb1fd4660"
  integrity sha512-iMDbmAWtfU+MHpxt/I5iWI7cY6YVEZUQ3MBgPQ++XD1PELuJHIl82xBmObyP2KyQmkNB2dsqF7seoQQiAn5yDQ==
  dependencies:
    is-core-module "^2.9.0"
    path-parse "^1.0.7"
    supports-preserve-symlinks-flag "^1.0.0"

resolve@~1.17.0:
  version "1.17.0"
  resolved "https://registry.yarnpkg.com/resolve/-/resolve-1.17.0.tgz#b25941b54968231cc2d1bb76a79cb7f2c0bf8444"
  integrity sha512-ic+7JYiV8Vi2yzQGFWOkiZD5Z9z7O2Zhm9XMaTxdJExKasieFCr+yXZ/WmXsckHiKl12ar0y6XiXDx3m4RHn1w==
  dependencies:
    path-parse "^1.0.6"

reusify@^1.0.4:
  version "1.0.4"
  resolved "https://registry.yarnpkg.com/reusify/-/reusify-1.0.4.tgz#90da382b1e126efc02146e90845a88db12925d76"
  integrity sha512-U9nH88a3fc/ekCF1l0/UP1IosiuIjyTh7hBvXVMHYgVcfGvt897Xguj2UOLDeI5BG2m7/uwyaLVT6fbtCwTyzw==

rimraf@^3.0.2:
  version "3.0.2"
  resolved "https://registry.yarnpkg.com/rimraf/-/rimraf-3.0.2.tgz#f1a5402ba6220ad52cc1282bac1ae3aa49fd061a"
  integrity sha512-JZkJMZkAGFFPP2YqXZXPbMlMBgsxzE8ILs4lMIX/2o0L9UBw9O/Y3o6wFw/i9YLapcUJWwqbi3kdxIPdC62TIA==
  dependencies:
    glob "^7.1.3"

run-parallel@^1.1.9:
  version "1.2.0"
  resolved "https://registry.yarnpkg.com/run-parallel/-/run-parallel-1.2.0.tgz#66d1368da7bdf921eb9d95bd1a9229e7f21a43ee"
  integrity sha512-5l4VyZR86LZ/lDxZTR6jqL8AFE2S0IFLMP26AbjsLVADxHdhB/c0GUsH+y39UfCi3dzz8OlQuPmnaJOMoDHQBA==
  dependencies:
    queue-microtask "^1.2.2"

sade@^1.7.3:
  version "1.8.1"
  resolved "https://registry.yarnpkg.com/sade/-/sade-1.8.1.tgz#0a78e81d658d394887be57d2a409bf703a3b2701"
  integrity sha512-xal3CZX1Xlo/k4ApwCFrHVACi9fBqJ7V+mwhBsuf/1IOKbBy098Fex+Wa/5QMubw09pSZ/u8EY8PWgevJsXp1A==
  dependencies:
    mri "^1.1.0"

safe-buffer@~5.1.0, safe-buffer@~5.1.1:
  version "5.1.2"
  resolved "https://registry.yarnpkg.com/safe-buffer/-/safe-buffer-5.1.2.tgz#991ec69d296e0313747d59bdfd2b745c35f8828d"
  integrity sha512-Gd2UZBJDkXlY7GbJxfsE8/nvKkUEU1G38c1siN6QP6a9PT9MmHB8GnpscSmMJSoF8LOIrt8ud/wPtojys4G6+g==

safe-buffer@~5.2.0:
  version "5.2.1"
  resolved "https://registry.yarnpkg.com/safe-buffer/-/safe-buffer-5.2.1.tgz#1eaf9fa9bdb1fdd4ec75f58f9cdb4e6b7827eec6"
  integrity sha512-rp3So07KcdmmKbGvgaNxQSJr7bGVSVk5S9Eq1F+ppbRo70+YeaDxkw5Dd8NPN+GD6bjnYm2VuPuCXmpuYvmCXQ==

safe-regex-test@^1.0.0:
  version "1.0.0"
  resolved "https://registry.yarnpkg.com/safe-regex-test/-/safe-regex-test-1.0.0.tgz#793b874d524eb3640d1873aad03596db2d4f2295"
  integrity sha512-JBUUzyOgEwXQY1NuPtvcj/qcBDbDmEvWufhlnXZIm75DEHp+afM1r1ujJpJsV/gSM4t59tpDyPi1sd6ZaPFfsA==
  dependencies:
    call-bind "^1.0.2"
    get-intrinsic "^1.1.3"
    is-regex "^1.1.4"

sax@>=0.6.0:
  version "1.2.4"
  resolved "https://registry.yarnpkg.com/sax/-/sax-1.2.4.tgz#2816234e2378bddc4e5354fab5caa895df7100d9"
  integrity sha512-NqVDv9TpANUjFm0N8uM5GxL36UgKi9/atZw+x7YFnQ8ckwFGKrl4xX4yWtrey3UJm5nP1kUbnYgLopqWNSRhWw==

scheduler@^0.23.0:
  version "0.23.0"
  resolved "https://registry.yarnpkg.com/scheduler/-/scheduler-0.23.0.tgz#ba8041afc3d30eb206a487b6b384002e4e61fdfe"
  integrity sha512-CtuThmgHNg7zIZWAXi3AsyIzA3n4xx7aNyjwC2VJldO2LMVDhFK+63xGqq6CsJH4rTAt6/M+N4GhZiDYPx9eUw==
  dependencies:
    loose-envify "^1.1.0"

schema-utils@^3.0.0:
  version "3.1.1"
  resolved "https://registry.yarnpkg.com/schema-utils/-/schema-utils-3.1.1.tgz#bc74c4b6b6995c1d88f76a8b77bea7219e0c8281"
  integrity sha512-Y5PQxS4ITlC+EahLuXaY86TXfR7Dc5lw294alXOq86JAHCihAIZfqv8nNCWvaEJvaC51uN9hbLGeV0cFBdH+Fw==
  dependencies:
    "@types/json-schema" "^7.0.8"
    ajv "^6.12.5"
    ajv-keywords "^3.5.2"

section-matter@^1.0.0:
  version "1.0.0"
  resolved "https://registry.yarnpkg.com/section-matter/-/section-matter-1.0.0.tgz#e9041953506780ec01d59f292a19c7b850b84167"
  integrity sha512-vfD3pmTzGpufjScBh50YHKzEu2lxBWhVEHsNGoEXmCmn2hKGfeNLYMzCJpe8cD7gqX7TJluOVpBkAequ6dgMmA==
  dependencies:
    extend-shallow "^2.0.1"
    kind-of "^6.0.0"

semver@^6.0.0, semver@^6.1.1, semver@^6.1.2, semver@^6.3.0:
  version "6.3.0"
  resolved "https://registry.yarnpkg.com/semver/-/semver-6.3.0.tgz#ee0a64c8af5e8ceea67687b133761e1becbd1d3d"
  integrity sha512-b39TBaTSfV6yBrapU89p5fKekE2m/NwnDocOVruQFS1/veMgdzuPcnOM34M6CwxW8jH/lxEa5rBoDeUwu5HHTw==

semver@^7.3.7, semver@~7.3.0:
  version "7.3.8"
  resolved "https://registry.yarnpkg.com/semver/-/semver-7.3.8.tgz#07a78feafb3f7b32347d725e33de7e2a2df67798"
  integrity sha512-NB1ctGL5rlHrPJtFDVIVzTyQylMLu9N9VICA6HSFJo8MCGVTMW6gfpicwKmmK/dAjTOrqu5l63JJOpDSrAis3A==
  dependencies:
    lru-cache "^6.0.0"

set-blocking@~2.0.0:
  version "2.0.0"
  resolved "https://registry.yarnpkg.com/set-blocking/-/set-blocking-2.0.0.tgz#045f9782d011ae9a6803ddd382b24392b3d890f7"
  integrity sha512-KiKBS8AnWGEyLzofFfmvKwpdPzqiy16LvQfK3yv/fVH7Bj13/wl3JSR1J+rfgRE9q7xUJK4qvgS8raSOeLUehw==

shebang-command@^2.0.0:
  version "2.0.0"
  resolved "https://registry.yarnpkg.com/shebang-command/-/shebang-command-2.0.0.tgz#ccd0af4f8835fbdc265b82461aaf0c36663f34ea"
  integrity sha512-kHxr2zZpYtdmrN1qDjrrX/Z1rR1kG8Dx+gkpK1G4eXmvXswmcE1hTWBWYUzlraYw1/yZp6YuDY77YtvbN0dmDA==
  dependencies:
    shebang-regex "^3.0.0"

shebang-regex@^3.0.0:
  version "3.0.0"
  resolved "https://registry.yarnpkg.com/shebang-regex/-/shebang-regex-3.0.0.tgz#ae16f1644d873ecad843b0307b143362d4c42172"
  integrity sha512-7++dFhtcx3353uBaq8DDR4NuxBetBzC7ZQOhmTQInHEd6bSrXdiEyzCvG07Z44UYdLShWUyXt5M/yhz8ekcb1A==

side-channel@^1.0.4:
  version "1.0.4"
  resolved "https://registry.yarnpkg.com/side-channel/-/side-channel-1.0.4.tgz#efce5c8fdc104ee751b25c58d4290011fa5ea2cf"
  integrity sha512-q5XPytqFEIKHkGdiMIrY10mvLRvnQh42/+GoBlFW3b2LXLE2xxJpZFdm94we0BaoV3RwJyGqg5wS7epxTv0Zvw==
  dependencies:
    call-bind "^1.0.0"
    get-intrinsic "^1.0.2"
    object-inspect "^1.9.0"

signal-exit@^3.0.0, signal-exit@^3.0.3:
  version "3.0.7"
  resolved "https://registry.yarnpkg.com/signal-exit/-/signal-exit-3.0.7.tgz#a9a1767f8af84155114eaabd73f99273c8f59ad9"
  integrity sha512-wnD2ZE+l+SPC/uoS0vXeE9L1+0wuaMqKlfz9AMUo38JsyLSBWSFcHR1Rri62LZc12vLr1gb3jl7iwQhgwpAbGQ==

simple-swizzle@^0.2.2:
  version "0.2.2"
  resolved "https://registry.yarnpkg.com/simple-swizzle/-/simple-swizzle-0.2.2.tgz#a4da6b635ffcccca33f70d17cb92592de95e557a"
  integrity sha512-JA//kQgZtbuY83m+xT+tXJkmJncGMTFT+C+g2h2R9uxkYIrE2yy9sgmcLhCnw57/WSD+Eh3J97FPEDFnbXnDUg==
  dependencies:
    is-arrayish "^0.3.1"

sirv@^1.0.7:
  version "1.0.19"
  resolved "https://registry.yarnpkg.com/sirv/-/sirv-1.0.19.tgz#1d73979b38c7fe91fcba49c85280daa9c2363b49"
  integrity sha512-JuLThK3TnZG1TAKDwNIqNq6QA2afLOCcm+iE8D1Kj3GA40pSPsxQjjJl0J8X3tsR7T+CP1GavpzLwYkgVLWrZQ==
  dependencies:
    "@polka/url" "^1.0.0-next.20"
    mrmime "^1.0.0"
    totalist "^1.0.0"

slash@^3.0.0:
  version "3.0.0"
  resolved "https://registry.yarnpkg.com/slash/-/slash-3.0.0.tgz#6539be870c165adbd5240220dbe361f1bc4d4634"
  integrity sha512-g9Q1haeby36OSStwb4ntCGGGaKsaVSjQ68fBxoQcutl5fS1vuY18H3wSt3jFyFtrkx+Kz0V1G85A4MyAdDMi2Q==

slash@^4.0.0:
  version "4.0.0"
  resolved "https://registry.yarnpkg.com/slash/-/slash-4.0.0.tgz#2422372176c4c6c5addb5e2ada885af984b396a7"
  integrity sha512-3dOsAHXXUkQTpOYcoAxLIorMTp4gIQr5IW3iVb7A7lFIp0VHhnynm9izx6TssdrIcVIESAlVjtnO2K8bg+Coew==

source-map-js@^1.0.2:
  version "1.0.2"
  resolved "https://registry.yarnpkg.com/source-map-js/-/source-map-js-1.0.2.tgz#adbc361d9c62df380125e7f161f71c826f1e490c"
  integrity sha512-R0XvVJ9WusLiqTCEiGCmICCMplcCkIwwR11mOSD9CR5u+IXYdiseeEuXCVAjS54zqwkLcPNnmU4OeJ6tUrWhDw==

source-map@^0.6.1:
  version "0.6.1"
  resolved "https://registry.yarnpkg.com/source-map/-/source-map-0.6.1.tgz#74722af32e9614e9c287a8d0bbde48b5e2f1a263"
  integrity sha512-UjgapumWlbMhkBgzT7Ykc5YXUT46F0iKu8SGXq0bcwP5dz/h0Plj6enJqjz1Zbq2l5WaqYnrVbwWOWMyF3F47g==

space-separated-tokens@^2.0.0:
  version "2.0.2"
  resolved "https://registry.yarnpkg.com/space-separated-tokens/-/space-separated-tokens-2.0.2.tgz#1ecd9d2350a3844572c3f4a312bceb018348859f"
  integrity sha512-PEGlAwrG8yXGXRjW32fGbg66JAlOAwbObuqVoJpv/mRgoWDQfgH1wDPvtzWyUSNAXBGSk8h755YDbbcEy3SH2Q==

speech-rule-engine@^4.0.6:
  version "4.0.7"
  resolved "https://registry.yarnpkg.com/speech-rule-engine/-/speech-rule-engine-4.0.7.tgz#b655dacbad3dae04acc0f7665e26ef258397dd09"
  integrity sha512-sJrL3/wHzNwJRLBdf6CjJWIlxC04iYKkyXvYSVsWVOiC2DSkHmxsqOhEeMsBA9XK+CHuNcsdkbFDnoUfAsmp9g==
  dependencies:
    commander "9.2.0"
    wicked-good-xpath "1.3.0"
    xmldom-sre "0.1.31"

sprintf-js@~1.0.2:
  version "1.0.3"
  resolved "https://registry.yarnpkg.com/sprintf-js/-/sprintf-js-1.0.3.tgz#04e6926f662895354f3dd015203633b857297e2c"
  integrity sha512-D9cPgkvLlV3t3IzL0D0YLvGA9Ahk4PcvVwUbN0dSGr1aP0Nrt4AEnTUbuGvquEC0mA64Gqt1fzirlRs5ibXx8g==

ssr-window@^4.0.0, ssr-window@^4.0.2:
  version "4.0.2"
  resolved "https://registry.yarnpkg.com/ssr-window/-/ssr-window-4.0.2.tgz#dc6b3ee37be86ac0e3ddc60030f7b3bc9b8553be"
  integrity sha512-ISv/Ch+ig7SOtw7G2+qkwfVASzazUnvlDTwypdLoPoySv+6MqlOV10VwPSE6EWkGjhW50lUmghPmpYZXMu/+AQ==

stable@^0.1.8:
  version "0.1.8"
  resolved "https://registry.yarnpkg.com/stable/-/stable-0.1.8.tgz#836eb3c8382fe2936feaf544631017ce7d47a3cf"
  integrity sha512-ji9qxRnOVfcuLDySj9qzhGSEFVobyt1kIOSkj1qZzYLzq7Tos/oUUWvotUPQLlrsidqsK6tBH89Bc9kL5zHA6w==

string-width@^1.0.1:
  version "1.0.2"
  resolved "https://registry.yarnpkg.com/string-width/-/string-width-1.0.2.tgz#118bdf5b8cdc51a2a7e70d211e07e2b0b9b107d3"
  integrity sha512-0XsVpQLnVCXHJfyEs8tC0zpTVIr5PKKsQtkT29IwupnPTjtPmQ3xT/4yCREF9hYkV/3M3kzcUTSAZT6a6h81tw==
  dependencies:
    code-point-at "^1.0.0"
    is-fullwidth-code-point "^1.0.0"
    strip-ansi "^3.0.0"

"string-width@^1.0.2 || 2 || 3 || 4", string-width@^4.1.0, string-width@^4.2.0:
  version "4.2.3"
  resolved "https://registry.yarnpkg.com/string-width/-/string-width-4.2.3.tgz#269c7117d27b05ad2e536830a8ec895ef9c6d010"
  integrity sha512-wKyQRQpjJ0sIp62ErSZdGsjMJWsap5oRNihHhu6G7JVO/9jIB6UyevL+tXuOqrng8j/cxKTWyWUwvSTriiZz/g==
  dependencies:
    emoji-regex "^8.0.0"
    is-fullwidth-code-point "^3.0.0"
    strip-ansi "^6.0.1"

string.prototype.matchall@^4.0.8:
  version "4.0.8"
  resolved "https://registry.yarnpkg.com/string.prototype.matchall/-/string.prototype.matchall-4.0.8.tgz#3bf85722021816dcd1bf38bb714915887ca79fd3"
  integrity sha512-6zOCOcJ+RJAQshcTvXPHoxoQGONa3e/Lqx90wUA+wEzX78sg5Bo+1tQo4N0pohS0erG9qtCqJDjNCQBjeWVxyg==
  dependencies:
    call-bind "^1.0.2"
    define-properties "^1.1.4"
    es-abstract "^1.20.4"
    get-intrinsic "^1.1.3"
    has-symbols "^1.0.3"
    internal-slot "^1.0.3"
    regexp.prototype.flags "^1.4.3"
    side-channel "^1.0.4"

string.prototype.trimend@^1.0.6:
  version "1.0.6"
  resolved "https://registry.yarnpkg.com/string.prototype.trimend/-/string.prototype.trimend-1.0.6.tgz#c4a27fa026d979d79c04f17397f250a462944533"
  integrity sha512-JySq+4mrPf9EsDBEDYMOb/lM7XQLulwg5R/m1r0PXEFqrV0qHvl58sdTilSXtKOflCsK2E8jxf+GKC0T07RWwQ==
  dependencies:
    call-bind "^1.0.2"
    define-properties "^1.1.4"
    es-abstract "^1.20.4"

string.prototype.trimstart@^1.0.6:
  version "1.0.6"
  resolved "https://registry.yarnpkg.com/string.prototype.trimstart/-/string.prototype.trimstart-1.0.6.tgz#e90ab66aa8e4007d92ef591bbf3cd422c56bdcf4"
  integrity sha512-omqjMDaY92pbn5HOX7f9IccLA+U1tA9GvtU4JrodiXFfYB7jPzzHpRzpglLAjtUV6bB557zwClJezTqnAiYnQA==
  dependencies:
    call-bind "^1.0.2"
    define-properties "^1.1.4"
    es-abstract "^1.20.4"

string_decoder@^1.1.1:
  version "1.3.0"
  resolved "https://registry.yarnpkg.com/string_decoder/-/string_decoder-1.3.0.tgz#42f114594a46cf1a8e30b0a84f56c78c3edac21e"
  integrity sha512-hkRX8U1WjJFd8LsDJ2yQ/wWWxaopEsABU1XfkM8A+j0+85JAGppt16cr1Whg6KIbb4okU6Mql6BOj+uup/wKeA==
  dependencies:
    safe-buffer "~5.2.0"

string_decoder@~1.1.1:
  version "1.1.1"
  resolved "https://registry.yarnpkg.com/string_decoder/-/string_decoder-1.1.1.tgz#9cf1611ba62685d7030ae9e4ba34149c3af03fc8"
  integrity sha512-n/ShnvDi6FHbbVfviro+WojiFzv+s8MPMHBczVePfUpDJLwoLT0ht1l4YwBCbi8pJAveEEdnkHyPyTP/mzRfwg==
  dependencies:
    safe-buffer "~5.1.0"

strip-ansi@^3.0.0, strip-ansi@^3.0.1:
  version "3.0.1"
  resolved "https://registry.yarnpkg.com/strip-ansi/-/strip-ansi-3.0.1.tgz#6a385fb8853d952d5ff05d0e8aaf94278dc63dcf"
  integrity sha512-VhumSSbBqDTP8p2ZLKj40UjBCV4+v8bUSEpUb4KjRgWk9pbqGF4REFj6KEagidb2f/M6AzC0EmFyDNGaw9OCzg==
  dependencies:
    ansi-regex "^2.0.0"

strip-ansi@^6.0.0, strip-ansi@^6.0.1:
  version "6.0.1"
  resolved "https://registry.yarnpkg.com/strip-ansi/-/strip-ansi-6.0.1.tgz#9e26c63d30f53443e9489495b2105d37b67a85d9"
  integrity sha512-Y38VPSHcqkFrCpFnQ9vuSXmquuv5oXOKpGeT6aGrr3o3Gc9AlVa6JBfUSOCnbxGGZF+/0ooI7KrPuUSztUdU5A==
  dependencies:
    ansi-regex "^5.0.1"

strip-bom-string@^1.0.0:
  version "1.0.0"
  resolved "https://registry.yarnpkg.com/strip-bom-string/-/strip-bom-string-1.0.0.tgz#e5211e9224369fbb81d633a2f00044dc8cedad92"
  integrity sha512-uCC2VHvQRYu+lMh4My/sFNmF2klFymLX1wHJeXnbEJERpV/ZsVuonzerjfrGpIGF7LBVa1O7i9kjiWvJiFck8g==

strip-bom@^3.0.0:
  version "3.0.0"
  resolved "https://registry.yarnpkg.com/strip-bom/-/strip-bom-3.0.0.tgz#2334c18e9c759f7bdd56fdef7e9ae3d588e68ed3"
  integrity sha512-vavAMRXOgBVNF6nyEEmL3DBK19iRpDcoIwW+swQ+CbGiu7lju6t+JklA1MHweoWtadgt4ISVUsXLyDq34ddcwA==

strip-final-newline@^2.0.0:
  version "2.0.0"
  resolved "https://registry.yarnpkg.com/strip-final-newline/-/strip-final-newline-2.0.0.tgz#89b852fb2fcbe936f6f4b3187afb0a12c1ab58ad"
  integrity sha512-BrpvfNAE3dcvq7ll3xVumzjKjZQ5tI1sEUIKr3Uoks0XUl45St3FlatVqef9prk4jRDzhW6WZg+3bk93y6pLjA==

strip-json-comments@^3.1.0, strip-json-comments@^3.1.1:
  version "3.1.1"
  resolved "https://registry.yarnpkg.com/strip-json-comments/-/strip-json-comments-3.1.1.tgz#31f1281b3832630434831c310c01cccda8cbe006"
  integrity sha512-6fPc+R4ihwqP6N/aIv2f1gMH8lOVtWQHoqC4yK6oSDVVocumAsfCqjkXnqiYMhmMwS/mEHLp7Vehlt3ql6lEig==

strip-outer@^1.0.1:
  version "1.0.1"
  resolved "https://registry.yarnpkg.com/strip-outer/-/strip-outer-1.0.1.tgz#b2fd2abf6604b9d1e6013057195df836b8a9d631"
  integrity sha512-k55yxKHwaXnpYGsOzg4Vl8+tDrWylxDEpknGjhTiZB8dFRU5rTo9CAzeycivxV3s+zlTKwrs6WxMxR95n26kwg==
  dependencies:
    escape-string-regexp "^1.0.2"

style-to-object@^0.3.0:
  version "0.3.0"
  resolved "https://registry.yarnpkg.com/style-to-object/-/style-to-object-0.3.0.tgz#b1b790d205991cc783801967214979ee19a76e46"
  integrity sha512-CzFnRRXhzWIdItT3OmF8SQfWyahHhjq3HwcMNCNLn+N7klOOqPjMeG/4JSu77D7ypZdGvSzvkrbyeTMizz2VrA==
  dependencies:
    inline-style-parser "0.1.1"

styled-jsx-plugin-postcss@^4.0.1:
  version "4.0.1"
  resolved "https://registry.yarnpkg.com/styled-jsx-plugin-postcss/-/styled-jsx-plugin-postcss-4.0.1.tgz#d1980db5f3af9bd662236822d02db3e80017371d"
  integrity sha512-Qy3OnewWZYykT0ESWRqqC7KhYSghXpel+cnY3/MOnmatEwvJl1+RB5YwJRjqhcODDoY/D+dKH97PZFuF3/rCBg==
  dependencies:
    postcss-load-config "^2.1.2"

styled-jsx@5.1.1:
  version "5.1.1"
  resolved "https://registry.yarnpkg.com/styled-jsx/-/styled-jsx-5.1.1.tgz#839a1c3aaacc4e735fed0781b8619ea5d0009d1f"
  integrity sha512-pW7uC1l4mBZ8ugbiZrcIsiIvVx1UmTfw7UkC3Um2tmfUq9Bhk8IiyEIPl6F8agHgjzku6j0xQEZbfA5uSgSaCw==
  dependencies:
    client-only "0.0.1"

supports-color@^5.3.0:
  version "5.5.0"
  resolved "https://registry.yarnpkg.com/supports-color/-/supports-color-5.5.0.tgz#e2e69a44ac8772f78a1ec0b35b689df6530efc8f"
  integrity sha512-QjVjwdXIt408MIiAqCX4oUKsgU2EqAGzs2Ppkm4aQYbjm+ZEWEcW4SfFNTr4uMNZma0ey4f5lgLrkB0aX0QMow==
  dependencies:
    has-flag "^3.0.0"

supports-color@^7.1.0:
  version "7.2.0"
  resolved "https://registry.yarnpkg.com/supports-color/-/supports-color-7.2.0.tgz#1b7dcdcb32b8138801b3e478ba6a51caa89648da"
  integrity sha512-qpCAvRl9stuOHveKsn7HncJRvv501qIacKzQlO/+Lwxc9+0q2wLyv4Dfvt80/DPn2pqOBsJdDiogXGR9+OvwRw==
  dependencies:
    has-flag "^4.0.0"

supports-preserve-symlinks-flag@^1.0.0:
  version "1.0.0"
  resolved "https://registry.yarnpkg.com/supports-preserve-symlinks-flag/-/supports-preserve-symlinks-flag-1.0.0.tgz#6eda4bd344a3c94aea376d4cc31bc77311039e09"
  integrity sha512-ot0WnXS9fgdkgIcePe6RHNk1WA8+muPa6cSjeR3V8K27q9BB1rTE3R1p7Hv0z1ZyAc8s6Vvv8DIyWf681MAt0w==

svg-parser@^2.0.4:
  version "2.0.4"
  resolved "https://registry.yarnpkg.com/svg-parser/-/svg-parser-2.0.4.tgz#fdc2e29e13951736140b76cb122c8ee6630eb6b5"
  integrity sha512-e4hG1hRwoOdRb37cIMSgzNsxyzKfayW6VOflrwvR+/bzrkyxY/31WkbgnQpgtrNp1SdpJvpUAGTa/ZoiPNDuRQ==

svgo@^2.8.0:
  version "2.8.0"
  resolved "https://registry.yarnpkg.com/svgo/-/svgo-2.8.0.tgz#4ff80cce6710dc2795f0c7c74101e6764cfccd24"
  integrity sha512-+N/Q9kV1+F+UeWYoSiULYo4xYSDQlTgb+ayMobAXPwMnLvop7oxKMo9OzIrX5x3eS4L4f2UHhc9axXwY8DpChg==
  dependencies:
    "@trysound/sax" "0.2.0"
    commander "^7.2.0"
    css-select "^4.1.3"
    css-tree "^1.1.3"
    csso "^4.2.0"
    picocolors "^1.0.0"
    stable "^0.1.8"

swiper@^8.4.5:
  version "8.4.5"
  resolved "https://registry.yarnpkg.com/swiper/-/swiper-8.4.5.tgz#149ca81f67393d3f33abddd0f968fc37e99980b5"
  integrity sha512-zveyEFBBv4q1sVkbJHnuH4xCtarKieavJ4SxP0QEHvdpPLJRuD7j/Xg38IVVLbp7Db6qrPsLUePvxohYx39Agw==
  dependencies:
    dom7 "^4.0.4"
    ssr-window "^4.0.2"

synckit@^0.8.4:
  version "0.8.4"
  resolved "https://registry.yarnpkg.com/synckit/-/synckit-0.8.4.tgz#0e6b392b73fafdafcde56692e3352500261d64ec"
  integrity sha512-Dn2ZkzMdSX827QbowGbU/4yjWuvNaCoScLLoMo/yKbu+P4GBR6cRGKZH27k6a9bRzdqcyd1DE96pQtQ6uNkmyw==
  dependencies:
    "@pkgr/utils" "^2.3.1"
    tslib "^2.4.0"

tabbable@^6.0.1:
  version "6.0.1"
  resolved "https://registry.yarnpkg.com/tabbable/-/tabbable-6.0.1.tgz#427a09b13c83ae41eed3e88abb76a4af28bde1a6"
  integrity sha512-SYJSIgeyXW7EuX1ytdneO5e8jip42oHWg9xl/o3oTYhmXusZVgiA+VlPvjIN+kHii9v90AmzTZEBcsEvuAY+TA==

tailwindcss@^3.2.4:
  version "3.2.4"
  resolved "https://registry.yarnpkg.com/tailwindcss/-/tailwindcss-3.2.4.tgz#afe3477e7a19f3ceafb48e4b083e292ce0dc0250"
  integrity sha512-AhwtHCKMtR71JgeYDaswmZXhPcW9iuI9Sp2LvZPo9upDZ7231ZJ7eA9RaURbhpXGVlrjX4cFNlB4ieTetEb7hQ==
  dependencies:
    arg "^5.0.2"
    chokidar "^3.5.3"
    color-name "^1.1.4"
    detective "^5.2.1"
    didyoumean "^1.2.2"
    dlv "^1.1.3"
    fast-glob "^3.2.12"
    glob-parent "^6.0.2"
    is-glob "^4.0.3"
    lilconfig "^2.0.6"
    micromatch "^4.0.5"
    normalize-path "^3.0.0"
    object-hash "^3.0.0"
    picocolors "^1.0.0"
    postcss "^8.4.18"
    postcss-import "^14.1.0"
    postcss-js "^4.0.0"
    postcss-load-config "^3.1.4"
    postcss-nested "6.0.0"
    postcss-selector-parser "^6.0.10"
    postcss-value-parser "^4.2.0"
    quick-lru "^5.1.1"
    resolve "^1.22.1"

tapable@^2.2.0:
  version "2.2.1"
  resolved "https://registry.yarnpkg.com/tapable/-/tapable-2.2.1.tgz#1967a73ef4060a82f12ab96af86d52fdb76eeca0"
  integrity sha512-GNzQvQTOIP6RyTfE2Qxb8ZVlNmw0n88vp1szwWRimP02mnTsx3Wtn5qRdqY9w2XduFNUgvOwhNnQsjwCp+kqaQ==

tar-fs@^2.1.0:
  version "2.1.1"
  resolved "https://registry.yarnpkg.com/tar-fs/-/tar-fs-2.1.1.tgz#489a15ab85f1f0befabb370b7de4f9eb5cbe8784"
  integrity sha512-V0r2Y9scmbDRLCNex/+hYzvp/zyYjvFbHPNgVTKfQvVrb6guiE/fxP+XblDNR011utopbkex2nM4dHNV6GDsng==
  dependencies:
    chownr "^1.1.1"
    mkdirp-classic "^0.5.2"
    pump "^3.0.0"
    tar-stream "^2.1.4"

tar-stream@^2.1.4:
  version "2.2.0"
  resolved "https://registry.yarnpkg.com/tar-stream/-/tar-stream-2.2.0.tgz#acad84c284136b060dc3faa64474aa9aebd77287"
  integrity sha512-ujeqbceABgwMZxEJnk2HDY2DlnUZ+9oEcb1KzTVfYHio0UE6dG71n60d8D2I4qNvleWrrXpmjpt7vZeF1LnMZQ==
  dependencies:
    bl "^4.0.3"
    end-of-stream "^1.4.1"
    fs-constants "^1.0.0"
    inherits "^2.0.3"
    readable-stream "^3.1.1"

text-table@^0.2.0:
  version "0.2.0"
  resolved "https://registry.yarnpkg.com/text-table/-/text-table-0.2.0.tgz#7f5ee823ae805207c00af2df4a84ec3fcfa570b4"
  integrity sha512-N+8UisAXDGk8PFXP4HAzVR9nbfmVJ3zYLAWiTIoqC5v5isinhr+r5uaO8+7r3BMfuNIufIsA7RdpVgacC2cSpw==

tiny-glob@^0.2.9:
  version "0.2.9"
  resolved "https://registry.yarnpkg.com/tiny-glob/-/tiny-glob-0.2.9.tgz#2212d441ac17928033b110f8b3640683129d31e2"
  integrity sha512-g/55ssRPUjShh+xkfx9UPDXqhckHEsHr4Vd9zX55oSdGZc/MD0m3sferOkwWtp98bv+kcVfEHtRJgBVJzelrzg==
  dependencies:
    globalyzer "0.1.0"
    globrex "^0.1.2"

to-fast-properties@^2.0.0:
  version "2.0.0"
  resolved "https://registry.yarnpkg.com/to-fast-properties/-/to-fast-properties-2.0.0.tgz#dc5e698cbd079265bc73e0377681a4e4e83f616e"
  integrity sha512-/OaKK0xYrs3DmxRYqL/yDc+FxFUVYhDlXMhRmv3z915w2HF1tnN1omB354j8VUGO/hbRzyD6Y3sA7v7GS/ceog==

to-regex-range@^5.0.1:
  version "5.0.1"
  resolved "https://registry.yarnpkg.com/to-regex-range/-/to-regex-range-5.0.1.tgz#1648c44aae7c8d988a326018ed72f5b4dd0392e4"
  integrity sha512-65P7iz6X5yEr1cwcgvQxbbIw7Uk3gOy5dIdtZ4rDveLqhrdJP+Li/Hx6tyK0NEb+2GCyneCMJiGqrADCSNk8sQ==
  dependencies:
    is-number "^7.0.0"

totalist@^1.0.0:
  version "1.1.0"
  resolved "https://registry.yarnpkg.com/totalist/-/totalist-1.1.0.tgz#a4d65a3e546517701e3e5c37a47a70ac97fe56df"
  integrity sha512-gduQwd1rOdDMGxFG1gEvhV88Oirdo2p+KjoYFU7k2g+i7n6AFFbDQ5kMPUsW0pNbfQsB/cwXvT1i4Bue0s9g5g==

tough-cookie@^4.0.0:
  version "4.1.2"
  resolved "https://registry.yarnpkg.com/tough-cookie/-/tough-cookie-4.1.2.tgz#e53e84b85f24e0b65dd526f46628db6c85f6b874"
  integrity sha512-G9fqXWoYFZgTc2z8Q5zaHy/vJMjm+WV0AkAeHxVCQiEB1b+dGvWzFW6QV07cY5jQ5gRkeid2qIkzkxUnmoQZUQ==
  dependencies:
    psl "^1.1.33"
    punycode "^2.1.1"
    universalify "^0.2.0"
    url-parse "^1.5.3"

tr46@~0.0.3:
  version "0.0.3"
  resolved "https://registry.yarnpkg.com/tr46/-/tr46-0.0.3.tgz#8184fd347dac9cdc185992f3a6622e14b9d9ab6a"
  integrity sha512-N3WMsuqV66lT30CrXNbEjx4GEwlow3v6rr4mCcv6prnfwhS01rkgyFdjPNBYd9br7LpXV1+Emh01fHnq2Gdgrw==

trim-repeated@^1.0.0:
  version "1.0.0"
  resolved "https://registry.yarnpkg.com/trim-repeated/-/trim-repeated-1.0.0.tgz#e3646a2ea4e891312bf7eace6cfb05380bc01c21"
  integrity sha512-pkonvlKk8/ZuR0D5tLW8ljt5I8kmxp2XKymhepUeOdCEfKpZaktSArkLHZt76OB1ZvO9bssUsDty4SWhLvZpLg==
  dependencies:
    escape-string-regexp "^1.0.2"

trough@^2.0.0:
  version "2.1.0"
  resolved "https://registry.yarnpkg.com/trough/-/trough-2.1.0.tgz#0f7b511a4fde65a46f18477ab38849b22c554876"
  integrity sha512-AqTiAOLcj85xS7vQ8QkAV41hPDIJ71XJB4RCUrzo/1GM2CQwhkJGaf9Hgr7BOugMRpgGUrqRg/DrBDl4H40+8g==

tsconfig-paths@^3.14.1:
  version "3.14.1"
  resolved "https://registry.yarnpkg.com/tsconfig-paths/-/tsconfig-paths-3.14.1.tgz#ba0734599e8ea36c862798e920bcf163277b137a"
  integrity sha512-fxDhWnFSLt3VuTwtvJt5fpwxBHg5AdKWMsgcPOOIilyjymcYVZoCQF8fvFRezCNfblEXmi+PcM1eYHeOAgXCOQ==
  dependencies:
    "@types/json5" "^0.0.29"
    json5 "^1.0.1"
    minimist "^1.2.6"
    strip-bom "^3.0.0"

tslib@^1.10.0, tslib@^1.8.1:
  version "1.14.1"
  resolved "https://registry.yarnpkg.com/tslib/-/tslib-1.14.1.tgz#cf2d38bdc34a134bcaf1091c41f6619e2f672d00"
  integrity sha512-Xni35NKzjgMrwevysHTCArtLDpPvye8zV/0E4EyYn43P7/7qvQwPh9BGkHewbMulVntbigmcT7rdX3BNo9wRJg==

tslib@^2.0.0, tslib@^2.2.0, tslib@^2.4.0:
  version "2.4.1"
  resolved "https://registry.yarnpkg.com/tslib/-/tslib-2.4.1.tgz#0d0bfbaac2880b91e22df0768e55be9753a5b17e"
  integrity sha512-tGyy4dAjRIEwI7BzsB0lynWgOpfqjUdq91XXAlIWD2OwKBH7oCl/GZG/HT4BOHrTlPMOASlMQ7veyTqpmRcrNA==

tsutils@^3.21.0:
  version "3.21.0"
  resolved "https://registry.yarnpkg.com/tsutils/-/tsutils-3.21.0.tgz#b48717d394cea6c1e096983eed58e9d61715b623"
  integrity sha512-mHKK3iUXL+3UF6xL5k0PEhKRUBKPBCv/+RkEOpjRWxxx27KKRBmmA60A9pgOUvMi8GKhRMPEmjBRPzs2W7O1OA==
  dependencies:
    tslib "^1.8.1"

tunnel@^0.0.6:
  version "0.0.6"
  resolved "https://registry.yarnpkg.com/tunnel/-/tunnel-0.0.6.tgz#72f1314b34a5b192db012324df2cc587ca47f92c"
  integrity sha512-1h/Lnq9yajKY2PEbBadPXj3VxsDDu844OnaAo52UVmIzIvwwtBPIuNvkjuzBlTWpfJyUbG3ez0KSBibQkj4ojg==

type-check@^0.4.0, type-check@~0.4.0:
  version "0.4.0"
  resolved "https://registry.yarnpkg.com/type-check/-/type-check-0.4.0.tgz#07b8203bfa7056c0657050e3ccd2c37730bab8f1"
  integrity sha512-XleUoc9uwGXqjWwXaUTZAmzMcFZ5858QA2vvx1Ur5xIcixXIP+8LnFDgRplU30us6teqdlskFfu+ae4K79Ooew==
  dependencies:
    prelude-ls "^1.2.1"

type-fest@^0.20.2:
  version "0.20.2"
  resolved "https://registry.yarnpkg.com/type-fest/-/type-fest-0.20.2.tgz#1bf207f4b28f91583666cb5fbd327887301cd5f4"
  integrity sha512-Ne+eE4r0/iWnpAxD852z3A+N0Bt5RN//NjJwRd2VFHEmrywxf5vsZlh4R6lixl6B+wz/8d+maTSAkN1FIkI3LQ==

type-fest@^2.11.2:
  version "2.19.0"
  resolved "https://registry.yarnpkg.com/type-fest/-/type-fest-2.19.0.tgz#88068015bb33036a598b952e55e9311a60fd3a9b"
  integrity sha512-RAH822pAdBgcNMAfWnCBU3CFZcfZ/i1eZjwFU/dsLKumyuuP3niueg2UAukXYF0E2AAoc82ZSSf9J0WQBinzHA==

typescript@^4.9.4:
  version "4.9.4"
  resolved "https://registry.yarnpkg.com/typescript/-/typescript-4.9.4.tgz#a2a3d2756c079abda241d75f149df9d561091e78"
  integrity sha512-Uz+dTXYzxXXbsFpM86Wh3dKCxrQqUcVMxwU54orwlJjOpO3ao8L7j5lH+dWfTwgCwIuM9GQ2kvVotzYJMXTBZg==

uc.micro@^1.0.1, uc.micro@^1.0.5:
  version "1.0.6"
  resolved "https://registry.yarnpkg.com/uc.micro/-/uc.micro-1.0.6.tgz#9c411a802a409a91fc6cf74081baba34b24499ac"
  integrity sha512-8Y75pvTYkLJW2hWQHXxoqRgV7qb9B+9vFEtidML+7koHUFapnVJAZ6cKs+Qjz5Aw3aZWHMC6u0wJE3At+nSGwA==

unbox-primitive@^1.0.2:
  version "1.0.2"
  resolved "https://registry.yarnpkg.com/unbox-primitive/-/unbox-primitive-1.0.2.tgz#29032021057d5e6cdbd08c5129c226dff8ed6f9e"
  integrity sha512-61pPlCD9h51VoreyJ0BReideM3MDKMKnh6+V9L08331ipq6Q8OFXZYiqP6n/tbHx4s5I9uRhcye6BrbkizkBDw==
  dependencies:
    call-bind "^1.0.2"
    has-bigints "^1.0.2"
    has-symbols "^1.0.3"
    which-boxed-primitive "^1.0.2"

unicode-canonical-property-names-ecmascript@^2.0.0:
  version "2.0.0"
  resolved "https://registry.yarnpkg.com/unicode-canonical-property-names-ecmascript/-/unicode-canonical-property-names-ecmascript-2.0.0.tgz#301acdc525631670d39f6146e0e77ff6bbdebddc"
  integrity sha512-yY5PpDlfVIU5+y/BSCxAJRBIS1Zc2dDG3Ujq+sR0U+JjUevW2JhocOF+soROYDSaAezOzOKuyyixhD6mBknSmQ==

unicode-match-property-ecmascript@^2.0.0:
  version "2.0.0"
  resolved "https://registry.yarnpkg.com/unicode-match-property-ecmascript/-/unicode-match-property-ecmascript-2.0.0.tgz#54fd16e0ecb167cf04cf1f756bdcc92eba7976c3"
  integrity sha512-5kaZCrbp5mmbz5ulBkDkbY0SsPOjKqVS35VpL9ulMPfSl0J0Xsm+9Evphv9CoIZFwre7aJoa94AY6seMKGVN5Q==
  dependencies:
    unicode-canonical-property-names-ecmascript "^2.0.0"
    unicode-property-aliases-ecmascript "^2.0.0"

unicode-match-property-value-ecmascript@^2.1.0:
  version "2.1.0"
  resolved "https://registry.yarnpkg.com/unicode-match-property-value-ecmascript/-/unicode-match-property-value-ecmascript-2.1.0.tgz#cb5fffdcd16a05124f5a4b0bf7c3770208acbbe0"
  integrity sha512-qxkjQt6qjg/mYscYMC0XKRn3Rh0wFPlfxB0xkt9CfyTvpX1Ra0+rAmdX2QyAobptSEvuy4RtpPRui6XkV+8wjA==

unicode-property-aliases-ecmascript@^2.0.0:
  version "2.1.0"
  resolved "https://registry.yarnpkg.com/unicode-property-aliases-ecmascript/-/unicode-property-aliases-ecmascript-2.1.0.tgz#43d41e3be698bd493ef911077c9b131f827e8ccd"
  integrity sha512-6t3foTQI9qne+OZoVQB/8x8rk2k1eVy1gRXhV3oFQ5T6R1dqQ1xtin3XqSlx3+ATBkliTaR/hHyJBm+LVPNM8w==

unified@^10.0.0, unified@^10.1.2:
  version "10.1.2"
  resolved "https://registry.yarnpkg.com/unified/-/unified-10.1.2.tgz#b1d64e55dafe1f0b98bb6c719881103ecf6c86df"
  integrity sha512-pUSWAi/RAnVy1Pif2kAoeWNBa3JVrx0MId2LASj8G+7AiHWoKZNTomq6LG326T68U7/e263X6fTdcXIy7XnF7Q==
  dependencies:
    "@types/unist" "^2.0.0"
    bail "^2.0.0"
    extend "^3.0.0"
    is-buffer "^2.0.0"
    is-plain-obj "^4.0.0"
    trough "^2.0.0"
    vfile "^5.0.0"

unist-builder@^3.0.0:
  version "3.0.0"
  resolved "https://registry.yarnpkg.com/unist-builder/-/unist-builder-3.0.0.tgz#728baca4767c0e784e1e64bb44b5a5a753021a04"
  integrity sha512-GFxmfEAa0vi9i5sd0R2kcrI9ks0r82NasRq5QHh2ysGngrc6GiqD5CDf1FjPenY4vApmFASBIIlk/jj5J5YbmQ==
  dependencies:
    "@types/unist" "^2.0.0"

unist-util-generated@^2.0.0:
  version "2.0.0"
  resolved "https://registry.yarnpkg.com/unist-util-generated/-/unist-util-generated-2.0.0.tgz#86fafb77eb6ce9bfa6b663c3f5ad4f8e56a60113"
  integrity sha512-TiWE6DVtVe7Ye2QxOVW9kqybs6cZexNwTwSMVgkfjEReqy/xwGpAXb99OxktoWwmL+Z+Epb0Dn8/GNDYP1wnUw==

unist-util-is@^3.0.0:
  version "3.0.0"
  resolved "https://registry.yarnpkg.com/unist-util-is/-/unist-util-is-3.0.0.tgz#d9e84381c2468e82629e4a5be9d7d05a2dd324cd"
  integrity sha512-sVZZX3+kspVNmLWBPAB6r+7D9ZgAFPNWm66f7YNb420RlQSbn+n8rG8dGZSkrER7ZIXGQYNm5pqC3v3HopH24A==

unist-util-is@^5.0.0:
  version "5.1.1"
  resolved "https://registry.yarnpkg.com/unist-util-is/-/unist-util-is-5.1.1.tgz#e8aece0b102fa9bc097b0fef8f870c496d4a6236"
  integrity sha512-F5CZ68eYzuSvJjGhCLPL3cYx45IxkqXSetCcRgUXtbcm50X2L9oOWQlfUfDdAf+6Pd27YDblBfdtmsThXmwpbQ==

unist-util-position@^4.0.0:
  version "4.0.3"
  resolved "https://registry.yarnpkg.com/unist-util-position/-/unist-util-position-4.0.3.tgz#5290547b014f6222dff95c48d5c3c13a88fadd07"
  integrity sha512-p/5EMGIa1qwbXjA+QgcBXaPWjSnZfQ2Sc3yBEEfgPwsEmJd8Qh+DSk3LGnmOM4S1bY2C0AjmMnB8RuEYxpPwXQ==
  dependencies:
    "@types/unist" "^2.0.0"

unist-util-remove-position@^4.0.1:
  version "4.0.1"
  resolved "https://registry.yarnpkg.com/unist-util-remove-position/-/unist-util-remove-position-4.0.1.tgz#d5b46a7304ac114c8d91990ece085ca7c2c135c8"
  integrity sha512-0yDkppiIhDlPrfHELgB+NLQD5mfjup3a8UYclHruTJWmY74je8g+CIFr79x5f6AkmzSwlvKLbs63hC0meOMowQ==
  dependencies:
    "@types/unist" "^2.0.0"
    unist-util-visit "^4.0.0"

unist-util-stringify-position@^3.0.0:
  version "3.0.2"
  resolved "https://registry.yarnpkg.com/unist-util-stringify-position/-/unist-util-stringify-position-3.0.2.tgz#5c6aa07c90b1deffd9153be170dce628a869a447"
  integrity sha512-7A6eiDCs9UtjcwZOcCpM4aPII3bAAGv13E96IkawkOAW0OhH+yRxtY0lzo8KiHpzEMfH7Q+FizUmwp8Iqy5EWg==
  dependencies:
    "@types/unist" "^2.0.0"

unist-util-visit-parents@^2.0.0:
  version "2.1.2"
  resolved "https://registry.yarnpkg.com/unist-util-visit-parents/-/unist-util-visit-parents-2.1.2.tgz#25e43e55312166f3348cae6743588781d112c1e9"
  integrity sha512-DyN5vD4NE3aSeB+PXYNKxzGsfocxp6asDc2XXE3b0ekO2BaRUpBicbbUygfSvYfUz1IkmjFR1YF7dPklraMZ2g==
  dependencies:
    unist-util-is "^3.0.0"

unist-util-visit-parents@^5.0.0, unist-util-visit-parents@^5.1.1:
  version "5.1.1"
  resolved "https://registry.yarnpkg.com/unist-util-visit-parents/-/unist-util-visit-parents-5.1.1.tgz#868f353e6fce6bf8fa875b251b0f4fec3be709bb"
  integrity sha512-gks4baapT/kNRaWxuGkl5BIhoanZo7sC/cUT/JToSRNL1dYoXRFl75d++NkjYk4TAu2uv2Px+l8guMajogeuiw==
  dependencies:
    "@types/unist" "^2.0.0"
    unist-util-is "^5.0.0"

unist-util-visit@^1.4.1:
  version "1.4.1"
  resolved "https://registry.yarnpkg.com/unist-util-visit/-/unist-util-visit-1.4.1.tgz#4724aaa8486e6ee6e26d7ff3c8685960d560b1e3"
  integrity sha512-AvGNk7Bb//EmJZyhtRUnNMEpId/AZ5Ph/KUpTI09WHQuDZHKovQ1oEv3mfmKpWKtoMzyMC4GLBm1Zy5k12fjIw==
  dependencies:
    unist-util-visit-parents "^2.0.0"

unist-util-visit@^4.0.0, unist-util-visit@^4.1.1:
  version "4.1.1"
  resolved "https://registry.yarnpkg.com/unist-util-visit/-/unist-util-visit-4.1.1.tgz#1c4842d70bd3df6cc545276f5164f933390a9aad"
  integrity sha512-n9KN3WV9k4h1DxYR1LoajgN93wpEi/7ZplVe02IoB4gH5ctI1AaF2670BLHQYbwj+pY83gFtyeySFiyMHJklrg==
  dependencies:
    "@types/unist" "^2.0.0"
    unist-util-is "^5.0.0"
    unist-util-visit-parents "^5.1.1"

universalify@^0.1.0:
  version "0.1.2"
  resolved "https://registry.yarnpkg.com/universalify/-/universalify-0.1.2.tgz#b646f69be3942dabcecc9d6639c80dc105efaa66"
  integrity sha512-rBJeI5CXAlmy1pV+617WB9J63U6XcazHHF2f2dbJix4XzpUF0RS3Zbj0FGIOCAva5P/d/GBOYaACQ1w+0azUkg==

universalify@^0.2.0:
  version "0.2.0"
  resolved "https://registry.yarnpkg.com/universalify/-/universalify-0.2.0.tgz#6451760566fa857534745ab1dde952d1b1761be0"
  integrity sha512-CJ1QgKmNg3CwvAv/kOFmtnEN05f0D/cn9QntgNOQlQF9dgvVTHj3t+8JPdjqawCHk7V/KA+fbUqzZ9XWhcqPUg==

update-browserslist-db@^1.0.9:
  version "1.0.10"
  resolved "https://registry.yarnpkg.com/update-browserslist-db/-/update-browserslist-db-1.0.10.tgz#0f54b876545726f17d00cd9a2561e6dade943ff3"
  integrity sha512-OztqDenkfFkbSG+tRxBeAnCVPckDBcvibKd35yDONx6OU8N7sqgwc7rCbkJ/WcYtVRZ4ba68d6byhC21GFh7sQ==
  dependencies:
    escalade "^3.1.1"
    picocolors "^1.0.0"

uri-js@^4.2.2:
  version "4.4.1"
  resolved "https://registry.yarnpkg.com/uri-js/-/uri-js-4.4.1.tgz#9b1a52595225859e55f669d928f88c6c57f2a77e"
  integrity sha512-7rKUyy33Q1yc98pQ1DAmLtwX109F7TIfWlW1Ydo8Wl1ii1SeHieeh0HHfPeL2fMXK6z0s8ecKs9frCuLJvndBg==
  dependencies:
    punycode "^2.1.0"

url-parse@^1.5.3:
  version "1.5.10"
  resolved "https://registry.yarnpkg.com/url-parse/-/url-parse-1.5.10.tgz#9d3c2f736c1d75dd3bd2be507dcc111f1e2ea9c1"
  integrity sha512-WypcfiRhfeUP9vvF0j6rw0J3hrWrw6iZv3+22h6iRMJ/8z1Tj6XfLP4DsUix5MhMPnXpiHDoKyoZ/bdCkwBCiQ==
  dependencies:
    querystringify "^2.1.1"
    requires-port "^1.0.0"

url@0.10.x:
  version "0.10.3"
  resolved "https://registry.yarnpkg.com/url/-/url-0.10.3.tgz#021e4d9c7705f21bbf37d03ceb58767402774c64"
  integrity sha512-hzSUW2q06EqL1gKM/a+obYHLIO6ct2hwPuviqTTOcfFVc61UbfJ2Q32+uGL/HCPxKqrdGB5QUwIe7UqlDgwsOQ==
  dependencies:
    punycode "1.3.2"
    querystring "0.2.0"

use-media@^1.4.0:
  version "1.4.0"
  resolved "https://registry.yarnpkg.com/use-media/-/use-media-1.4.0.tgz#e777bf1f382a7aacabbd1f9ce3da2b62e58b2a98"
  integrity sha512-XsgyUAf3nhzZmEfhc5MqLHwyaPjs78bgytpVJ/xDl0TF4Bptf3vEpBNBBT/EIKOmsOc8UbuECq3mrP3mt1QANA==

util-deprecate@^1.0.1, util-deprecate@^1.0.2, util-deprecate@~1.0.1:
  version "1.0.2"
  resolved "https://registry.yarnpkg.com/util-deprecate/-/util-deprecate-1.0.2.tgz#450d4dc9fa70de732762fbd2d4a28981419a0ccf"
  integrity sha512-EPD5q1uXyFxJpCrLnCc1nHnq3gOa6DZBocAIiI2TaSCA7VCJ1UJDMagCzIkXNsUYfD1daK//LTEQ8xiIbrHtcw==

uuid@^8.3.0:
  version "8.3.2"
  resolved "https://registry.yarnpkg.com/uuid/-/uuid-8.3.2.tgz#80d5b5ced271bb9af6c445f21a1a04c606cefbe2"
  integrity sha512-+NYs2QeMWy+GWFOEm9xnn6HCDp0l7QBD7ml8zLUmJ+93Q5NF0NocErnwkTkXVFNiX3/fpC6afS8Dhb/gz7R7eg==

uvu@^0.5.0:
  version "0.5.6"
  resolved "https://registry.yarnpkg.com/uvu/-/uvu-0.5.6.tgz#2754ca20bcb0bb59b64e9985e84d2e81058502df"
  integrity sha512-+g8ENReyr8YsOc6fv/NVJs2vFdHBnBNdfE49rshrTzDWOlUx4Gq7KOS2GD8eqhy2j+Ejq29+SbKH8yjkAqXqoA==
  dependencies:
    dequal "^2.0.0"
    diff "^5.0.0"
    kleur "^4.0.3"
    sade "^1.7.3"

validator@^13.7.0:
  version "13.7.0"
  resolved "https://registry.yarnpkg.com/validator/-/validator-13.7.0.tgz#4f9658ba13ba8f3d82ee881d3516489ea85c0857"
  integrity sha512-nYXQLCBkpJ8X6ltALua9dRrZDHVYxjJ1wgskNt1lH9fzGjs3tgojGSCBjmEPwkWS1y29+DrizMTW19Pr9uB2nw==

vfile-message@^3.0.0:
  version "3.1.3"
  resolved "https://registry.yarnpkg.com/vfile-message/-/vfile-message-3.1.3.tgz#1360c27a99234bebf7bddbbbca67807115e6b0dd"
  integrity sha512-0yaU+rj2gKAyEk12ffdSbBfjnnj+b1zqTBv3OQCTn8yEB02bsPizwdBPrLJjHnK+cU9EMMcUnNv938XcZIkmdA==
  dependencies:
    "@types/unist" "^2.0.0"
    unist-util-stringify-position "^3.0.0"

vfile@^5.0.0:
  version "5.3.6"
  resolved "https://registry.yarnpkg.com/vfile/-/vfile-5.3.6.tgz#61b2e70690cc835a5d0d0fd135beae74e5a39546"
  integrity sha512-ADBsmerdGBs2WYckrLBEmuETSPyTD4TuLxTrw0DvjirxW1ra4ZwkbzG8ndsv3Q57smvHxo677MHaQrY9yxH8cA==
  dependencies:
    "@types/unist" "^2.0.0"
    is-buffer "^2.0.0"
    unist-util-stringify-position "^3.0.0"
    vfile-message "^3.0.0"

web-namespaces@^2.0.0:
  version "2.0.1"
  resolved "https://registry.yarnpkg.com/web-namespaces/-/web-namespaces-2.0.1.tgz#1010ff7c650eccb2592cebeeaf9a1b253fd40692"
  integrity sha512-bKr1DkiNa2krS7qxNtdrtHAmzuYGFQLiQ13TsorsdT6ULTkPLKuu5+GsFpDlg6JFjUTwX2DyhMPG2be8uPrqsQ==

web-streams-polyfill@^3.0.3:
  version "3.2.1"
  resolved "https://registry.yarnpkg.com/web-streams-polyfill/-/web-streams-polyfill-3.2.1.tgz#71c2718c52b45fd49dbeee88634b3a60ceab42a6"
  integrity sha512-e0MO3wdXWKrLbL0DgGnUV7WHVuw9OUvL4hjgnPkIeEvESk74gAITi5G606JtZPp39cd8HA9VQzCIvA49LpPN5Q==

webidl-conversions@^3.0.0:
  version "3.0.1"
  resolved "https://registry.yarnpkg.com/webidl-conversions/-/webidl-conversions-3.0.1.tgz#24534275e2a7bc6be7bc86611cc16ae0a5654871"
  integrity sha512-2JAn3z8AR6rjK8Sm8orRC0h/bcl/DqL7tRPdGZ4I1CjdF+EaMLmYxBHyXuKL849eucPFhvBoxMsflfOb8kxaeQ==

webpack-bundle-analyzer@4.7.0:
  version "4.7.0"
  resolved "https://registry.yarnpkg.com/webpack-bundle-analyzer/-/webpack-bundle-analyzer-4.7.0.tgz#33c1c485a7fcae8627c547b5c3328b46de733c66"
  integrity sha512-j9b8ynpJS4K+zfO5GGwsAcQX4ZHpWV+yRiHDiL+bE0XHJ8NiPYLTNVQdlFYWxtpg9lfAQNlwJg16J9AJtFSXRg==
  dependencies:
    acorn "^8.0.4"
    acorn-walk "^8.0.0"
    chalk "^4.1.0"
    commander "^7.2.0"
    gzip-size "^6.0.0"
    lodash "^4.17.20"
    opener "^1.5.2"
    sirv "^1.0.7"
    ws "^7.3.1"

whatwg-url@^5.0.0:
  version "5.0.0"
  resolved "https://registry.yarnpkg.com/whatwg-url/-/whatwg-url-5.0.0.tgz#966454e8765462e37644d3626f6742ce8b70965d"
  integrity sha512-saE57nupxk6v3HY35+jzBwYa0rKSy0XR8JSxZPwgLr7ys0IBzhGviA1/TUGJLmSVqs8pb9AnvICXEuOHLprYTw==
  dependencies:
    tr46 "~0.0.3"
    webidl-conversions "^3.0.0"

which-boxed-primitive@^1.0.2:
  version "1.0.2"
  resolved "https://registry.yarnpkg.com/which-boxed-primitive/-/which-boxed-primitive-1.0.2.tgz#13757bc89b209b049fe5d86430e21cf40a89a8e6"
  integrity sha512-bwZdv0AKLpplFY2KZRX6TvyuN7ojjr7lwkg6ml0roIy9YeuSr7JS372qlNW18UQYzgYK9ziGcerWqZOmEn9VNg==
  dependencies:
    is-bigint "^1.0.1"
    is-boolean-object "^1.1.0"
    is-number-object "^1.0.4"
    is-string "^1.0.5"
    is-symbol "^1.0.3"

which@^2.0.1:
  version "2.0.2"
  resolved "https://registry.yarnpkg.com/which/-/which-2.0.2.tgz#7c6a8dd0a636a0327e10b59c9286eee93f3f51b1"
  integrity sha512-BLI3Tl1TW3Pvl70l3yq3Y64i+awpwXqsGBYWkkqMtnbXgrMD+yj7rhW0kuEDxzJaYXGjEW5ogapKNMEKNMjibA==
  dependencies:
    isexe "^2.0.0"

wicg-inert@^3.1.2:
  version "3.1.2"
  resolved "https://registry.yarnpkg.com/wicg-inert/-/wicg-inert-3.1.2.tgz#df10cf756b773a96fce107c3ddcd43be5d1e3944"
  integrity sha512-Ba9tGNYxXwaqKEi9sJJvPMKuo063umUPsHN0JJsjrs2j8KDSzkWLMZGZ+MH1Jf1Fq4OWZ5HsESJID6nRza2ang==

wicked-good-xpath@1.3.0:
  version "1.3.0"
  resolved "https://registry.yarnpkg.com/wicked-good-xpath/-/wicked-good-xpath-1.3.0.tgz#81b0e95e8650e49c94b22298fff8686b5553cf6c"
  integrity sha512-Gd9+TUn5nXdwj/hFsPVx5cuHHiF5Bwuc30jZ4+ronF1qHK5O7HD0sgmXWSEgwKquT3ClLoKPVbO6qGwVwLzvAw==

wide-align@^1.1.0:
  version "1.1.5"
  resolved "https://registry.yarnpkg.com/wide-align/-/wide-align-1.1.5.tgz#df1d4c206854369ecf3c9a4898f1b23fbd9d15d3"
  integrity sha512-eDMORYaPNZ4sQIuuYPDHdQvf4gyCF9rEEV/yPxGfwPkRodwEgiMUUXTx/dex+Me0wxx53S+NgUHaP7y3MGlDmg==
  dependencies:
    string-width "^1.0.2 || 2 || 3 || 4"

word-wrap@^1.2.3:
  version "1.2.3"
  resolved "https://registry.yarnpkg.com/word-wrap/-/word-wrap-1.2.3.tgz#610636f6b1f703891bd34771ccb17fb93b47079c"
  integrity sha512-Hz/mrNwitNRh/HUAtM/VT/5VH+ygD6DV7mYKZAtHOrbs8U7lvPS6xf7EJKMF0uW1KJCl0H701g3ZGus+muE5vQ==

workspace-tools@^0.29.0:
  version "0.29.1"
  resolved "https://registry.yarnpkg.com/workspace-tools/-/workspace-tools-0.29.1.tgz#ff38f7484961cd87a342a8fd14eacd31d1645f56"
  integrity sha512-BVPROxNszGmyaUD2ErLWP4BpCiIkG1P//CnziOvHd27o1TeBm+7T1HKlYu89T4XGAjgPL/NP+tZ4j6aBvG/p/A==
  dependencies:
    "@yarnpkg/lockfile" "^1.1.0"
    git-url-parse "^13.0.0"
    globby "^11.0.0"
    jju "^1.4.0"
    js-yaml "^4.1.0"
    micromatch "^4.0.0"

wrap-ansi@^7.0.0:
  version "7.0.0"
  resolved "https://registry.yarnpkg.com/wrap-ansi/-/wrap-ansi-7.0.0.tgz#67e145cff510a6a6984bdf1152911d69d2eb9e43"
  integrity sha512-YVGIj2kamLSTxw6NsZjoBxfSwsn0ycdesmc4p+Q21c5zPuZ1pl+NfxVdxPtdHvmNVOQ6XSYG4AUtyt/Fi7D16Q==
  dependencies:
    ansi-styles "^4.0.0"
    string-width "^4.1.0"
    strip-ansi "^6.0.0"

wrappy@1:
  version "1.0.2"
  resolved "https://registry.yarnpkg.com/wrappy/-/wrappy-1.0.2.tgz#b5243d8f3ec1aa35f1364605bc0d1036e30ab69f"
  integrity sha512-l4Sp/DRseor9wL6EvV2+TuQn63dMkPjZ/sp9XkghTEbV9KlPS1xUsZ3u7/IQO4wxtcFB4bgpQPRcR3QCvezPcQ==

ws@^7.3.1:
  version "7.5.9"
  resolved "https://registry.yarnpkg.com/ws/-/ws-7.5.9.tgz#54fa7db29f4c7cec68b1ddd3a89de099942bb591"
  integrity sha512-F+P9Jil7UiSKSkppIiD94dN07AwvFixvLIj1Og1Rl9GGMuNipJnV9JzjD6XuqmAeiswGvUmNLjr5cFuXwNS77Q==

xml2js@^0.4.19:
  version "0.4.23"
  resolved "https://registry.yarnpkg.com/xml2js/-/xml2js-0.4.23.tgz#a0c69516752421eb2ac758ee4d4ccf58843eac66"
  integrity sha512-ySPiMjM0+pLDftHgXY4By0uswI3SPKLDw/i3UXbnO8M/p28zqexCUoPmQFrYD+/1BzhGJSs2i1ERWKJAtiLrug==
  dependencies:
    sax ">=0.6.0"
    xmlbuilder "~11.0.0"

xmlbuilder@~11.0.0:
  version "11.0.1"
  resolved "https://registry.yarnpkg.com/xmlbuilder/-/xmlbuilder-11.0.1.tgz#be9bae1c8a046e76b31127726347d0ad7002beb3"
  integrity sha512-fDlsI/kFEx7gLvbecc0/ohLG50fugQp8ryHzMTuW9vSa1GJ0XYWKnhsUx7oie3G98+r56aTQIUB4kht42R3JvA==

xmldom-sre@0.1.31:
  version "0.1.31"
  resolved "https://registry.yarnpkg.com/xmldom-sre/-/xmldom-sre-0.1.31.tgz#10860d5bab2c603144597d04bf2c4980e98067f4"
  integrity sha512-f9s+fUkX04BxQf+7mMWAp5zk61pciie+fFLC9hX9UVvCeJQfNHRHXpeo5MPcR0EUf57PYLdt+ZO4f3Ipk2oZUw==

xss@^1.0.14:
  version "1.0.14"
  resolved "https://registry.yarnpkg.com/xss/-/xss-1.0.14.tgz#4f3efbde75ad0d82e9921cc3c95e6590dd336694"
  integrity sha512-og7TEJhXvn1a7kzZGQ7ETjdQVS2UfZyTlsEdDOqvQF7GoxNfY+0YLCzBy1kPdsDDx4QuNAonQPddpsn6Xl/7sw==
  dependencies:
    commander "^2.20.3"
    cssfilter "0.0.10"

xtend@^4.0.2:
  version "4.0.2"
  resolved "https://registry.yarnpkg.com/xtend/-/xtend-4.0.2.tgz#bb72779f5fa465186b1f438f674fa347fdb5db54"
  integrity sha512-LKYU1iAXJXUgAXn9URjiu+MWhyUXHsvfp7mcuYm9dSUKK0/CjtrUwFAxD82/mCWbtLsGjFIad0wIsod4zrTAEQ==

xxhashjs@~0.2.2:
  version "0.2.2"
  resolved "https://registry.yarnpkg.com/xxhashjs/-/xxhashjs-0.2.2.tgz#8a6251567621a1c46a5ae204da0249c7f8caa9d8"
  integrity sha512-AkTuIuVTET12tpsVIQo+ZU6f/qDmKuRUcjaqR+OIvm+aCBsZ95i7UVY5WJ9TMsSaZ0DA2WxoZ4acu0sPH+OKAw==
  dependencies:
    cuint "^0.2.2"

y18n@^5.0.5:
  version "5.0.8"
  resolved "https://registry.yarnpkg.com/y18n/-/y18n-5.0.8.tgz#7f4934d0f7ca8c56f95314939ddcd2dd91ce1d55"
  integrity sha512-0pfFzegeDWJHJIAmTLRP2DwHjdF5s7jo9tuztdQxAhINCdvS+3nGINqPd00AphqJR/0LhANUS6/+7SCb98YOfA==

yallist@^3.0.2:
  version "3.1.1"
  resolved "https://registry.yarnpkg.com/yallist/-/yallist-3.1.1.tgz#dbb7daf9bfd8bac9ab45ebf602b8cbad0d5d08fd"
  integrity sha512-a4UGQaWPH59mOXUYnAG2ewncQS4i4F43Tv3JoAM+s2VDAmS9NsK8GpDMLrCHPksFT7h3K6TOoUNn2pb7RoXx4g==

yallist@^4.0.0:
  version "4.0.0"
  resolved "https://registry.yarnpkg.com/yallist/-/yallist-4.0.0.tgz#9bb92790d9c0effec63be73519e11a35019a3a72"
  integrity sha512-3wdGidZyq5PB084XLES5TpOSRA3wjXAlIWMhum2kRcv/41Sn2emQ0dycQW4uZXLejwKvg6EsvbdlVL+FYEct7A==

yaml-loader@^0.8.0:
  version "0.8.0"
  resolved "https://registry.yarnpkg.com/yaml-loader/-/yaml-loader-0.8.0.tgz#c839325e3fdee082b3768b2a21fe34fde5d96f61"
  integrity sha512-LjeKnTzVBKWiQBeE2L9ssl6WprqaUIxCSNs5tle8PaDydgu3wVFXTbMfsvF2MSErpy9TDVa092n4q6adYwJaWg==
  dependencies:
    javascript-stringify "^2.0.1"
    loader-utils "^2.0.0"
    yaml "^2.0.0"

yaml@^1.10.0, yaml@^1.10.2:
  version "1.10.2"
  resolved "https://registry.yarnpkg.com/yaml/-/yaml-1.10.2.tgz#2301c5ffbf12b467de8da2333a459e29e7920e4b"
  integrity sha512-r3vXyErRCYJ7wg28yvBY5VSoAF8ZvlcW9/BwUzEtUsjvX/DKs24dIkuwjtuprwJJHsbyUbLApepYTR1BN4uHrg==

yaml@^2.0.0:
  version "2.2.0"
  resolved "https://registry.yarnpkg.com/yaml/-/yaml-2.2.0.tgz#882c762992888b4144bffdec5745df340627fdd3"
  integrity sha512-auf7Gi6QwO7HW//GA9seGvTXVGWl1CM/ADWh1+RxtXr6XOxnT65ovDl9fTi4e0monEyJxCHqDpF6QnFDXmJE4g==

yargs-parser@^18.1.3:
  version "18.1.3"
  resolved "https://registry.yarnpkg.com/yargs-parser/-/yargs-parser-18.1.3.tgz#be68c4975c6b2abf469236b0c870362fab09a7b0"
  integrity sha512-o50j0JeToy/4K6OZcaQmW6lyXXKhq7csREXcDwk2omFPJEwUNOVtJKvmDr9EI1fAJZUyZcRF7kxGBWmRXudrCQ==
  dependencies:
    camelcase "^5.0.0"
    decamelize "^1.2.0"

yargs-parser@^20.2.2:
  version "20.2.9"
  resolved "https://registry.yarnpkg.com/yargs-parser/-/yargs-parser-20.2.9.tgz#2eb7dc3b0289718fc295f362753845c41a0c94ee"
  integrity sha512-y11nGElTIV+CT3Zv9t7VKl+Q3hTQoT9a1Qzezhhl6Rp21gJ/IVTW7Z3y9EWXhuUBC2Shnf+DX0antecpAwSP8w==

yargs@^16.1.1:
  version "16.2.0"
  resolved "https://registry.yarnpkg.com/yargs/-/yargs-16.2.0.tgz#1c82bf0f6b6a66eafce7ef30e376f49a12477f66"
  integrity sha512-D1mvvtDG0L5ft/jGWkLpG1+m0eQxOfaBvTNELraWj22wSVUMWxZUvYgJYcKh6jGGIkJFhH4IZPQhR4TKpc8mBw==
  dependencies:
    cliui "^7.0.2"
    escalade "^3.1.1"
    get-caller-file "^2.0.5"
    require-directory "^2.1.1"
    string-width "^4.2.0"
    y18n "^5.0.5"
    yargs-parser "^20.2.2"

yocto-queue@^0.1.0:
  version "0.1.0"
  resolved "https://registry.yarnpkg.com/yocto-queue/-/yocto-queue-0.1.0.tgz#0294eb3dee05028d31ee1a5fa2c556a6aaf10a1b"
  integrity sha512-rVksvsnNCdJ/ohGc6xgPwyN8eheCxsiLM8mxuE/t/mOVqJewPuO1miLpTHQiRgTKCLexL4MeAFVagts7HmNZ2Q==

z-schema@~5.0.2:
  version "5.0.5"
  resolved "https://registry.yarnpkg.com/z-schema/-/z-schema-5.0.5.tgz#6805a48c5366a6125cae0e58752babfd503daf32"
  integrity sha512-D7eujBWkLa3p2sIpJA0d1pr7es+a7m0vFAnZLlCEKq/Ij2k0MLi9Br2UPxoxdYystm5K1yeBGzub0FlYUEWj2Q==
  dependencies:
    lodash.get "^4.4.2"
    lodash.isequal "^4.5.0"
    validator "^13.7.0"
  optionalDependencies:
    commander "^9.4.1"

zwitch@^2.0.0:
  version "2.0.4"
  resolved "https://registry.yarnpkg.com/zwitch/-/zwitch-2.0.4.tgz#c827d4b0acb76fc3e685a4c6ec2902d51070e9d7"
  integrity sha512-bXE4cR/kVZhKZX/RjPEflHaKVhUVl85noU3v6b8apfQEc1x4A+zBxjZ4lN8LqGd6WZ3dl98pY4o717VFmoPp+A==

```

`/Users/nikola/dev/marp/package.json`:

```json
{
  "name": "@marp-team/marp",
  "description": "The entrance repository of Markdown presentation ecosystem",
  "private": true,
  "license": "MIT",
  "author": {
    "name": "Marp team",
    "url": "https://github.com/marp-team"
  },
  "contributors": [
    {
      "name": "Yuki Hattori",
      "url": "https://github.com/yhatt"
    }
  ],
  "repository": {
    "type": "git",
    "url": "https://github.com/marp-team/marp"
  },
  "workspaces": [
    "website"
  ],
  "prettier": {
    "semi": false,
    "singleQuote": true
  },
  "scripts": {
    "check:format": "yarn -s format -c",
    "check:ts": "yarn lage check:ts",
    "format:write": "yarn -s format --write",
    "format": "prettier \"**/*.{css,js,jsx,json,md,mdx,scss,ts,tsx,yaml,yml}\"",
    "lint:js": "eslint --report-unused-disable-directives --cache .",
    "website": "yarn workspace @marp-team/marp-website dev"
  },
  "devDependencies": {
    "@tsconfig/recommended": "^1.0.1",
    "@types/node": "~18.11.18",
    "@typescript-eslint/eslint-plugin": "^5.47.1",
    "@typescript-eslint/parser": "^5.47.1",
    "eslint": "^8.30.0",
    "eslint-config-prettier": "^8.3.0",
    "eslint-import-resolver-typescript": "^3.5.2",
    "eslint-plugin-import": "^2.25.4",
    "lage": "^1.9.6",
    "prettier": "^2.8.1",
    "typescript": "^4.9.4"
  },
  "resolutions": {
    "json5": "^2.2.2"
  }
}

```

`/Users/nikola/dev/marp/tsconfig.json`:

```json
{
  "extends": "@tsconfig/recommended/tsconfig.json",
  "compilerOptions": {
    "lib": ["es2015", "dom"],
    "noImplicitAny": false,
    "resolveJsonModule": true,
    "strict": true
  }
}

```