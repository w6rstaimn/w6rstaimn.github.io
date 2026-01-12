import { getCollection } from 'astro:content';
const posts = await getCollection('blog');
posts.forEach(p => console.log('ID:', p.id, 'Slug:', p.slug));
