// @ts-ignore
import { defineCollection, z } from 'astro:content';

// Zod Schemas 
const Author = z.object({
  id: z.string().uuid(),
  name: z.string(),
  email: z.string().email(),
  avatar: z.string()
});

const NewspaperPost = z.object({
  id: z.string().uuid(),
  title: z.string().min(5),
  content: z.string(),
  publishedAt: z.date(),
  tags: z.array(z.string()),
  authors: z.array(Author).optional(),
  coverImage: z.array(z.string().url()).optional(),
  isFeatured: z.boolean().default(false),
  isDraft: z.boolean().default(false)
});

// Collections 
const Authors = defineCollection({
  type: 'data',
  schema: Author,
});

const NewspaperPosts = defineCollection({
  type: 'content',
  schema: NewspaperPost,
});

// Exporting 
export const collections = { NewspaperPosts,Authors };
