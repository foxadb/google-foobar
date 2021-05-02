def boolean_matrix_to_integer_columns(g):
    """
    Transform columns of a boolean matrix into an array of integers
    """
    return [sum(g[i][j] << i for i in range(len(g))) for j in range(len(g[0]))]


def compute_image(x, y, image_size):
    """
    Compute image of two vectors x and y following the game of life rule
    saying 2x2 blocks must contain exactly one thruthy bit to be thruthy
    """
    a = x & ~(1 << image_size)  # top left
    b = x >> 1  # bottom left
    c = y & ~(1 << image_size)  # top right
    d = y >> 1  # bottom right
    return (a & ~b & ~c & ~d) \
        | (~a & b & ~c & ~d) \
        | (~a & ~b & c & ~d) \
        | (~a & ~b & ~c & d)


def compute_all_images(image_size):
    """
    Compute images with all possible couples of antecedent integers between
    0 and 2^(image_size + 1). Note that the complexity is O(2^(2 * image_size))
    so the fact that image_size is maximum 9 makes this run in limited time
    """
    max_antecedent = 1 << (image_size + 1)
    return [
        [compute_image(i, j, image_size) for j in range(max_antecedent)]
        for i in range(max_antecedent)
    ]


def count_antecedents(image_ints, all_images):
    """
    Iterate through the array of images and find the antecedents for each one.
    We store the counter of paths to reach each antecedent in a dictionary.
    Note that we only need the counter to answer the problem, so it is useless
    to store the antecedent values and it helps in terms of space complexity
    """
    antecedents_count = {i: 1 for i in range(len(all_images))}
    for current_image in image_ints:
        next_antecedents_count = {i: 0 for i in range(len(all_images))}
        for current_antecedent in antecedents_count:
            for next_antecedent, computed_image in enumerate(all_images[current_antecedent]):
                if (computed_image == current_image):
                    next_antecedents_count[next_antecedent] += antecedents_count[current_antecedent]
        antecedents_count = next_antecedents_count
    return sum(antecedents_count.values())


def solution(g):
    """
    We transform the matrix columns to binary integers then we compute images
    of all possible antecedents. It is important to iterate through columns and
    not through rows because matrix height is limited to 9 but width could go up
    to 50 so we have 2^50 = 1125899906842624 possible antecedents for each rows
    but only 2^10 = 1024 antecedents for each columns
    """
    image_size = len(g)  # matrix height (max. 9)
    image_ints = boolean_matrix_to_integer_columns(g)
    all_images = compute_all_images(image_size)
    return count_antecedents(image_ints, all_images)
