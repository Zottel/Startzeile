function Startzeile(config) {
	// Hooks
	this.hooks = {};
	this.addHook = function(event, callback){
		if(this.hooks[event] === undefined){
			this.hooks[event] = [];
		}

		this.hooks[event].push(callback);
	}
	this.delHook = function(event, callback){
		if(this.hooks[event] !== undefined){
			var index = this.hooks[event].indexOf(callback);
			if(index != -1){
				this.hooks[event].splice(index, 1);
			}
		}
	}
	this.callHook = function(event, data){
		if(this.hooks[event] !== undefined){
			this.hooks[event].forEach(function(callback){
				callback(data);
			});
		}
	};
	
}

function ResultList(startzeile, default_results) {
	var shown = false;
	var pages_container = undefined;
	var tags_container = undefined;
	
	this.show = function(p_container, t_container) {
		pages_container = p_container; tags_container = t_container;
		
		$(pages_container).empty();
		$(tags_container).empty();
		
	}
	
	this.resultPages(pages) {
		console.debug('resultPages', pages')
		if(pages_container === undefined) {
			return;
		}
	}
	
	this.resultTags(tags) {
		console.debug('resultTags', tags')
		if(tags_container === undefined) {
			return;
		}
	}
	
	//Setup
	startzeile.addHook('resultPages',
	                   $.proxy(this.resultPages, this));
	
	startzeile.addHook('resultTags',
	                   $.proxy(this.resultTags, this));
}

function Searchbox(startzeile, default_search) {
	var shown = false;
	var search_container = undefined;
	
	this.show = function(s_container) {
		search_container = s_container;
		$(s_container).val('');
	}
	
	// Setup
	
}
