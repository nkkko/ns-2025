# MARP Cheatsheet

## Basic Setup and Configuration

```yaml
---
marp: true
theme: default
paginate: true
footer: 'Your Footer Text'
---
```

### Themes
- `default`: Standard theme
- `gaia`: Modern, colorful theme
- `uncover`: Minimal design with emphasis on content

### Common Frontmatter Options
- `marp: true` - Enables MARP
- `paginate: true` - Adds page numbers
- `header: 'Text'` - Adds a header to all slides
- `footer: 'Text'` - Adds a footer to all slides
- `backgroundColor: 'color'` - Sets slide background color
- `color: 'color'` - Sets text color
- `style: |` - Add custom CSS in frontmatter

## Slide Separation and Navigation

```markdown
# Slide 1

Content for first slide

---

# Slide 2

Content for second slide
```

### Section Slides
For organizing content into sections:

```markdown
<!-- _class: lead -->
# Section Title
```

## Text Formatting

### Headers
```markdown
# Level 1 Header (Title)
## Level 2 Header (Section)
### Level 3 Header (Subsection)
```

### Text Styles
```markdown
**Bold text**
*Italic text*
~~Strikethrough~~
`Inline code`
```

### Lists
```markdown
- Unordered list item
- Another item
  - Nested item

1. Ordered list item
2. Second item
   1. Nested ordered item
```

### Blockquotes
```markdown
> This is a blockquote
> Second line of quote
```

### Code Blocks
````markdown
```python
def example():
    return "This is code with syntax highlighting"
```
````

## Working with Images

### Basic Image
```markdown
![](path/to/image.png)
```

### Sized Images
```markdown
![width:500px](image.png)
![height:300px](image.png)
![width:500px height:300px](image.png)
```

### Image Positioning
```markdown
![center](image.png)
![right](image.png)
![left](image.png)
```

### Combined Attributes
```markdown
![width:400px center](image.png)
```

### Background Images
```markdown
![bg](background.jpg)
```

### Background Image Options
```markdown
![bg fit](background.jpg)
![bg cover](background.jpg)
![bg contain](background.jpg)
![bg opacity:.3](background.jpg)
![bg blur:5px](background.jpg)
![bg brightness:.8](background.jpg)
```

### Multiple Background Images
```markdown
![bg left:33%](left.jpg)
![bg right:67%](right.jpg)
```

## Tables

```markdown
| Header 1 | Header 2 | Header 3 |
|----------|----------|----------|
| Cell 1   | Cell 2   | Cell 3   |
| Cell 4   | Cell 5   | Cell 6   |
```

### Table Alignment
```markdown
| Left-aligned | Center-aligned | Right-aligned |
|:-------------|:--------------:|-------------:|
| Left         | Center         | Right        |
```

## Styling Individual Slides

### Custom Classes
```markdown
<!-- _class: custom-class -->
# Slide with Custom Class
```

### Custom Background
```markdown
<!-- _backgroundColor: lightblue -->
# Slide with Blue Background
```

### Custom Text Color
```markdown
<!-- _color: red -->
# Slide with Red Text
```

### Multiple Styles
```markdown
<!-- _class: lead -->
<!-- _backgroundColor: black -->
<!-- _color: white -->
# Dramatic Title Slide
```

## Custom CSS Styling

### In-Document CSS
```markdown
<style>
section {
  font-family: 'Arial', sans-serif;
}
h1 {
  color: #0066cc;
}
.custom-class {
  background-color: #f5f5f5;
}
</style>
```

### Local CSS Theme
```yaml
---
marp: true
theme: default
style: |
  section {
    background-color: #f5f5f5;
  }
  h1 {
    color: #0066cc;
  }
---
```

## Advanced Features

### Speaker Notes
```markdown
# Slide with Notes

Content visible on the slide

<!-- Note content only visible in presenter view -->
```

### Fragments (Progressive Disclosure)
```html
<div class="fragment">
  This content appears on click
</div>

<div class="fragment">
  This appears second
</div>
```

### Math Equations (using KaTeX)
```markdown
Inline equation: $E=mc^2$

Block equation:
$$
\frac{1}{n} \sum_{i=1}^{n} x_i
$$
```

### Emoji Support
```markdown
# I :heart: MARP! 😄
```

### Raw HTML
```markdown
<div class="custom-box">
  <p>Custom HTML content</p>
</div>
```

## Exporting and Presenting

### CLI Export Options
```
npx @marp-team/marp-cli slide.md --pdf
npx @marp-team/marp-cli slide.md --pptx
npx @marp-team/marp-cli slide.md --html
```

### VS Code Integration
- Install "Marp for VS Code" extension
- Preview slides in real-time
- Export from VS Code

## Tips and Best Practices

1. **Consistency**: Maintain consistent styling across slides
2. **Readability**: Use large fonts and high contrast colors
3. **Images**: Optimize images for file size and resolution
4. **Organization**: Use section slides to divide content
5. **Whitespace**: Leave enough space around content
6. **Templates**: Create reusable templates for common slide layouts
7. **Testing**: Test presentations on the target display resolution

## Common Issues and Solutions

### Images Not Displaying
- Check file paths are correct (relative to markdown file)
- Ensure image files exist in the referenced location
- Try using absolute paths if needed

### Styling Not Applied
- Check CSS syntax
- Make sure classes are correctly defined and applied
- Inspect with developer tools when viewing HTML output

### Export Problems
- Install required dependencies for PDF export
- Check permissions for output directories
- Update Marp CLI to latest version

## Resources

- [Marp Documentation](https://marpit.marp.app/)
- [Marp CLI](https://github.com/marp-team/marp-cli)
- [Marp VS Code Extension](https://marketplace.visualstudio.com/items?itemName=marp-team.marp-vscode)
- [Marp Core](https://github.com/marp-team/marp-core)