import json

# Input and output file paths
input_file = 'training-dataset.jsonl'
output_file = 'filtered-dataset.jsonl'

# Define which keys to keep in the profile
profile_keys_to_keep = [
    'username', 'full_name', 'biography', 'post_count', 'follower_count', 'following_count',
    'is_business_account', 'is_private', 'is_verified', 'highlight_reel_count', 'entities'
]

# Define which keys to keep in each post
post_keys_to_keep = ['id', 'timestamp', 'caption', 'comments_count', 'like_count', 'media_type']

# Open the input file and the output file
with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
    for line in infile:
        # Parse the current line as a JSON object
        data = json.loads(line.strip())
        
        # Extract and filter the profile section
        profile = {key: data['profile'][key] for key in profile_keys_to_keep if key in data['profile']}
        
        # Extract and filter the posts section
        posts = []
        for post in data['posts']:
            filtered_post = {key: post[key] for key in post_keys_to_keep if key in post}
            posts.append(filtered_post)
        
        # Create the filtered data
        filtered_data = {
            'profile': profile,
            'posts': posts
        }
        
        # Write the filtered data as JSON to the output file
        outfile.write(json.dumps(filtered_data, ensure_ascii=False) + '\n')

print(f"Filtered data has been written to {output_file}")
