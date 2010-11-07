

<form action="/page/save" method="POST">
    <input type="hidden" name="_id"></input>
    <ul>
        <li>
            <label for="page_url">URL</label>
            <input type="text" name="page_url"></input>
            <div class="error"></div>
        </li>
        
        <li>
            <label for="page_title">Title</label>
            <input type="text" name="page_title"></input>
            <div class="error"></div>
        </li>
        
        <li>
            <label for="page_body">Page body (HTML)</label>
            <textarea name="page_body"></textarea>
            <div class="error"></div>
        </li>
        
        <li>
            <label for="page_enabled">Visible for everybody</label>
            <input type="checkbox" name="page_enabled"></input>
        </li>
        
        <li>
            <input type="submit" value="Save"></input>
        </li>
        
</form>