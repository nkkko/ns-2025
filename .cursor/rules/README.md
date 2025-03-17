# Cursor Rules for Network Science Course

This directory contains rules for maintaining consistent and high-quality content across the Network Science course materials.

## Lecture-Related Rules

### Image Generation and Integration

The following rules provide guidelines for creating and using images in lecture slides:

1. **[Lecture Image Generation](lecture-image-generation.mdc)**: Guidelines for creating Python scripts that generate images to support lecture slides.
   - Script organization and best practices
   - Image formatting and sizing
   - Function structure for reproducible visualizations
   - Dependencies and requirements management

2. **[Lecture Image Linking](lecture-image-linking.mdc)**: Guidelines for effectively linking and using generated images within Marp-based lecture slides.
   - Basic image linking in Markdown
   - Image sizing guidelines
   - Background images usage
   - Image-code pairing techniques
   - Progressive image reveals for step-by-step demonstrations

### Marp Presentation Rules

These rules ensure consistency across Marp slide decks:

1. **[Marp Slide Structure](marp-slide-structure.mdc)**: Guidelines for structuring Marp slides effectively.
   - Slide separation and organization
   - Frontmatter configuration
   - Consistent header usage

2. **[Marp Directives and Styling](marp-directives-styling.mdc)**: Guidelines for using Marp directives and styling.
   - Global and local directives
   - CSS customization
   - Theme consistency

3. **[Marp Content Best Practices](marp-content-best-practices.mdc)**: Guidelines for creating effective content in Marp presentations.
   - Text content organization
   - Code blocks formatting
   - Diagrams and tables usage

4. **[Marp Advanced Features](marp-advanced-features.mdc)**: Guidelines for using Marp's advanced features.
   - Background images and filters
   - Split backgrounds
   - Animations and transitions
   - Math equations

5. **[Marp Export and Presentation](marp-export-presentation.mdc)**: Guidelines for exporting and presenting Marp slides.
   - Export formats and commands
   - File organization
   - Speaker notes

## Using These Rules

### For Creating New Lecture Material

1. **Setting up a new lecture**:
   - Create a new directory under `lectures/XX` (where XX is the lecture number)
   - Create a `lecture.md` file following the Marp slide structure guidelines
   - Create an `images` subdirectory for visualizations

2. **Generating images**:
   - Create a Python script (e.g., `generate_images.py`) in the lecture directory
   - Use the image generation template as a starting point
   - Run the script to generate images into the `images` subdirectory

3. **Linking images in slides**:
   - Use the image linking guidelines to include generated images in your slides
   - Test the presentation by previewing with a Marp viewer

### For Maintaining Consistency

- Refer to these rules when reviewing or updating existing lectures
- Use the rules as a checklist when creating new content
- Ensure all team members follow these guidelines for consistent output

## Templates

Related templates can be found in the [templates directory](..templates/):

- [`image_generation_template.py`](../templates/image_generation_template.py): A template Python script for generating lecture images