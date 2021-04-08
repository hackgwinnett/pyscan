<img src="https://raw.githubusercontent.com/hershyz/pyscan/main/pyscan.png"/>
<p><i>JSON parsing module for Python.</i></p>

<h4>Usage:</h4>
<pre>
<b>Importing the module:</b>
import pyscan
<br/><b>Supported commands:</b>
pyscan.get_groups(json_path)                 Returns an array of all groups in a JSON file.
pyscan.get_indiv(json_path)                  Returns an array of all non-grouped properties in a JSON file.
pyscan.read_indiv(json_path, name)           Returns the value of a non-grouped property in a JSON file.
pyscan.read_group(json_path, group, name)    Returns the value of a grouped property in a JSON file.
</pre>
