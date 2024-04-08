{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1",
   "metadata": {},
   "outputs": [],
   "source": [
    "#pip install geemap"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3",
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "import os\n",
    "import ee\n",
    "import geemap\n",
    "import ipywidgets as widgets"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4",
   "metadata": {},
   "outputs": [],
   "source": [
    "Map = geemap.Map()\n",
    "Map"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5",
   "metadata": {},
   "outputs": [],
   "source": [
    "out_dir = os.path.join(os.path.expanduser(\"~\"), \"Downloads\")\n",
    "if not os.path.exists(out_dir):\n",
    "    os.makedirs(out_dir)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6",
   "metadata": {},
   "outputs": [],
   "source": [
    "style = {\"description_width\": \"initial\"}\n",
    "title = widgets.Text(\n",
    "    description=\"Title:\", value=\"Landsat Timelapse\", width=200, style=style\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7",
   "metadata": {},
   "outputs": [],
   "source": [
    "bands = widgets.Dropdown(\n",
    "    description=\"Select RGB Combo:\",\n",
    "    options=[\n",
    "        \"Red/Green/Blue\",\n",
    "        \"NIR/Red/Green\",\n",
    "        \"SWIR2/SWIR1/NIR\",\n",
    "        \"NIR/SWIR1/Red\",\n",
    "        \"SWIR2/NIR/Red\",\n",
    "        \"SWIR2/SWIR1/Red\",\n",
    "        \"SWIR1/NIR/Blue\",\n",
    "        \"NIR/SWIR1/Blue\",\n",
    "        \"SWIR2/NIR/Green\",\n",
    "        \"SWIR1/NIR/Red\",\n",
    "    ],\n",
    "    value=\"NIR/Red/Green\",\n",
    "    style=style,\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8",
   "metadata": {},
   "outputs": [],
   "source": [
    "hbox1 = widgets.HBox([title, bands])\n",
    "hbox1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9",
   "metadata": {},
   "outputs": [],
   "source": [
    "start_year = widgets.IntSlider(\n",
    "    description=\"Start Year:\", value=1984, min=1984, max=2021, style=style\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "10",
   "metadata": {},
   "outputs": [],
   "source": [
    "end_year = widgets.IntSlider(\n",
    "    description=\"End Year:\", value=2021, min=1984, max=2021, style=style\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "11",
   "metadata": {},
   "outputs": [],
   "source": [
    "hbox2 = widgets.HBox([start_year, end_year])\n",
    "hbox2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "12",
   "metadata": {},
   "outputs": [],
   "source": [
    "speed = widgets.IntSlider(\n",
    "    description=\"Frames per second:\",\n",
    "    tooltip=\"Frames per second:\",\n",
    "    value=10,\n",
    "    min=1,\n",
    "    max=30,\n",
    "    style=style,\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "13",
   "metadata": {},
   "outputs": [],
   "source": [
    "download = widgets.Checkbox(value=False, description=\"Download the GIF\", style=style)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "14",
   "metadata": {},
   "outputs": [],
   "source": [
    "hbox3 = widgets.HBox([speed, download])\n",
    "hbox3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "15",
   "metadata": {},
   "outputs": [],
   "source": [
    "font_size = widgets.IntSlider(\n",
    "    description=\"Font size:\", value=30, min=10, max=50, style=style\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "16",
   "metadata": {},
   "outputs": [],
   "source": [
    "font_color = widgets.ColorPicker(\n",
    "    concise=False, description=\"Font color:\", value=\"white\", style=style\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "17",
   "metadata": {},
   "outputs": [],
   "source": [
    "progress_bar_color = widgets.ColorPicker(\n",
    "    concise=False, description=\"Progress bar color:\", value=\"blue\", style=style\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "18",
   "metadata": {},
   "outputs": [],
   "source": [
    "hbox4 = widgets.HBox([font_size, font_color, progress_bar_color])\n",
    "hbox4"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "19",
   "metadata": {},
   "outputs": [],
   "source": [
    "submit = widgets.Button(\n",
    "    description=\"Submit\",\n",
    "    button_style=\"primary\",\n",
    "    tooltip=\"Click the submit the request to create timelapse\",\n",
    "    style=style,\n",
    ")\n",
    "\n",
    "output = widgets.Output()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "20",
   "metadata": {},
   "outputs": [],
   "source": [
    "def submit_clicked(b):\n",
    "    with output:\n",
    "        output.clear_output()\n",
    "        if start_year.value >= end_year.value:\n",
    "            print(\"The end year must be great than the start year.\")\n",
    "            return\n",
    "        print(\"Computing...\")\n",
    "\n",
    "        Map.add_landsat_ts_gif(\n",
    "            roi=Map.user_roi,\n",
    "            label=title.value,\n",
    "            start_year=start_year.value,\n",
    "            end_year=end_year.value,\n",
    "            start_date=\"05-01\",\n",
    "            end_date=\"10-31\",\n",
    "            bands=bands.value.split(\"/\"),\n",
    "            font_color=font_color.value,\n",
    "            frames_per_second=speed.value,\n",
    "            font_size=font_size.value,\n",
    "            progress_bar_color=progress_bar_color.value,\n",
    "            download=download.value,\n",
    "        )\n",
    "\n",
    "\n",
    "submit.on_click(submit_clicked)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "21",
   "metadata": {},
   "outputs": [],
   "source": [
    "submit"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "22",
   "metadata": {},
   "outputs": [],
   "source": [
    "output"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5060ad18-71a5-4656-b81a-2f263a136ac3",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
