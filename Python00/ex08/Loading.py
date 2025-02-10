import time
import shutil


def format_time(seconds: float) -> str:
    """
    Convert seconds to a human readable format
    """
    mins, secs = divmod(seconds, 60)
    return f"{int(mins):02}:{int(secs):02}"


def ft_tqdm(lst: range) -> None:  # type: ignore
    """
    works the same as tqdm but self written
    """
    width = shutil.get_terminal_size().columns
    bar_width = width - 40
    start = time.time()

    curr = -1
    total = len(lst)
    print("\r", end="", flush=True)
    for item in lst:
        curr += 1
        time_elapsed = time.time() - start
        percentage = (curr + 1) / total
        bar_length = int(bar_width * percentage)
        progbar = f"{'█' * bar_length}{' ' * (bar_width - bar_length)}"
        itpersec = (curr + 1) / time_elapsed
        est_total_time = time_elapsed / percentage
        est_remaining_time = est_total_time - time_elapsed
        percentage_str = f"{percentage:.0%}".rjust(4)
        elapsed_str = format_time(time_elapsed)
        remaining_str = format_time(est_remaining_time)
        print(
            f"\r{percentage_str}|{progbar}| {curr + 1}/{total} "
            f"[{elapsed_str}<{remaining_str}, {itpersec:.2f}it/s]",
            end="", flush=True
        )
        yield item
