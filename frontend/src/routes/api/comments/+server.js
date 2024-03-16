import {json} from '@sveltejs/kit';
import {comments} from '$lib/comments.js';
export function GET(){
    return json(comments);
}

export async function POST(requestEvent){
   
    const {text} = await requestEvent.request.json();
    const newComment = {
        id: comments.length + 1,
        text
    };
    comments.push(newComment);
    return json(newComment,{status:201});
}   