// Imports 
import { config, fields, collection } from '@keystatic/core';

// Keystatic Config 
export default config({
  storage: {
    kind: 'local',
  },
  collections: {
    NewspaperPosts: collection({
      label: 'NewspaperPosts',
      slugField: 'title',
      path: 'src/content/posts/*',
      format: { contentField: 'content' },
      schema:
      {
        title: fields.slug({ name: { label: 'Title' } }),
        content: fields.document({
          label: 'Content',
          formatting: true,
          dividers: true,
          links: true,
          images: {
            directory: 'src/assets/images/posts',
            publicPath: '../../assets/images/posts/',
          },
        }),
        publishedAt: fields.datetime({
          label: 'Event date and time',
          description: 'The date and time of the event',
          defaultValue:{
            kind: 'now'
        }
        }),
        tags: fields.array(
          fields.text({ label: 'Tag' }),
          {
            label: 'Tag',
            itemLabel: props => props.value
          }
        ),
        authors: fields.array(
          fields.relationship({
            label: 'Authors',
            description: 'A list of authors for this post',
            collection: 'Authors',
            validation: {
              isRequired: true
            }
          }), {
          label: 'Authors',
          itemLabel: props => props.value as string
        }
        ),
        coverImage: fields.image({
          label: 'Post Cover Image',
          description: 'Image for Post Cover',
          directory: 'public/images/posts/cover',
          publicPath: '/images/posts/cover'
        }),
        isFeatured: fields.checkbox({
          label: 'is Featured',
          description: 'Set this post as Featured '
        }),
        draft: fields.checkbox({
          label: 'is Draft',
          description: 'Set this post as draft to prevent it from being published'
        }),
      },
    }),
    Authors: collection({
      label: 'Authors',
      slugField: 'id',
      format: { data: 'json' },
      path: 'src/content/authors/*',
      schema: {
        avatar: fields.image({
          label: 'Author\'s Avatar Image',
          description: 'Image for Author Profile Pic',
          directory: 'public/images/authors/profile',
          publicPath: '/images/authors/profiler'
        }),
        id: fields.text({
          label: 'Author ID',
          defaultValue: `${crypto.randomUUID()}`,
          validation: {
            length: {
              min: 36,
              max: 36
            },
          },
        }),
        name: fields.text({
          label: 'Author Name',
          validation: {
            length: {
              min: 5
            }
          }
        }),
        email: fields.text({
          label: 'Author Email',
          validation: {
            length: {
              min: 6
            }
          }
        }),
      },
    }),
  },
});
